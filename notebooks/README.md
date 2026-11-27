# Analysis notebooks

**Layout rule.** Any nonlinear content goes in `nonlinear/`. Linear-only work goes in `linear/`, by database
(`KBM`, `MTM`, or `general` when tied to none), then by the point it supports. Work with no GK data goes in
`theory/`. Each folder holds at most about 10 notebooks; beyond that, make subfolders. Notebooks are atomic.

**Naming rule (user, 2026-11-27).** A notebook's filename, and its figures' filenames, say *what is plotted*, not what the
analysis is: `<y>_vs_<x>_per_<line or panel variable>`, e.g. `gamma_rms_error_vs_fixed_width_per_filter.ipynb`.
- `_and_` separates **different plots** (panels or figures) and is used for nothing else:
  `phi_extent_ratio_and_gamma_rms_error_vs_fixed_width_per_filter` is two panels. Quantities drawn on **one** plot are
  joined with plain `_`: `phi_apar_extent_ratio_vs_fixed_width` is one panel with both fields.
- Atomic: one notebook per kind of figure. A notebook whose parts make different kinds of plot is several notebooks.
- No analysis words (`convergence`, `rule`, `oracle`, `physics`, `collapse`, `check`) unless the plot literally shows that.
- Figure files carry the code as a prefix when a notebook draws one figure per code: `tglf_<name>.png`, `gftm_<name>.png`.
- Markdown cells say what the code below them does (what is loaded, what is computed, what is plotted against what), not the
  question or the verdict (user, 2026-11-27). Verdicts go in the Fusion_PhD results README.

Every notebook finds the repository by searching upward for `pyproject.toml`, so depth does not matter. Each
notebook sets its own path under `Plots/`, independent of its folder. The results column is the directory under
`results/` in Fusion_PhD holding the published copy.


## theory

No GK data: Gaussian-Hermite fits and similar.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [gaussian_hermite_projection_vs_theta_per_width_ratio_nbasis](theory/gaussian_hermite_projection_vs_theta_per_width_ratio_nbasis.ipynb) | Hermite projections of a Gaussian: fit error against mismatch (talk slides 11-12) | talk_20261102 |

## linear/KBM/tglf_width_search

**Argument step: the width search is unreliable.** TGLF over-prediction, FIND_WIDTH, FILTER x NBASIS, SAT1/SAT2.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [tglf_default_gamma_vs_gs2_gamma_colour_ky](linear/KBM/tglf_width_search/tglf_default_gamma_vs_gs2_gamma_colour_ky.ipynb) | TGLF default width search against GS2, growth-rate scatter (talk slide 9) | talk_20261102 |
| [tglf_gamma_vs_gs2_gamma_per_width_choice](linear/KBM/tglf_width_search/tglf_gamma_vs_gs2_gamma_per_width_choice.ipynb) | Growth-rate bias of the search against GS2, with tables | tglf_search_bias |
| [tglf_searched_width_shift_and_gamma_error_vs_search_nbasis_per_filter](linear/KBM/tglf_width_search/tglf_searched_width_shift_and_gamma_error_vs_search_nbasis_per_filter.ipynb) | Selected width vs search basis, best fixed WIDTH and NBASIS | tglf_find_width |
| [tglf_gamma_error_and_omega_error_vs_width_per_nbasis](linear/KBM/tglf_width_search/tglf_gamma_error_and_omega_error_vs_width_per_nbasis.ipynb) | Selected width vs search basis, best fixed WIDTH and NBASIS | tglf_find_width |
| [tglf_gamma_vs_gs2_gamma_per_filter_nbasis](linear/KBM/tglf_width_search/tglf_gamma_vs_gs2_gamma_per_filter_nbasis.ipynb) | FILTER x NBASIS vs GS2 on the four kbm_free databases | tglf_filter_width |
| [tglf_filter0_width_vs_filter2_width_per_nbasis](linear/KBM/tglf_width_search/tglf_filter0_width_vs_filter2_width_per_nbasis.ipynb) | FILTER x NBASIS vs GS2 on the four kbm_free databases | tglf_filter_width |
| [tglf_sat1_sat2_gamma_vs_gs2_gamma_per_filter_nbasis](linear/KBM/tglf_width_search/tglf_sat1_sat2_gamma_vs_gs2_gamma_per_filter_nbasis.ipynb) | SAT1 (EM search) vs SAT2 (ES search) vs GS2 on kbm_free | tglf_sat1_sat2 |
| [tglf_sat1_sat2_extent_vs_gs2_extent_per_filter_nbasis](linear/KBM/tglf_width_search/tglf_sat1_sat2_extent_vs_gs2_extent_per_filter_nbasis.ipynb) | SAT1 (EM search) vs SAT2 (ES search) vs GS2 on kbm_free | tglf_sat1_sat2 |
| [tglf_sat1_sat2_selected_width_and_extent_ratio_vs_nbasis_per_filter](linear/KBM/tglf_width_search/tglf_sat1_sat2_selected_width_and_extent_ratio_vs_nbasis_per_filter.ipynb) | SAT1 (EM search) vs SAT2 (ES search) vs GS2 on kbm_free | tglf_sat1_sat2 |
| [tglf_searched_width_vs_best_extent_width_per_nbasis](linear/KBM/tglf_width_search/tglf_searched_width_vs_best_extent_width_per_nbasis.ipynb) | TGLF SAT1/SAT2 search width against the per-KBM oracle width (best extents vs GS2) from the fixed-width runs | width_search_vs_oracle |
| [tglf_within_tolerance_fraction_and_extent_error_vs_search_nbasis_per_sat](linear/KBM/tglf_width_search/tglf_within_tolerance_fraction_and_extent_error_vs_search_nbasis_per_sat.ipynb) | TGLF SAT1/SAT2 search width against the per-KBM oracle width (best extents vs GS2) from the fixed-width runs | width_search_vs_oracle |
| [gs2_equivalent_width_histogram_per_database](linear/KBM/tglf_width_search/gs2_equivalent_width_histogram_per_database.ipynb) | Equivalent Gaussian width of each GS2-KBM field from its 95 % extent in $\theta_b$, against the oracle and search widths, and the NBASIS it implies | equivalent_gaussian_width |
| [tglf_gftm_best_width_and_searched_width_vs_gs2_width_range_per_nbasis](linear/KBM/tglf_width_search/tglf_gftm_best_width_and_searched_width_vs_gs2_width_range_per_nbasis.ipynb) | Equivalent Gaussian width of each GS2-KBM field from its 95 % extent in $\theta_b$, against the oracle and search widths, and the NBASIS it implies | equivalent_gaussian_width |
| [gftm_nbasis_needed_vs_width_ratio_per_field](linear/KBM/tglf_width_search/gftm_nbasis_needed_vs_width_ratio_per_field.ipynb) | Equivalent Gaussian width of each GS2-KBM field from its 95 % extent in $\theta_b$, against the oracle and search widths, and the NBASIS it implies | equivalent_gaussian_width |
| [gftm_searched_width_gamma_vs_gs2_gamma_per_nbasis](linear/KBM/tglf_width_search/gftm_searched_width_gamma_vs_gs2_gamma_per_nbasis.ipynb) | GFTM emulated max-gamma width search (grid, no bisection) vs GS2, FILTER 0.5 and 0, vs fixed 0.4 and TGLF searches | gftm_width_search |
| [tglf_gftm_searched_width_gamma_ratio_vs_nbasis_per_filter](linear/KBM/tglf_width_search/tglf_gftm_searched_width_gamma_ratio_vs_nbasis_per_filter.ipynb) | GFTM emulated max-gamma width search (grid, no bisection) vs GS2, FILTER 0.5 and 0, vs fixed 0.4 and TGLF searches | gftm_width_search |
| [tglf_gamma_error_and_omega_error_vs_width_per_mode_filter](linear/KBM/tglf_width_search/tglf_gamma_error_and_omega_error_vs_width_per_mode_filter.ipynb) | Extent filter on top of TGLF's frequency filter | kbm_extent_filter_tglf |
| [tglf_extent_ratio_vs_width_per_mode_filter](linear/KBM/tglf_width_search/tglf_extent_ratio_vs_width_per_mode_filter.ipynb) | Extent filter on top of TGLF's frequency filter | kbm_extent_filter_tglf |
| [tglf_gamma_error_and_omega_error_vs_search_upper_width_per_width_choice](linear/KBM/tglf_width_search/tglf_gamma_error_and_omega_error_vs_search_upper_width_per_width_choice.ipynb) | Extent filter on top of TGLF's frequency filter | kbm_extent_filter_tglf |

