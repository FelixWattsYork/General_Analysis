#!/usr/bin/env python3
"""Plot selected flux surfaces (R vs Z) from a GEQDSK file.

Usage: python plot_flux_surfaces.py jetto.eqdsk_out [out.pdf]
"""

import sys

import matplotlib.pyplot as plt
import numpy as np
from pyrokinetics.equilibrium import read_equilibrium

R_LIST = [0.16, 0.33, 0.49, 0.65, 0.82]  # r/a of surfaces to plot

eq_file = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else "surfaces.pdf"

eq = read_equilibrium(eq_file, "GEQDSK", psi_n_lcfs=0.999)

plt.figure(figsize=(5.25, 3.75))
for r_a in R_LIST:
    psin = np.interp(r_a, eq["rho"].data.magnitude, eq["psi_n"].data.magnitude)
    surf = eq.flux_surface(psi_n=psin)
    R, Z = surf["R"].data.magnitude, surf["Z"].data.magnitude
    plt.plot(R, Z, "k")

plt.xlabel("R [m]")
plt.ylabel("Z [m]")
plt.axis("square")
plt.xlim(R.min() * 0.9, R.max() * 1.1)  # outermost surface (R_LIST ascending)
plt.tight_layout()
plt.savefig(out)
