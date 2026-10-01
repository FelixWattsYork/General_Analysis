"""Consensus KBM / MTM / mixed classification of a linear gyrokinetic mode (Fusion_PhD-7k70).

Three indicators, each a few lines from pyrokinetics quantities:
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

# ---- cutoffs: ONE place. Values are set by the calibration in results/mode_classification/ ----
# Calibrated on GS2 NSTX_MTM n1000 + SPR-045 kbm_8d + M1 kbm_8d (notebooks/mode_classification_calibration.ipynb).
T_BAL = 0.05         # T below this is ballooning parity (KBM): 99.5% of SPR-045/M1 cases lie below; NSTX T has a sparse 0.01-0.3 tail
T_TEAR = 0.7         # T above this is tearing parity (MTM): the NSTX_MTM population peaks at 0.7-1; 0.5-0.7 is a shoulder and is left 'mixed'
CHI_KBM = (0.5, 2.0) # KBM band of chi_e/chi_i: Kotschenreuther T1 gives chi_i/chi_e ~ 1; our ion-direction T<0.05 cases have IQR 0.5-1.0
CHI_MTM = 10.0       # MTM: chi_e/chi_i above this: Kotschenreuther T1 gives chi_i/chi_e ~ 1/10; our T>0.7 NSTX cases have 5th percentile ~40
DE_CHI_KBM = 0.4     # KBM: D_e/chi_e above this: Kotschenreuther T1 gives 2/3 for KBM, small/negative for ITG/TEM; ours peaks 0.55-1.5


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
    """'KBM' / 'MTM' / 'mixed': a label only if every indicator agrees."""
    c = ind["chi_ratio"]
    if (ind["omega"] > 0 and ind["T"] < T_BAL and CHI_KBM[0] < c < CHI_KBM[1]
            and (DE_CHI_KBM is None or ind["de_chi"] > DE_CHI_KBM)):
        return "KBM"
    if ind["omega"] < 0 and ind["T"] > T_TEAR and c > CHI_MTM:
        return "MTM"
    return "mixed"