## linear/KBM/tglf_gftm_resolution/single_kbm

**Argument step: fixed width against NBASIS**, on one KBM.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [gs2_tglf_gftm_field_eigenfunction_vs_theta_per_width_nbasis](linear/KBM/tglf_gftm_resolution/single_kbm/gs2_tglf_gftm_field_eigenfunction_vs_theta_per_width_nbasis.ipynb) | One KBM (SPR-045 sample_0818) against WIDTH and NBASIS, GFTM and TGLF; v2 section (qp5.41): fig3 under TGLF SAT2 / NXGRID >= NBASIS+8 | spr045_single_kbm |
| [tglf_gftm_gamma_and_omega_and_extent_ratio_vs_width_per_nbasis](linear/KBM/tglf_gftm_resolution/single_kbm/tglf_gftm_gamma_and_omega_and_extent_ratio_vs_width_per_nbasis.ipynb) | One KBM (SPR-045 sample_0818) against WIDTH and NBASIS, GFTM and TGLF; v2 section (qp5.41): fig3 under TGLF SAT2 / NXGRID >= NBASIS+8 | spr045_single_kbm |
| [tglf_gftm_selected_width_and_gamma_and_extent_ratio_vs_nbasis_per_solver](linear/KBM/tglf_gftm_resolution/single_kbm/tglf_gftm_selected_width_and_gamma_and_extent_ratio_vs_nbasis_per_solver.ipynb) | One KBM (SPR-045 sample_0818) against WIDTH and NBASIS, GFTM and TGLF; v2 section (qp5.41): fig3 under TGLF SAT2 / NXGRID >= NBASIS+8 | spr045_single_kbm |
| [tglf_gftm_phi_and_apar_eigenfunction_vs_theta_per_nbasis_width](linear/KBM/tglf_gftm_resolution/single_kbm/tglf_gftm_phi_and_apar_eigenfunction_vs_theta_per_nbasis_width.ipynb) | How WIDTH and NBASIS resolve its eigenfunction, one figure per code (talk slide 16) | talk_20261102 |
| [gs2_phi_and_apar_eigenfunction_vs_theta](linear/KBM/tglf_gftm_resolution/single_kbm/gs2_phi_and_apar_eigenfunction_vs_theta.ipynb) | Its GS2 eigenfunction, real and imaginary parts (talk slide 17) | talk_20261102 |
| [tglf_gftm_gamma_ratio_vs_width_per_nbasis](linear/KBM/tglf_gftm_resolution/single_kbm/tglf_gftm_gamma_ratio_vs_width_per_nbasis.ipynb) | Its $\gamma_{code}/\gamma_{GS2}$ against WIDTH (talk slide 18) | talk_20261102 |
| [tglf_gftm_gs2_field_eigenfunction_vs_theta_per_knob_value](linear/KBM/tglf_gftm_resolution/single_kbm/tglf_gftm_gs2_field_eigenfunction_vs_theta_per_knob_value.ipynb) | TGLF physics knobs (THETA_TRAPPED, XNU_FACTOR, PARK, GHAT, GCHAT, DAMP_*, LINSKER, GRADB, SAT presets) on this one KBM: $\gamma$, $\omega$, extents, overlap with GS2, and how the eigenfunction changes (qp5.47) | spr045_single_kbm |
| [tglf_gamma_ratio_and_omega_ratio_and_extent_ratio_and_overlap_vs_knob_per_nbasis](linear/KBM/tglf_gftm_resolution/single_kbm/tglf_gamma_ratio_and_omega_ratio_and_extent_ratio_and_overlap_vs_knob_per_nbasis.ipynb) | TGLF physics knobs (THETA_TRAPPED, XNU_FACTOR, PARK, GHAT, GCHAT, DAMP_*, LINSKER, GRADB, SAT presets) on this one KBM: $\gamma$, $\omega$, extents, overlap with GS2, and how the eigenfunction changes (qp5.47) | spr045_single_kbm |
| [tglf_omega_ratio_and_overlap_vs_gamma_ratio_per_knob](linear/KBM/tglf_gftm_resolution/single_kbm/tglf_omega_ratio_and_overlap_vs_gamma_ratio_per_knob.ipynb) | TGLF physics knobs (THETA_TRAPPED, XNU_FACTOR, PARK, GHAT, GCHAT, DAMP_*, LINSKER, GRADB, SAT presets) on this one KBM: $\gamma$, $\omega$, extents, overlap with GS2, and how the eigenfunction changes (qp5.47) | spr045_single_kbm |

## linear/KBM/tglf_gftm_resolution/kbm_database

