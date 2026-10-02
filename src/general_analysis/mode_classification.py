"""Consensus KBM / MTM / mixed classification of a linear gyrokinetic mode (Fusion_PhD-7k70).

Three indicators, each a few lines from pyrokinetics quantities (D_e/chi_e is still reported, no longer cut on):
  T      tearing parameter |int A_par dl| / int |A_par| dl (Hatch et al. 2012, PRL 108, 235002)
  omega  signed mode frequency, ion direction > 0, electron direction < 0
  chi    chi_e/chi_i from chi_s = (Q_s - 1.5 T_s Gamma_s)/(n_s T_s a/L_Ts)
         (Kotschenreuther et al. 2019, NF 59 096001; Kennedy et al. 2023)
plus optional D_e/chi_e, D_s = Gamma_s/(n_s a/L_ns), which separates KBM from ITG/TEM in
Kotschenreuther's Table 1 (KBM ~2/3, ITG/TEM small or negative).

Purpose: find regions of parameter space that are CLEARLY one mode type, so classify() is a
tough consensus filter: anything not agreeing on every indicator is 'mixed'.
"""
import numpy as np
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


def indicators(pyro):
    """T, omega, chi_e/chi_i, D_e/chi_e of the final time of a loaded GS2 linear run.

    `pyro` needs gk_output loaded with fields and fluxes, plus its local_species and geometry.
    """
    out, ls = pyro.gk_output, pyro.local_species
    last = lambda a: a.isel(time=-1) if "time" in a.dims else a
    T = float(FieldLine(pyro).compute_linear_tearing_parameter().squeeze())
    omega = ION_DIRECTION * float(last(out["mode_frequency"]).squeeze())
    heat = last(out["heat"]).sum("field").squeeze().pint.dequantify()     # total over phi, apar, bpar
    part = last(out["particle"]).sum("field").squeeze().pint.dequantify()
    sp = lambda s: (float(ls[s].temp.m), float(ls[s].dens.m), float(ls[s].inverse_lt.m), float(ls[s].inverse_ln.m))

    np.seterr(divide="ignore", invalid="ignore")  # zero-flux (non-converged) runs give nan, not an exception

    def chi(names):  # summed over the species in `names`; temperatures and densities are in tref, nref
        num = den = 0.0
        for s in names:
            t, n, alt, _ = sp(s)
            num += float(heat.sel(species=s)) - 1.5 * t * float(part.sel(species=s))
            den += n * t * alt
        return np.float64(num) / den

    ions = [s for s in ls.names if s != "electron"]
    chi_e, chi_i = chi(["electron"]), chi(ions)
    _, n_e, _, aln_e = sp("electron")
    return dict(T=T, omega=omega, chi_e=chi_e, chi_i=chi_i, chi_ratio=np.float64(chi_e) / chi_i,
                de_chi=np.float64(float(part.sel(species="electron"))) / (n_e * aln_e) / chi_e)


def classify(ind):
    """'KBM' / 'MTM' / 'mixed': a label only if every criterion agrees."""
    if ind["omega"] > 0 and ind["T"] < T_BAL and CHI_KBM[0] < ind["chi_ratio"] < CHI_KBM[1]:
        return "KBM"
    if ind["omega"] < 0 and ind["T"] > T_TEAR:
        return "MTM"
    return "mixed"


def classify_T_omega(ind):
    """As classify() from T and omega only, for GFTM/TGLF (no per-mode flux weights, Fusion_PhD-9lgj)."""
    return classify({**ind, "chi_ratio": np.sqrt(CHI_KBM[0] * CHI_KBM[1])})
