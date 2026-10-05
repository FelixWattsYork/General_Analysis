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


def indicators(scan, ds):
    """T, omega, chi_e/chi_i per sample, from a PyroScan/PyroHypercube `scan` and its final-time GK output dataset `ds`.

    ds: PyroScanGKOutput.from_netcdf(...).data with sample, complex apar, mode_frequency, heat, particle (the scan's pyro_cube).
    Sample i's Pyro is the scan's base with that sample's scanned values applied (scan.update_self_parameters); its apar is
    attached as gk_output so FieldLine computes T with that sample's own geometry. Species (T, n, a/L_T) come from the same Pyro.
    """
    names = [str(n) for n in ds.sample_name.values]
    assert names == list(scan.sample_names), "scan and dataset samples differ"
    scan.update_self_parameters()
    apar = ds["apar"].squeeze().pint.dequantify()
    T = []
    for n, a in zip(names, apar):
        a = a.dropna("theta")  # ragged-theta cubes (R4) are NaN-padded outside the sample's own grid
        if a.theta.size == 0:  # failed run: no eigenfunction
            T.append(np.nan)
            continue
        pyro = scan.pyro_dict[n]
        pyro.gk_output = xr.Dataset({"apar": a})
        T.append(float(FieldLine(pyro).compute_linear_tearing_parameter().squeeze()))
    T = np.array(T)
    heat = ds["heat"].sum("field").pint.dequantify()
    part = ds["particle"].sum("field").pint.dequantify()
    np.seterr(divide="ignore", invalid="ignore")  # zero-flux (non-converged) samples give nan, not an exception

    def chi(group):  # summed over the species in `group`; temperatures and densities are in tref, nref
        num = den = 0.0
        for s in group:
            t, n, alt = np.array([[float(scan.pyro_dict[k].local_species[s].temp.m), float(scan.pyro_dict[k].local_species[s].dens.m),
                                   float(scan.pyro_dict[k].local_species[s].inverse_lt.m)] for k in names]).T
            num = num + heat.sel(species=s).values - 1.5 * t * part.sel(species=s).values
            den = den + n * t * alt
        return num / den

    chi_e, chi_i = chi(["electron"]), chi([str(s) for s in ds.species.values if s != "electron"])
    return xr.Dataset({"T": ("sample", T), "omega": ("sample", ION_DIRECTION * ds["mode_frequency"].pint.dequantify().values.ravel()),
                       "chi_ratio": ("sample", chi_e / chi_i)}, coords={"sample": ds.sample.values, "sample_name": ("sample", names)})


def classify(ind):
    """'KBM' / 'MTM' / 'mixed' (array over samples, or a scalar for one dict): a label only if every criterion agrees."""
    kbm = (ind["omega"] > 0) & (ind["T"] < T_BAL) & (CHI_KBM[0] < ind["chi_ratio"]) & (ind["chi_ratio"] < CHI_KBM[1])
    mtm = (ind["omega"] < 0) & (ind["T"] > T_TEAR)
    return np.select([kbm, mtm], ["KBM", "MTM"], "mixed")


def classify_T_omega(ind):
    """As classify() from T and omega only, for GFTM/TGLF (no per-mode flux weights, Fusion_PhD-9lgj)."""
    return classify({**ind, "chi_ratio": np.sqrt(CHI_KBM[0] * CHI_KBM[1])})