**Argument step: fixed width against NBASIS**, over the KBM databases.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [gs2_width_from_abs_phi_vs_width_from_complex_phi_per_database](linear/KBM/tglf_gftm_resolution/kbm_database/gs2_width_from_abs_phi_vs_width_from_complex_phi_per_database.ipynb) | Does the Galerkin field solve make low-NBASIS width selection reliable | gftm_galerkin_field |
| [gftm_overshoot_and_width_and_gamma_error_and_extent_error_vs_nbasis_per_field_solver](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_overshoot_and_width_and_gamma_error_and_extent_error_vs_nbasis_per_field_solver.ipynb) | Does the Galerkin field solve make low-NBASIS width selection reliable | gftm_galerkin_field |
| [gftm_changed_mode_fraction_vs_ky_per_field_solver](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_changed_mode_fraction_vs_ky_per_field_solver.ipynb) | Does the Galerkin field solve make low-NBASIS width selection reliable | gftm_galerkin_field |
| [gftm_gamma_error_and_extent_error_vs_width_per_field_solver](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_gamma_error_and_extent_error_vs_width_per_field_solver.ipynb) | Does the Galerkin field solve make low-NBASIS width selection reliable | gftm_galerkin_field |
| [gftm_gamma_and_omega_vs_gs2_per_width_choice](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_gamma_and_omega_vs_gs2_per_width_choice.ipynb) | Does the Galerkin field solve make low-NBASIS width selection reliable | gftm_galerkin_field |
| [gftm_searched_width_error_vs_fixed_width_error_per_database](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_searched_width_error_vs_fixed_width_error_per_database.ipynb) | Does the Galerkin field solve make low-NBASIS width selection reliable | gftm_galerkin_field |
| [gftm_gamma_error_and_omega_error_vs_run_time_per_width_choice](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_gamma_error_and_omega_error_vs_run_time_per_width_choice.ipynb) | Does the Galerkin field solve make low-NBASIS width selection reliable | gftm_galerkin_field |
| [gftm_best_width_vs_gs2_extent_per_nbasis](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_best_width_vs_gs2_extent_per_nbasis.ipynb) | GFTM error against the Hermite-basis width mismatch $s$ | kbm_width_collapse |
| [gftm_gamma_error_and_omega_error_and_extent_error_vs_scaled_width_per_nbasis](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_gamma_error_and_omega_error_and_extent_error_vs_scaled_width_per_nbasis.ipynb) | GFTM error against the Hermite-basis width mismatch $s$ | kbm_width_collapse |
| [gs2_field_extent_ratio_histogram_per_database](linear/KBM/tglf_gftm_resolution/kbm_database/gs2_field_extent_ratio_histogram_per_database.ipynb) | GFTM error against the Hermite-basis width mismatch $s$ | kbm_width_collapse |
| [gftm_gamma_error_vs_gs2_extent_per_settings](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_gamma_error_vs_gs2_extent_per_settings.ipynb) | GFTM error against the Hermite-basis width mismatch $s$ | kbm_width_collapse |
| [gftm_run_time_vs_nbasis_and_vs_scaled_width](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_run_time_vs_nbasis_and_vs_scaled_width.ipynb) | GFTM error against the Hermite-basis width mismatch $s$ | kbm_width_collapse |
| [tglf_gftm_gamma_error_and_omega_error_and_gamma_ratio_vs_width_per_nbasis](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_gftm_gamma_error_and_omega_error_and_gamma_ratio_vs_width_per_nbasis.ipynb) | TGLF and GFTM error vs WIDTH per NBASIS | kbm_width_collapse |
| [tglf_gftm_gamma_error_and_omega_error_and_gamma_ratio_vs_width_per_nbasis_tglf_filter0](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_gftm_gamma_error_and_omega_error_and_gamma_ratio_vs_width_per_nbasis_tglf_filter0.ipynb) | The same with TGLF at FILTER 0 | kbm_width_collapse |
| [gftm_gamma_error_and_omega_error_and_no_ion_mode_fraction_vs_filter_per_width](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_gamma_error_and_omega_error_and_no_ion_mode_fraction_vs_filter_per_width.ipynb) | GFTM accuracy vs FILTER and WIDTH | kbm_filter_width |
| [gftm_gamma_error_and_omega_error_and_no_ion_mode_fraction_vs_width_per_filter](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_gamma_error_and_omega_error_and_no_ion_mode_fraction_vs_width_per_filter.ipynb) | GFTM accuracy vs FILTER and WIDTH | kbm_filter_width |
| [tglf_gamma_ratio_and_omega_ratio_and_extent_ratio_vs_knob_per_mode](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_gamma_ratio_and_omega_ratio_and_extent_ratio_vs_knob_per_mode.ipynb) | Converged TGLF KBM $\gamma$ against THETA_TRAPPED, XNU_FACTOR, PARK and the SAT presets, WIDTH 0.4 | tglf_trapped_knobs |
| [tglf_gamma_ratio_vs_trapped_fraction_per_database](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_gamma_ratio_vs_trapped_fraction_per_database.ipynb) | Converged TGLF KBM $\gamma$ against THETA_TRAPPED, XNU_FACTOR, PARK and the SAT presets, WIDTH 0.4 | tglf_trapped_knobs |
| [tglf_within_tolerance_fraction_vs_knob_per_nbasis](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_within_tolerance_fraction_vs_knob_per_nbasis.ipynb) | Converged TGLF KBM $\gamma$ against THETA_TRAPPED, XNU_FACTOR, PARK and the SAT presets, WIDTH 0.4 | tglf_trapped_knobs |
| [tglf_trapped_fraction_sensitivity_vs_gamma_ratio](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_trapped_fraction_sensitivity_vs_gamma_ratio.ipynb) | Converged TGLF KBM $\gamma$ against THETA_TRAPPED, XNU_FACTOR, PARK and the SAT presets, WIDTH 0.4 | tglf_trapped_knobs |
| [tglf_gamma_ratio_and_omega_ratio_vs_theta_trapped_park](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_gamma_ratio_and_omega_ratio_vs_theta_trapped_park.ipynb) | Converged TGLF KBM $\gamma$ against THETA_TRAPPED, XNU_FACTOR, PARK and the SAT presets, WIDTH 0.4 | tglf_trapped_knobs |
| [tglf_gamma_and_omega_vs_gs2_per_ghat](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_gamma_and_omega_vs_gs2_per_ghat.ipynb) | TGLF GHAT (0.4–1) on the 738 KBMs: $\gamma$, $\omega$, extent ratios and fraction within 10/20 % of GS2, pooled and per database; the over-predicted $f_t$-insensitive modes; WIDTH 0.4 | tglf_ghat_database |
| [tglf_within_tolerance_fraction_and_gamma_ratio_vs_ghat_per_database](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_within_tolerance_fraction_and_gamma_ratio_vs_ghat_per_database.ipynb) | TGLF GHAT (0.4–1) on the 738 KBMs: $\gamma$, $\omega$, extent ratios and fraction within 10/20 % of GS2, pooled and per database; the over-predicted $f_t$-insensitive modes; WIDTH 0.4 | tglf_ghat_database |
| [phi_apar_extent_ratio_and_gamma_error_and_changed_mode_fraction_and_no_ion_mode_fraction_vs_width_per_filter](linear/KBM/tglf_gftm_resolution/kbm_database/phi_apar_extent_ratio_and_gamma_error_and_changed_mode_fraction_and_no_ion_mode_fraction_vs_width_per_filter.ipynb) | φ, A∥ extent ratio, γ error, changed-mode and no-ion-mode fractions vs WIDTH, per FILTER (TGLF, GFTM; KBM databases) | kbm_fixed_width_nbasis |
| [extent_error_and_gamma_error_and_omega_error_and_no_ion_mode_fraction_vs_width_per_nbasis](linear/KBM/tglf_gftm_resolution/kbm_database/extent_error_and_gamma_error_and_omega_error_and_no_ion_mode_fraction_vs_width_per_nbasis.ipynb) | Extent, γ, ω errors and no-ion-mode fraction vs WIDTH, per NBASIS (TGLF, GFTM; KBM databases); GFTM NBASIS 32 NXGRID table | kbm_fixed_width_nbasis |
| [extent_error_and_gamma_error_and_omega_error_and_no_ion_mode_fraction_and_run_time_vs_nbasis](linear/KBM/tglf_gftm_resolution/kbm_database/extent_error_and_gamma_error_and_omega_error_and_no_ion_mode_fraction_and_run_time_vs_nbasis.ipynb) | Extent, γ, ω errors, no-ion-mode fraction and run time vs NBASIS, per WIDTH (TGLF, GFTM; KBM databases) | kbm_fixed_width_nbasis |
| [tglf_gftm_within_tolerance_fraction_vs_width_per_nbasis](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_gftm_within_tolerance_fraction_vs_width_per_nbasis.ipynb) | Fraction of KBMs with extents within x of GS2, and gamma within x of the top NBASIS, vs WIDTH per NBASIS (TGLF, GFTM) | basis_resolution_rule |
| [gftm_within_tolerance_fraction_vs_nbasis_per_width](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_within_tolerance_fraction_vs_nbasis_per_width.ipynb) | Fraction of KBMs with extents within x of GS2, and gamma within x of the top NBASIS, vs WIDTH per NBASIS (TGLF, GFTM) | basis_resolution_rule |
| [gs2_nbasis_needed_vs_width_ratio_and_vs_width_per_tolerance](linear/KBM/tglf_gftm_resolution/kbm_database/gs2_nbasis_needed_vs_width_ratio_and_vs_width_per_tolerance.ipynb) | GS2 KBM fields projected onto the TGLF/GFTM Hermite basis: NBASIS needed against WIDTH, the fixed-width rule, and its check against the codes | basis_resolution_rule |
| [gs2_gaussian_sigma_vs_extent_per_database](linear/KBM/tglf_gftm_resolution/kbm_database/gs2_gaussian_sigma_vs_extent_per_database.ipynb) | GS2 KBM fields projected onto the TGLF/GFTM Hermite basis: NBASIS needed against WIDTH, the fixed-width rule, and its check against the codes | basis_resolution_rule |
| [gs2_projection_error_vs_width_per_nbasis](linear/KBM/tglf_gftm_resolution/kbm_database/gs2_projection_error_vs_width_per_nbasis.ipynb) | GS2 KBM fields projected onto the TGLF/GFTM Hermite basis: NBASIS needed against WIDTH, the fixed-width rule, and its check against the codes | basis_resolution_rule |
| [tglf_gftm_within_tolerance_fraction_vs_width_per_nbasis_projected](linear/KBM/tglf_gftm_resolution/kbm_database/tglf_gftm_within_tolerance_fraction_vs_width_per_nbasis_projected.ipynb) | GS2 KBM fields projected onto the TGLF/GFTM Hermite basis: NBASIS needed against WIDTH, the fixed-width rule, and its check against the codes | basis_resolution_rule |

