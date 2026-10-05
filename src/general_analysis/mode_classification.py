"""Consensus KBM / MTM / mixed classification of a linear gyrokinetic mode (Fusion_PhD-7k70).

Three indicators, each a few lines from pyrokinetics quantities:
  T      tearing parameter |int A_par dl| / int |A_par| dl (Hatch et al. 2012, PRL 108, 235002)
  omega  signed mode frequency, ion direction > 0, electron direction < 0
  chi    chi_e/chi_i from chi_s = (Q_s - 1.5 T_s Gamma_s)/(n_s T_s a/L_Ts)
         (Kotschenreuther et al. 2019, NF 59 096001; Kennedy et al. 2023)

Purpose: find regions of parameter space that are CLEARLY one mode type, so classify() is a
tough consensus filter: anything not agreeing on every indicator is 'mixed'.
"""
import numpy as np
import xarray as xr
from pathlib import Path
from pyrokinetics import Pyro, PyroHypercube, PyroScan
from pyrokinetics.pyroscan import PyroScanGKOutput
from pyrokinetics.diagnostics.field_line import FieldLine

# Pyrokinetics' convention: mode_frequency > 0 is the ion direction, < 0 the electron direction.
# Source: pyrokinetics gk_code/cgyro.py ("-ve is electron direction"), gene.py ("Match pyro
# convention for ion/electron direction"); confirmed on our GS2 data in
# Fusion_PhD results/mode_classification (NSTX MTM cases are omega < 0, see README).
ION_DIRECTION = +1

# ---- cutoffs: ONE place. User's final criteria, 2026-10-01 (Fusion_PhD docs/mode_filtering.md, Fusion_PhD-lqwx) ----
# Supersedes the Fusion_PhD-7k70 calibration (T_TEAR 0.7, CHI_KBM (0.5, 2), CHI_MTM 10, DE_CHI_KBM 0.4); the
# MTM chi_e/chi_i cut and the KBM D_e/chi_e cut are removed at the user's request.
T_BAL = 0.05         # KBM: T below this (ballooning parity)
T_TEAR = 0.15        # MTM: T above this (tearing parity)
CHI_KBM = (0.25, 4.0)  # KBM: chi_e/chi_i band


def _tie_species(pyro):
    """The KBM hypercubes' deck rule: every ion shares the first ion's a/L_T, and every species' a/L_n is the electron's."""
    ls = pyro.local_species
    ions = [s for s in ls.names if s != "electron"]
    for s in ions[1:]:
        ls[s].inverse_lt = ls[ions[0]].inverse_lt
    for s in ions:
        ls[s].inverse_ln = ls["electron"].inverse_ln


def attach_legacy_funcs(scan):
    """Re-attach the derived settings of GS2 scans whose pyroscan.json predates parameter_func serialisation.

    Measured against each run's own deck (Fusion_PhD-k8w8): beta_prime follows beta, and the KBM cubes tie ion and electron gradients.
    Scans saved with named parameter_func (pyro sample_pyro) carry these in their json and do not need this.
    """
    if "beta" in scan.parameter_dict:
        scan.add_parameter_func("beta", "enforce_consistent_beta_prime", {})
    for k in ("deuterium_temp_gradient", "electron_dens_gradient"):
        if k in scan.parameter_dict:
            scan.add_parameter_func(k, _tie_species, {})
    return scan


def load_gs2_cube(base, cube=None, file_name="gs2.in"):
    """(scan, ds) of a GS2 Latin-hypercube database `base` (the directory holding pyro_cube/ and the run directories).

    cube: 'pyro_cube' (final time) or 'pyro_cube_avg' (tail average); default the final-time cube if there is one.
    R4's cube_eigenfunctions.nc is used where present (ragged theta, see indicators()). Nothing in the run directories is read.
    """
    base = Path(base)
    cd = base / (cube or next(c for c in ("pyro_cube", "pyro_cube_avg") if (base / c / "cube.nc").exists()))
    nc = cd / "cube_eigenfunctions.nc" if (cd / "cube_eigenfunctions.nc").exists() else cd / "cube.nc"
    scan = PyroHypercube(pyro=Pyro(gk_file=cd / "pyroscan_base.input", gk_code="GS2"), pyroscan_json=cd / "pyroscan.json",
                         base_directory=base, file_name=file_name)
    return attach_legacy_funcs(scan), PyroScanGKOutput.from_netcdf(nc).data


def load_gridded_cube(cube_dir, code="GS2", file_name="gs2.in"):
    """(scan, ds) of a gridded PyroScan cube directory (pyroscan.json + cube.nc), e.g. GS2 KX_SCAN's pyro_cube_avg; ds has one 'sample' dim."""
    cd = Path(cube_dir)
    scan = PyroScan(pyro=Pyro(gk_file=cd / "pyroscan_base.input", gk_code=code), pyroscan_json=cd / "pyroscan.json",
                    base_directory=cd.parent, file_name=file_name)
    return attach_legacy_funcs(scan), as_samples(scan, PyroScanGKOutput.from_netcdf(cd / "cube.nc").data)


def as_samples(scan, ds):
    """ds with a single 'sample' dimension in the scan's run order: a gridded PyroScan's parameter dims are stacked, first parameter outermost."""
    if "sample" in ds.dims:
        return ds
    ds = ds.stack(sample=list(scan.parameter_dict)).reset_index("sample")
    ds = ds.assign_coords(sample=np.arange(ds.sizes["sample"]), sample_name=("sample", list(scan.pyro_dict)))
    return ds.transpose("sample", ...)