## linear/KBM/extent/definition_single_kbm

**Argument step: pyro's extent**, its definition and one KBM.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [gs2_phi_95pct_extent_vs_theta](linear/KBM/extent/definition_single_kbm/gs2_phi_95pct_extent_vs_theta.ipynb) | How pyrokinetics measures a mode's extent (talk extent-definition slide) | talk_20261102 |
| [tglf_gftm_phi_extent_and_apar_extent_vs_width_per_nbasis](linear/KBM/extent/definition_single_kbm/tglf_gftm_phi_extent_and_apar_extent_vs_width_per_nbasis.ipynb) | One KBM, 95% extent of $\phi$ and $A_\parallel$ vs WIDTH (talk slide 18b; v2 section, qp5.41: TGLF SAT2, NXGRID >= NBASIS+8) | talk_20261102, spr045_single_kbm |

## linear/KBM/extent/kbm_database

**Argument step: pyro's extent** over the KBM databases.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [tglf_gftm_extent_ratio_vs_width_per_nbasis](linear/KBM/extent/kbm_database/tglf_gftm_extent_ratio_vs_width_per_nbasis.ipynb) | Median extent ratio code/GS2 vs WIDTH (talk slide 19) | talk_20261102 |
| [tglf_gftm_extent_error_vs_width_per_field](linear/KBM/extent/kbm_database/tglf_gftm_extent_error_vs_width_per_field.ipynb) | Extent ratio per field vs WIDTH (talk slide 24) | talk_20261102 |
| [tglf_extent_error_vs_width_per_field_nbasis](linear/KBM/extent/kbm_database/tglf_extent_error_vs_width_per_field_nbasis.ipynb) | TGLF extent vs WIDTH per NBASIS, three FILTERs | tglf_quadrature_extent |
| [gs2_projected_extent_ratio_vs_nbasis_and_vs_nxgrid_per_width](linear/KBM/extent/kbm_database/gs2_projected_extent_ratio_vs_nbasis_and_vs_nxgrid_per_width.ipynb) | GFTM extent and omega vs WIDTH: node density or NBASIS | gftm_quadrature_extent |
| [gftm_extent_error_and_gamma_error_vs_nxgrid_per_width](linear/KBM/extent/kbm_database/gftm_extent_error_and_gamma_error_vs_nxgrid_per_width.ipynb) | GFTM extent and omega vs WIDTH: node density or NBASIS | gftm_quadrature_extent |
| [gftm_phi_extent_error_vs_basis_scale_and_vs_node_spacing_per_width](linear/KBM/extent/kbm_database/gftm_phi_extent_error_vs_basis_scale_and_vs_node_spacing_per_width.ipynb) | GFTM extent and omega vs WIDTH: node density or NBASIS | gftm_quadrature_extent |
| [gftm_gamma_error_and_omega_error_and_extent_error_vs_width_per_nbasis](linear/KBM/extent/kbm_database/gftm_gamma_error_and_omega_error_and_extent_error_vs_width_per_nbasis.ipynb) | GFTM extent and omega vs WIDTH: node density or NBASIS | gftm_quadrature_extent |
| [gftm_bpar_sigma_extent_error_vs_width_per_field](linear/KBM/extent/kbm_database/gftm_bpar_sigma_extent_error_vs_width_per_field.ipynb) | GFTM $B_\parallel$ extent at large WIDTH | gftm_bpar_extent |
| [gs2_projected_bpar_extent_error_vs_width_per_nbasis](linear/KBM/extent/kbm_database/gs2_projected_bpar_extent_error_vs_width_per_nbasis.ipynb) | GFTM $B_\parallel$ extent at large WIDTH | gftm_bpar_extent |
| [gftm_gs2_field_eigenfunction_and_kperp_vs_theta_per_code](linear/KBM/extent/kbm_database/gftm_gs2_field_eigenfunction_and_kperp_vs_theta_per_code.ipynb) | GFTM $B_\parallel$ extent at large WIDTH | gftm_bpar_extent |
| [gs2_extent_vs_each_parameter_per_database](linear/KBM/extent/kbm_database/gs2_extent_vs_each_parameter_per_database.ipynb) | Extent against the kbm_free hypercube's physics parameters | kbm_extent_parameters |
| [gs2_extent_residual_vs_each_parameter_per_database](linear/KBM/extent/kbm_database/gs2_extent_residual_vs_each_parameter_per_database.ipynb) | Extent against the kbm_free hypercube's physics parameters | kbm_extent_parameters |
| [gs2_extent_vs_power_law_extent_per_database](linear/KBM/extent/kbm_database/gs2_extent_vs_power_law_extent_per_database.ipynb) | Extent against the kbm_free hypercube's physics parameters | kbm_extent_parameters |
| [gftm_gamma_error_and_omega_error_and_extent_error_vs_width](linear/KBM/extent/kbm_database/gftm_gamma_error_and_omega_error_and_extent_error_vs_width.ipynb) | Which extent the oracle width selects, and what predicts the width | kbm_width_oracle_physics |
| [gftm_extent_ratio_and_best_width_histograms](linear/KBM/extent/kbm_database/gftm_extent_ratio_and_best_width_histograms.ipynb) | Which extent the oracle width selects, and what predicts the width | kbm_width_oracle_physics |
| [gftm_best_width_vs_each_parameter_per_database](linear/KBM/extent/kbm_database/gftm_best_width_vs_each_parameter_per_database.ipynb) | Which extent the oracle width selects, and what predicts the width | kbm_width_oracle_physics |
| [gftm_best_width_gain_vs_beta_per_database](linear/KBM/extent/kbm_database/gftm_best_width_gain_vs_beta_per_database.ipynb) | Which extent the oracle width selects, and what predicts the width | kbm_width_oracle_physics |
| [gftm_within_tolerance_fraction_vs_tolerance_per_width_choice](linear/KBM/extent/kbm_database/gftm_within_tolerance_fraction_vs_tolerance_per_width_choice.ipynb) | Which extent the oracle width selects, and what predicts the width | kbm_width_oracle_physics |
| [gftm_gamma_error_vs_extent_cutoff_per_width](linear/KBM/extent/kbm_database/gftm_gamma_error_vs_extent_cutoff_per_width.ipynb) | Does an extent cut fix GFTM mode selection | kbm_extent_filter |
| [gftm_gamma_error_and_omega_error_vs_extent_cutoff_width](linear/KBM/extent/kbm_database/gftm_gamma_error_and_omega_error_vs_extent_cutoff_width.ipynb) | Does an extent cut fix GFTM mode selection | kbm_extent_filter |
| [gftm_dominant_mode_extent_vs_best_mode_extent_per_width](linear/KBM/extent/kbm_database/gftm_dominant_mode_extent_vs_best_mode_extent_per_width.ipynb) | Does an extent cut fix GFTM mode selection | kbm_extent_filter |
| [gftm_gs2_phi_eigenfunction_vs_theta_per_mode](linear/KBM/extent/kbm_database/gftm_gs2_phi_eigenfunction_vs_theta_per_mode.ipynb) | Does an extent cut fix GFTM mode selection | kbm_extent_filter |
| [gftm_gamma_error_and_omega_error_vs_width_per_mode_filter](linear/KBM/extent/kbm_database/gftm_gamma_error_and_omega_error_vs_width_per_mode_filter.ipynb) | Does an extent cut fix GFTM mode selection | kbm_extent_filter |
| [gftm_extent_vs_gs2_extent_per_width](linear/KBM/extent/kbm_database/gftm_extent_vs_gs2_extent_per_width.ipynb) | Does an extent cut fix GFTM mode selection | kbm_extent_filter |
| [gftm_extent_ratio_vs_width_per_mode_filter](linear/KBM/extent/kbm_database/gftm_extent_ratio_vs_width_per_mode_filter.ipynb) | Does an extent cut fix GFTM mode selection | kbm_extent_filter |
| [gs2_extended_field_eigenfunctions_vs_theta_per_case](linear/KBM/extent/kbm_database/gs2_extended_field_eigenfunctions_vs_theta_per_case.ipynb) | Does an extent cut fix GFTM mode selection | kbm_extent_filter |
| [gs2_tearing_parameter_vs_phi_extent_per_mode_label](linear/KBM/extent/kbm_database/gs2_tearing_parameter_vs_phi_extent_per_mode_label.ipynb) | Does an extent cut fix GFTM mode selection | kbm_extent_filter |

## linear/KBM/database

The KBM population and $\gamma$ parity against GS2.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [tglf_gftm_gamma_vs_gs2_gamma_per_settings](linear/KBM/database/tglf_gftm_gamma_vs_gs2_gamma_per_settings.ipynb) | Growth-rate parity, FILTER=0.5 GFTM arms vs GS2 | kbm_hypercube_gamma_parity_f05 |
| [gftm_gamma_vs_tglf_gamma_per_settings](linear/KBM/database/gftm_gamma_vs_tglf_gamma_per_settings.ipynb) | Growth-rate parity, FILTER=0.5 GFTM arms vs GS2 | kbm_hypercube_gamma_parity_f05 |
| [tglf_gftm_gamma_vs_gs2_gamma_per_settings_filter0](linear/KBM/database/tglf_gftm_gamma_vs_gs2_gamma_per_settings_filter0.ipynb) | The original FILTER=0 five arms, with the user's manual edits (mode 0, per-case scatter) | kbm_hypercube_gamma_parity |
| [gs2_converged_kbm_count_per_database](linear/KBM/database/gs2_converged_kbm_count_per_database.ipynb) | Converged GS2 KBMs per case in the kbm_free cubes (the paper's 738) | kbm_gs2_population |

## linear/MTM/mode_structure

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [gftm_mtm_gamma_error_spearman_per_descriptor](linear/MTM/mode_structure/gftm_mtm_gamma_error_spearman_per_descriptor.ipynb) | Gamma error vs extent and core fraction | mtm_core_tail |
| [gftm_mtm_gamma_error_and_capture_vs_each_descriptor_per_settings](linear/MTM/mode_structure/gftm_mtm_gamma_error_and_capture_vs_each_descriptor_per_settings.ipynb) | Gamma error vs extent and core fraction | mtm_core_tail |
| [gs2_mtm_extent_ratio_histogram_and_apar_vs_theta_and_kpar_spectrum](linear/MTM/mode_structure/gs2_mtm_extent_ratio_histogram_and_apar_vs_theta_and_kpar_spectrum.ipynb) | Gamma error vs extent and core fraction | mtm_core_tail |
| [gftm_mtm_gamma_error_spearman_per_descriptor_mtm_only](linear/MTM/mode_structure/gftm_mtm_gamma_error_spearman_per_descriptor_mtm_only.ipynb) | The same, MTM-only population | mtm_only_rescore |
| [gftm_mtm_gamma_error_and_capture_vs_each_descriptor_per_settings_mtm_only](linear/MTM/mode_structure/gftm_mtm_gamma_error_and_capture_vs_each_descriptor_per_settings_mtm_only.ipynb) | The same, MTM-only population | mtm_only_rescore |
| [gs2_mtm_extent_ratio_histogram_and_apar_vs_theta_and_kpar_spectrum_mtm_only](linear/MTM/mode_structure/gs2_mtm_extent_ratio_histogram_and_apar_vs_theta_and_kpar_spectrum_mtm_only.ipynb) | The same, MTM-only population | mtm_only_rescore |
| [gftm_gs2_apar_amplitude_and_phase_vs_theta_per_settings_mtm_only](linear/MTM/mode_structure/gftm_gs2_apar_amplitude_and_phase_vs_theta_per_settings_mtm_only.ipynb) | $A_\parallel$ phase winding, MTM-only population | mtm_only_rescore |
| [gftm_tearing_parameter_and_gamma_ratio_and_phase_winding_vs_nbasis_per_width_mtm_only](linear/MTM/mode_structure/gftm_tearing_parameter_and_gamma_ratio_and_phase_winding_vs_nbasis_per_width_mtm_only.ipynb) | $A_\parallel$ phase winding, MTM-only population | mtm_only_rescore |
| [gs2_gftm_phi_eigenfunction_vs_theta_per_code](linear/MTM/mode_structure/gs2_gftm_phi_eigenfunction_vs_theta_per_code.ipynb) | GS2 vs GFTM eigenfunction of one MTM deck (user's notebook) | - |

## linear/MTM/extent_law

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [gs2_mtm_extent_vs_fitted_extent_per_law](linear/MTM/extent_law/gs2_mtm_extent_vs_fitted_extent_per_law.ipynb) | $\theta_{95}(k_y,\hat s,q)$ law refit on NSTX | mtm_extent_law_refit |
| [gs2_mtm_extent_residual_vs_q](linear/MTM/extent_law/gs2_mtm_extent_residual_vs_q.ipynb) | $\theta_{95}(k_y,\hat s,q)$ law refit on NSTX | mtm_extent_law_refit |
| [gs2_mtm_extent_and_residual_vs_each_parameter_per_database](linear/MTM/extent_law/gs2_mtm_extent_and_residual_vs_each_parameter_per_database.ipynb) | Extent vs every parameter | mtm_extent_parameters |
| [gs2_mtm_extent_regression_coefficient_table](linear/MTM/extent_law/gs2_mtm_extent_regression_coefficient_table.ipynb) | Extent vs every parameter | mtm_extent_parameters |
| [gs2_mtm_extent_vs_fitted_extent_colour_q](linear/MTM/extent_law/gs2_mtm_extent_vs_fitted_extent_colour_q.ipynb) | Extent vs every parameter | mtm_extent_parameters |
| [gs2_mtm_extent_and_residual_vs_each_parameter_per_database_mtm_only](linear/MTM/extent_law/gs2_mtm_extent_and_residual_vs_each_parameter_per_database_mtm_only.ipynb) | The same, MTM-only population | mtm_only_rescore |
| [gs2_mtm_extent_regression_coefficient_table_mtm_only](linear/MTM/extent_law/gs2_mtm_extent_regression_coefficient_table_mtm_only.ipynb) | The same, MTM-only population | mtm_only_rescore |
| [gs2_mtm_extent_vs_fitted_extent_colour_q_mtm_only](linear/MTM/extent_law/gs2_mtm_extent_vs_fitted_extent_colour_q_mtm_only.ipynb) | The same, MTM-only population | mtm_only_rescore |
| [gs2_mtm_phi_apar_power_vs_basis_angle](linear/MTM/extent_law/gs2_mtm_phi_apar_power_vs_basis_angle.ipynb) | GS2 $\phi$ and $A_\parallel$ equivalent Gaussian widths in $\theta_b$, width laws, basis projection, settings | mtm_field_widths |
| [gs2_mtm_width_and_nbasis_needed_histograms](linear/MTM/extent_law/gs2_mtm_width_and_nbasis_needed_histograms.ipynb) | GS2 $\phi$ and $A_\parallel$ equivalent Gaussian widths in $\theta_b$, width laws, basis projection, settings | mtm_field_widths |
| [gs2_mtm_apar_width_vs_phi_width_and_vs_fitted_width](linear/MTM/extent_law/gs2_mtm_apar_width_vs_phi_width_and_vs_fitted_width.ipynb) | GS2 $\phi$ and $A_\parallel$ equivalent Gaussian widths in $\theta_b$, width laws, basis projection, settings | mtm_field_widths |
| [gs2_mtm_projection_error_vs_width_per_field](linear/MTM/extent_law/gs2_mtm_projection_error_vs_width_per_field.ipynb) | GS2 $\phi$ and $A_\parallel$ equivalent Gaussian widths in $\theta_b$, width laws, basis projection, settings | mtm_field_widths |
| [gftm_mtm_error_and_capture_vs_width_ratio_per_settings](linear/MTM/extent_law/gftm_mtm_error_and_capture_vs_width_ratio_per_settings.ipynb) | GS2 $\phi$ and $A_\parallel$ equivalent Gaussian widths in $\theta_b$, width laws, basis projection, settings | mtm_field_widths |
| [gftm_extent_over_width_vs_width_and_analytic_width_vs_calibrated_width](linear/MTM/extent_law/gftm_extent_over_width_vs_width_and_analytic_width_vs_calibrated_width.ipynb) | GS2 $\phi$ and $A_\parallel$ equivalent Gaussian widths in $\theta_b$, width laws, basis projection, settings | mtm_field_widths |
| [gs2_mtm_phi_and_apar_eigenfunction_vs_theta_per_output_file](linear/MTM/extent_law/gs2_mtm_phi_and_apar_eigenfunction_vs_theta_per_output_file.ipynb) | Are the $A_\parallel$ spike trains real? run final-time field vs cube, spike count vs $k_y\hat s$ | mtm_field_widths |
| [gs2_mtm_apar_spike_count_vs_ky_shat_and_vs_ky](linear/MTM/extent_law/gs2_mtm_apar_spike_count_vs_ky_shat_and_vs_ky.ipynb) | Are the $A_\parallel$ spike trains real? run final-time field vs cube, spike count vs $k_y\hat s$ | mtm_field_widths |

## linear/MTM/settings

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [gftm_mtm_gamma_vs_gs2_gamma_per_settings](linear/MTM/settings/gftm_mtm_gamma_vs_gs2_gamma_per_settings.ipynb) | Default vs m11 settings | nstx_mtm_lhc_default_vs_m11 |
| [gftm_mtm_gamma_error_vs_nxgrid_floor_and_extent_margin](linear/MTM/settings/gftm_mtm_gamma_error_vs_nxgrid_floor_and_extent_margin.ipynb) | Recipe grid scored, frozen settings recommendation | mtm_settings_recommendation |
| [gftm_mtm_gamma_error_vs_extent_per_settings](linear/MTM/settings/gftm_mtm_gamma_error_vs_extent_per_settings.ipynb) | Recipe grid scored, frozen settings recommendation | mtm_settings_recommendation |
| [gftm_mtm_gamma_error_vs_mean_nbasis_per_settings](linear/MTM/settings/gftm_mtm_gamma_error_vs_mean_nbasis_per_settings.ipynb) | Recipe grid scored, frozen settings recommendation | mtm_settings_recommendation |
| [gftm_mtm_gamma_error_and_capture_per_settings_n300](linear/MTM/settings/gftm_mtm_gamma_error_and_capture_per_settings_n300.ipynb) | Max-basis arm B on NSTX_MTM n300 | mtm_maxbasis_n300 |
| [gftm_first_node_angle_vs_reach_per_settings](linear/MTM/settings/gftm_first_node_angle_vs_reach_per_settings.ipynb) | Max fixed basis with per-case WIDTH | mtm_maxbasis |
| [gftm_mtm_gamma_error_and_capture_per_settings_max_nbasis](linear/MTM/settings/gftm_mtm_gamma_error_and_capture_per_settings_max_nbasis.ipynb) | Max fixed basis with per-case WIDTH | mtm_maxbasis |
| [gftm_mtm_gamma_error_and_capture_vs_nbasis](linear/MTM/settings/gftm_mtm_gamma_error_and_capture_vs_nbasis.ipynb) | NBASIS ladder at fixed NXGRID and per-case WIDTH | mtm_maxbasis |
| [gftm_mtm_gamma_error_and_capture_per_settings_all_arms](linear/MTM/settings/gftm_mtm_gamma_error_and_capture_per_settings_all_arms.ipynb) | All MTM settings re-scored on the MTM-only population | mtm_only_rescore |
| [gftm_mtm_gamma_error_per_settings_dropped_extent_quartile](linear/MTM/settings/gftm_mtm_gamma_error_per_settings_dropped_extent_quartile.ipynb) | All MTM settings re-scored on the MTM-only population | mtm_only_rescore |
| [gftm_mtm_gamma_error_and_capture_per_settings_extent_fit](linear/MTM/settings/gftm_mtm_gamma_error_and_capture_per_settings_extent_fit.ipynb) | Extent-rule arm with the new law | mtm_extent_rule_law2 |
| [gftm_mtm_gamma_vs_gs2_gamma_per_settings_extent_fit](linear/MTM/settings/gftm_mtm_gamma_vs_gs2_gamma_per_settings_extent_fit.ipynb) | Extent-rule arm with the new law | mtm_extent_rule_law2 |

## linear/general/diagnostics

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [gftm_gs2_apar_amplitude_and_phase_vs_theta_per_settings](linear/general/diagnostics/gftm_gs2_apar_amplitude_and_phase_vs_theta_per_settings.ipynb) | $A_\parallel$ phase winding: physics or Hermite-basis artefact | gftm_phase_winding |
| [gftm_tearing_parameter_and_gamma_ratio_and_phase_winding_vs_nbasis_per_width](linear/general/diagnostics/gftm_tearing_parameter_and_gamma_ratio_and_phase_winding_vs_nbasis_per_width.ipynb) | $A_\parallel$ phase winding: physics or Hermite-basis artefact | gftm_phase_winding |
| [gftm_gamma_ratio_vs_bpar_phi_ratio_per_width](linear/general/diagnostics/gftm_gamma_ratio_vs_bpar_phi_ratio_per_width.ipynb) | Do large-$B_\parallel$ cases have bad growth rates | gftm_bpar_ratio |
| [gftm_over_gs2_bpar_phi_ratio_vs_ky_per_width](linear/general/diagnostics/gftm_over_gs2_bpar_phi_ratio_vs_ky_per_width.ipynb) | Do large-$B_\parallel$ cases have bad growth rates | gftm_bpar_ratio |
| [gftm_changed_mode_fraction_and_gamma_error_and_phi_beyond_pi_fraction_vs_width_per_nbasis](linear/general/diagnostics/gftm_changed_mode_fraction_and_gamma_error_and_phi_beyond_pi_fraction_vs_width_per_nbasis.ipynb) | What causes the high-WIDTH gamma error | gftm_highwidth_cause |
| [tglf_gftm_gamma_error_vs_width_per_code](linear/general/diagnostics/tglf_gftm_gamma_error_vs_width_per_code.ipynb) | What causes the high-WIDTH gamma error | gftm_highwidth_cause |
| [gftm_gamma_error_vs_width_per_nbasis_r4](linear/general/diagnostics/gftm_gamma_error_vs_width_per_nbasis_r4.ipynb) | What GFTM gets wrong on R4, and where else | gftm_r4_diagnosis |
| [gs2_gftm_gamma_and_omega_vs_beta_per_settings_r4](linear/general/diagnostics/gs2_gftm_gamma_and_omega_vs_beta_per_settings_r4.ipynb) | What GFTM gets wrong on R4, and where else | gftm_r4_diagnosis |
| [gftm_all_modes_gamma_and_omega_vs_beta_per_mode_type_r4](linear/general/diagnostics/gftm_all_modes_gamma_and_omega_vs_beta_per_mode_type_r4.ipynb) | What GFTM gets wrong on R4, and where else | gftm_r4_diagnosis |
| [gftm_best_overlap_mode_gamma_and_overlap_vs_beta_r4](linear/general/diagnostics/gftm_best_overlap_mode_gamma_and_overlap_vs_beta_r4.ipynb) | What GFTM gets wrong on R4, and where else | gftm_r4_diagnosis |
| [gftm_gamma_error_per_mode_choice_r4](linear/general/diagnostics/gftm_gamma_error_per_mode_choice_r4.ipynb) | What GFTM gets wrong on R4, and where else | gftm_r4_diagnosis |
| [gftm_high_error_case_parameter_percentile_per_parameter](linear/general/diagnostics/gftm_high_error_case_parameter_percentile_per_parameter.ipynb) | What GFTM gets wrong on R4, and where else | gftm_r4_diagnosis |
| [gftm_gamma_minus_gs2_gamma_vs_alpha_per_database](linear/general/diagnostics/gftm_gamma_minus_gs2_gamma_vs_alpha_per_database.ipynb) | What GFTM gets wrong on R4, and where else | gftm_r4_diagnosis |
| [gs2_time_tolerance_histogram_per_database](linear/general/diagnostics/gs2_time_tolerance_histogram_per_database.ipynb) | R4 GS2 time-resolved convergence | r4_gs2_convergence |
| [gs2_time_tolerance_vs_ky_and_vs_beta](linear/general/diagnostics/gs2_time_tolerance_vs_ky_and_vs_beta.ipynb) | R4 GS2 time-resolved convergence | r4_gs2_convergence |
| [gs2_gamma_and_omega_vs_time_per_run](linear/general/diagnostics/gs2_gamma_and_omega_vs_time_per_run.ipynb) | R4 GS2 time-resolved convergence | r4_gs2_convergence |
| [gftm_over_gs2_bpar_ratio_vs_ky_per_database](linear/general/diagnostics/gftm_over_gs2_bpar_ratio_vs_ky_per_database.ipynb) | GFTM $B_\parallel/A_\parallel$ vs GS2 before and after pyro PR #613 | pyro_bpar_normalisation |
| [gs2_mode_indicator_histograms_and_pairwise_scatter_per_database](linear/general/diagnostics/gs2_mode_indicator_histograms_and_pairwise_scatter_per_database.ipynb) | Mode classifier calibration on the GS2 databases | mode_classification |
| [gs2_chi_e_over_chi_i_per_mode_label](linear/general/diagnostics/gs2_chi_e_over_chi_i_per_mode_label.ipynb) | Mode classifier calibration on the GS2 databases | mode_classification |
| [gs2_apar_and_phi_eigenfunction_vs_theta_per_mode_label](linear/general/diagnostics/gs2_apar_and_phi_eigenfunction_vs_theta_per_mode_label.ipynb) | Mode classifier calibration on the GS2 databases | mode_classification |
| [gftm_gamma_vs_ky](linear/general/diagnostics/gftm_gamma_vs_ky.ipynb) | GyroRun end-to-end GFTM scan and cube smoke test | gyrorun_gftm_smoke |
| [gftm_gamma_vs_ky_shat](linear/general/diagnostics/gftm_gamma_vs_ky_shat.ipynb) | GyroRun end-to-end GFTM scan and cube smoke test | gyrorun_gftm_smoke |

## linear/general/plotting

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [tglf_gftm_gs2_gamma_and_omega_vs_q_shat_beta_and_gamma_difference_vs_ky_parameter](linear/general/plotting/tglf_gftm_gs2_gamma_and_omega_vs_q_shat_beta_and_gamma_difference_vs_ky_parameter.ipynb) | User's linear plotting (machine-specific data path) | - |
| [tglf_gftm_gs2_gamma_and_omega_vs_beta_and_vs_ky_and_phi_and_apar_eigenfunction_vs_theta](linear/general/plotting/tglf_gftm_gs2_gamma_and_omega_vs_beta_and_vs_ky_and_phi_and_apar_eigenfunction_vs_theta.ipynb) | User's beta-scan plotting (machine-specific data path) | - |
| [phi_apar_eigenfunction_vs_theta_per_mode_type](linear/general/plotting/phi_apar_eigenfunction_vs_theta_per_mode_type.ipynb) | User's KBM and MTM eigenfunction plots | - |
| [gs2_gftm_cgyro_phi_and_apar_eigenfunction_vs_theta_per_code](linear/general/plotting/gs2_gftm_cgyro_phi_and_apar_eigenfunction_vs_theta_per_code.ipynb) | User's comparison of specific GFTM iterations (machine-specific data path) | - |
| [gftm_cgyro_gs2_phi_eigenfunction_vs_theta_per_settings](linear/general/plotting/gftm_cgyro_gs2_phi_eigenfunction_vs_theta_per_settings.ipynb) | User's Gary settings comparison (machine-specific data path) | - |
| [gftm_gamma_vs_gs2_gamma_per_settings_m3_to_m9](linear/general/plotting/gftm_gamma_vs_gs2_gamma_per_settings_m3_to_m9.ipynb) | User's m3-m9 comparisons (machine-specific data path) | - |
| [gftm_cgyro_phi_eigenfunction_vs_theta_per_width_nxgrid_and_gauss_hermite_node_theta_vs_nxgrid](linear/general/plotting/gftm_cgyro_phi_eigenfunction_vs_theta_per_width_nxgrid_and_gauss_hermite_node_theta_vs_nxgrid.ipynb) | WIDTH and NXGRID plots. **Does not open:** master holds unresolved merge markers | width_nxgrid_improved |
| [tglf_gftm_gs2_gamma_and_omega_vs_beta_per_mode](linear/general/plotting/tglf_gftm_gs2_gamma_and_omega_vs_beta_per_mode.ipynb) | $\beta$ stabilisation and mode type, GFTM and TGLF vs GS2 | beta_stabilisation_f05 |
| [tglf_gftm_gs2_field_eigenfunction_and_phase_vs_theta_per_code_r4](linear/general/plotting/tglf_gftm_gs2_field_eigenfunction_and_phase_vs_theta_per_code_r4.ipynb) | $\beta$ stabilisation and mode type, GFTM and TGLF vs GS2 | beta_stabilisation_f05 |
| [gftm_gs2_extent_and_extent_ratio_and_apar_amplitude_vs_beta_per_width_r4](linear/general/plotting/gftm_gs2_extent_and_extent_ratio_and_apar_amplitude_vs_beta_per_width_r4.ipynb) | $\beta$ stabilisation and mode type, GFTM and TGLF vs GS2 | beta_stabilisation_f05 |
| [gs2_gamma_vs_time_per_cell_r4](linear/general/plotting/gs2_gamma_vs_time_per_cell_r4.ipynb) | $\beta$ stabilisation and mode type, GFTM and TGLF vs GS2 | beta_stabilisation_f05 |
| [gftm_gamma_and_extent_ratio_vs_width_per_ky_r4](linear/general/plotting/gftm_gamma_and_extent_ratio_vs_width_per_ky_r4.ipynb) | $\beta$ stabilisation and mode type, GFTM and TGLF vs GS2 | beta_stabilisation_f05 |
| [ideal_ballooning_gamma_vs_alpha_per_beta_r4](linear/general/plotting/ideal_ballooning_gamma_vs_alpha_per_beta_r4.ipynb) | $\beta$ stabilisation and mode type, GFTM and TGLF vs GS2 | beta_stabilisation_f05 |
| [gftm_gamma_vs_nbasis_per_beta_r4](linear/general/plotting/gftm_gamma_vs_nbasis_per_beta_r4.ipynb) | $\beta$ stabilisation and mode type, GFTM and TGLF vs GS2 | beta_stabilisation_f05 |
| [gftm_over_gs2_bpar_amplitude_ratio_and_apar_amplitude_ratio_vs_ky_per_width_r4](linear/general/plotting/gftm_over_gs2_bpar_amplitude_ratio_and_apar_amplitude_ratio_vs_ky_per_width_r4.ipynb) | $\beta$ stabilisation and mode type, GFTM and TGLF vs GS2 | beta_stabilisation_f05 |
| [tglf_gftm_gs2_gamma_and_omega_vs_q_and_vs_shat_per_settings_s1_3](linear/general/plotting/tglf_gftm_gs2_gamma_and_omega_vs_q_and_vs_shat_per_settings_s1_3.ipynb) | $\beta$ stabilisation and mode type, GFTM and TGLF vs GS2 | beta_stabilisation_f05 |

## nonlinear

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [tglf_gene_heat_flux_vs_exb_shear_and_gamma_vs_ky_and_heat_flux_vs_time](nonlinear/tglf_gene_heat_flux_vs_exb_shear_and_gamma_vs_ky_and_heat_flux_vs_time.ipynb) | User's nonlinear plotting (machine-specific data path) | - |

`_templates/` holds the starter notebook and `examples/` a worked example.