def load_gftm_cube(leaf):
    """(scan, ds) of a GFTM leaf: a GyroRun leaf (pyroscan.json + pyroscan.nc at its root) or a legacy one (pyro_cube/cube.nc + pyroscan.json)."""
    leaf = Path(leaf)
    cd = leaf / "pyro_cube" if (leaf / "pyro_cube" / "cube.nc").exists() else leaf
    scan = PyroHypercube(pyro=Pyro(gk_file=cd / "pyroscan_base.input", gk_code="GFTM"), pyroscan_json=cd / "pyroscan.json",
                         base_directory=leaf, file_name="input.gftm")
    return scan, PyroScanGKOutput.from_netcdf(cd / ("cube.nc" if (cd / "cube.nc").exists() else "pyroscan.nc")).data


def tearing_parity(scan, ds, samples=None):
    """Tearing parameter T and apar even fraction E for every sample (and mode, kx...) of a cube, from the cube's complex apar.

    apar is ds['apar'], else the 'apar' field of ds['eigenfunctions'] (legacy cubes). Sample i's Pyro is scan.sample_pyro(i, gk_output=...)
    (its own geometry, no run directory); FieldLine does the rest. samples: positions to compute (default all); the others are NaN.
    """
    ds = as_samples(scan, ds)
    apar = (ds["apar"] if "apar" in ds else ds["eigenfunctions"].sel(field="apar")).pint.dequantify()
    n = apar.sizes["sample"]
    todo = range(n) if samples is None else sorted(int(i) for i in samples)
    T, E = {}, {}
    for i in todo:
        a = apar.isel(sample=i, drop=True).dropna("theta", how="all").sortby("theta")  # ragged / padded theta grids
        if not a.theta.size:
            continue
        fl = FieldLine(scan.sample_pyro(i, gk_output=xr.Dataset({"apar": a})))
        T[i], E[i] = fl.compute_linear_tearing_parameter(), fl.compute_linear_parity()
    ref = next(iter(T.values()))
    nan = xr.full_like(ref, np.nan, dtype=float)
    stack = lambda d: xr.concat([d.get(i, nan) for i in range(n)], "sample")
    return xr.Dataset({"T": stack(T), "E": stack(E)}).assign_coords(sample_name=("sample", ds.sample_name.values))


def indicators(scan, ds):
    """T, apar even fraction E, omega, chi_e/chi_i per sample, from a PyroScan/PyroHypercube `scan` and its final-time GK output dataset `ds`.

    ds: PyroScanGKOutput.from_netcdf(...).data with sample, complex apar, mode_frequency, heat, particle (the scan's pyro_cube).
    Sample i's Pyro is scan.sample_pyro(i, gk_output=...): the base with that sample's scanned values and derived settings
    applied, its apar attached; FieldLine gives T with that sample's geometry and the same Pyro gives T_s, n_s, a/L_Ts.
    """
    ds = as_samples(scan, ds)
    names = [str(n) for n in ds.sample_name.values]
    assert names == list(scan.pyro_dict), "scan and dataset samples differ"
    apar = ds["apar"].squeeze().pint.dequantify()
    sp, T, E = {}, [], []
    for i, (n, a) in enumerate(zip(names, apar)):
        # ragged-theta cubes (R4) are NaN-padded and their theta axis is the unsorted union of the samples' grids
        a = a.dropna("theta").sortby("theta")
        pyro = scan.sample_pyro(i, gk_output=xr.Dataset({"apar": a}))
        fl = FieldLine(pyro) if a.theta.size else None
        T.append(float(fl.compute_linear_tearing_parameter().squeeze()) if fl else np.nan)
        E.append(float(fl.compute_linear_parity().squeeze()) if fl else np.nan)  # apar even fraction, about theta = 0
        sp[n] = {s: (float(pyro.local_species[s].temp.m), float(pyro.local_species[s].dens.m), float(pyro.local_species[s].inverse_lt.m))
                 for s in pyro.local_species.names}  # keep numbers, not 1000 Pyros
    T = np.array(T)
    heat = ds["heat"].sum("field").pint.dequantify()
    part = ds["particle"].sum("field").pint.dequantify()
    np.seterr(divide="ignore", invalid="ignore")  # zero-flux (non-converged) samples give nan, not an exception

    def chi(group):  # summed over the species in `group`; temperatures and densities are in tref, nref
        num = den = 0.0
        for s in group:
            t, n, alt = np.array([sp[k][s] for k in names]).T
            num = num + heat.sel(species=s).values - 1.5 * t * part.sel(species=s).values
            den = den + n * t * alt
        return num / den

    chi_e, chi_i = chi(["electron"]), chi([str(s) for s in ds.species.values if s != "electron"])
    return xr.Dataset({"T": ("sample", T), "E": ("sample", np.array(E)), "omega": ("sample", ION_DIRECTION * ds["mode_frequency"].pint.dequantify().values.ravel()),
                       "chi_ratio": ("sample", chi_e / chi_i)}, coords={"sample": ds.sample.values, "sample_name": ("sample", names)})


def classify(ind):
    """'KBM' / 'MTM' / 'mixed' (array over samples, or a scalar for one dict): a label only if every criterion agrees."""
    kbm = (ind["omega"] > 0) & (ind["T"] < T_BAL) & (CHI_KBM[0] < ind["chi_ratio"]) & (ind["chi_ratio"] < CHI_KBM[1])
    mtm = (ind["omega"] < 0) & (ind["T"] > T_TEAR)
    return np.select([kbm, mtm], ["KBM", "MTM"], "mixed")


def classify_T_omega(ind):
    """As classify() from T and omega only, for GFTM/TGLF (no per-mode flux weights, Fusion_PhD-9lgj)."""
    return classify({**ind, "chi_ratio": np.sqrt(CHI_KBM[0] * CHI_KBM[1])})
