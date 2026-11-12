# Analysis notebooks

**Layout rule.** Any nonlinear content goes in `nonlinear/`. Linear-only work goes in `linear/`, by database
(`KBM`, `MTM`, or `general` when tied to none), then by the point it supports. Work with no GK data goes in
`theory/`. Each folder holds at most about 10 notebooks; beyond that, make subfolders. Notebooks are atomic.

Every notebook finds the repository by searching upward for `pyproject.toml`, so depth does not matter. Each
notebook sets its own path under `Plots/`, independent of its folder. The results column is the directory under
`results/` in Fusion_PhD holding the published copy.


## theory

No GK data: Gaussian-Hermite fits and similar.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [hermite_projections_of_gaussian](theory/hermite_projections_of_gaussian.ipynb) | Hermite projections of a Gaussian: fit error against mismatch (talk slides 11-12) | talk_20261102 |

## linear/KBM/tglf_width_search

**Argument step: the width search is unreliable.** TGLF over-prediction, FIND_WIDTH, FILTER x NBASIS, SAT1/SAT2.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [tglf_default_search_vs_gs2_scatter](linear/KBM/tglf_width_search/tglf_default_search_vs_gs2_scatter.ipynb) | TGLF default width search against GS2, growth-rate scatter (talk slide 9) | talk_20261102 |
| [tglf_search_bias_vs_gs2](linear/KBM/tglf_width_search/tglf_search_bias_vs_gs2.ipynb) | Growth-rate bias of the search against GS2, with tables | tglf_search_bias |
| [tglf_find_width_selected_width_and_fixed_width](linear/KBM/tglf_width_search/tglf_find_width_selected_width_and_fixed_width.ipynb) | Selected width vs search basis, best fixed WIDTH and NBASIS | tglf_find_width |
| [tglf_filter_width](linear/KBM/tglf_width_search/tglf_filter_width.ipynb) | FILTER x NBASIS vs GS2 on the four kbm_free databases | tglf_filter_width |
| [tglf_sat1_sat2](linear/KBM/tglf_width_search/tglf_sat1_sat2.ipynb) | SAT1 (EM search) vs SAT2 (ES search) vs GS2 on kbm_free | tglf_sat1_sat2 |
| [kbm_tglf_extent_filter_mode_selection](linear/KBM/tglf_width_search/kbm_tglf_extent_filter_mode_selection.ipynb) | Extent filter on top of TGLF's frequency filter | kbm_extent_filter_tglf |

## linear/KBM/tglf_gftm_resolution/single_kbm

**Argument step: fixed width against NBASIS**, on one KBM.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [spr045_single_kbm_width_nbasis](linear/KBM/tglf_gftm_resolution/single_kbm/spr045_single_kbm_width_nbasis.ipynb) | One KBM (SPR-045 sample_0818) against WIDTH and NBASIS, GFTM and TGLF | spr045_single_kbm |
| [eigenfunction_resolution_width_nbasis](linear/KBM/tglf_gftm_resolution/single_kbm/eigenfunction_resolution_width_nbasis.ipynb) | How WIDTH and NBASIS resolve its eigenfunction, one figure per code (talk slide 16) | talk_20261102 |
| [single_kbm_gs2_eigenfunction](linear/KBM/tglf_gftm_resolution/single_kbm/single_kbm_gs2_eigenfunction.ipynb) | Its GS2 eigenfunction, real and imaginary parts (talk slide 17) | talk_20261102 |
| [single_kbm_gamma_ratio_vs_width](linear/KBM/tglf_gftm_resolution/single_kbm/single_kbm_gamma_ratio_vs_width.ipynb) | Its $\gamma_{code}/\gamma_{GS2}$ against WIDTH (talk slide 18) | talk_20261102 |

## linear/KBM/tglf_gftm_resolution/kbm_database

**Argument step: fixed width against NBASIS**, over the KBM databases.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [gftm_galerkin_field_width_selection](linear/KBM/tglf_gftm_resolution/kbm_database/gftm_galerkin_field_width_selection.ipynb) | Does the Galerkin field solve make low-NBASIS width selection reliable | gftm_galerkin_field |
| [kbm_width_collapse](linear/KBM/tglf_gftm_resolution/kbm_database/kbm_width_collapse.ipynb) | GFTM error against the Hermite-basis width mismatch $s$ | kbm_width_collapse |
| [kbm_width_ushape](linear/KBM/tglf_gftm_resolution/kbm_database/kbm_width_ushape.ipynb) | TGLF and GFTM error vs WIDTH per NBASIS | kbm_width_collapse |
| [kbm_width_ushape_tglf_f0](linear/KBM/tglf_gftm_resolution/kbm_database/kbm_width_ushape_tglf_f0.ipynb) | The same with TGLF at FILTER 0 | kbm_width_collapse |
| [kbm_gftm_accuracy_vs_filter_and_width](linear/KBM/tglf_gftm_resolution/kbm_database/kbm_gftm_accuracy_vs_filter_and_width.ipynb) | GFTM accuracy vs FILTER and WIDTH | kbm_filter_width |
| [fixed_width_nbasis_convergence](linear/KBM/tglf_gftm_resolution/kbm_database/fixed_width_nbasis_convergence.ipynb) | Fixed WIDTH x NBASIS convergence, TGLF and GFTM, with cost; NXGRID >= NBASIS + 8 | kbm_fixed_width_nbasis |

## linear/KBM/extent/definition_single_kbm

**Argument step: pyro's extent**, its definition and one KBM.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [extent_definition](linear/KBM/extent/definition_single_kbm/extent_definition.ipynb) | How pyrokinetics measures a mode's extent (talk extent-definition slide) | talk_20261102 |
| [single_kbm_extent_vs_width](linear/KBM/extent/definition_single_kbm/single_kbm_extent_vs_width.ipynb) | One KBM, 95% extent of $\phi$ and $A_\parallel$ vs WIDTH (talk slide 18b) | talk_20261102 |

## linear/KBM/extent/kbm_database

**Argument step: pyro's extent** over the KBM databases.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [database_extent_ratio_vs_width](linear/KBM/extent/kbm_database/database_extent_ratio_vs_width.ipynb) | Median extent ratio code/GS2 vs WIDTH (talk slide 19) | talk_20261102 |
| [database_extent_per_field_vs_width](linear/KBM/extent/kbm_database/database_extent_per_field_vs_width.ipynb) | Extent ratio per field vs WIDTH (talk slide 24) | talk_20261102 |
| [tglf_quadrature_extent](linear/KBM/extent/kbm_database/tglf_quadrature_extent.ipynb) | TGLF extent vs WIDTH per NBASIS, three FILTERs | tglf_quadrature_extent |
| [gftm_gauss_hermite_extent_and_omega_vs_width](linear/KBM/extent/kbm_database/gftm_gauss_hermite_extent_and_omega_vs_width.ipynb) | GFTM extent and omega vs WIDTH: node density or NBASIS | gftm_quadrature_extent |
| [gftm_bpar_extent](linear/KBM/extent/kbm_database/gftm_bpar_extent.ipynb) | GFTM $B_\parallel$ extent at large WIDTH | gftm_bpar_extent |
| [kbm_extent_vs_physics_parameters](linear/KBM/extent/kbm_database/kbm_extent_vs_physics_parameters.ipynb) | Extent against the kbm_free hypercube's physics parameters | kbm_extent_parameters |
| [kbm_width_oracle_extent_physics](linear/KBM/extent/kbm_database/kbm_width_oracle_extent_physics.ipynb) | Which extent the oracle width selects, and what predicts the width | kbm_width_oracle_physics |
| [kbm_gftm_extent_filter_mode_selection](linear/KBM/extent/kbm_database/kbm_gftm_extent_filter_mode_selection.ipynb) | Does an extent cut fix GFTM mode selection | kbm_extent_filter |

## linear/KBM/database

The KBM population and $\gamma$ parity against GS2.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [kbm_hypercube_gamma_parity](linear/KBM/database/kbm_hypercube_gamma_parity.ipynb) | Growth-rate parity, FILTER=0.5 GFTM arms vs GS2 | kbm_hypercube_gamma_parity_f05 |
| [kbm_hypercube_gamma_parity_five_arms_filter0](linear/KBM/database/kbm_hypercube_gamma_parity_five_arms_filter0.ipynb) | The original FILTER=0 five arms, with the user's manual edits (mode 0, per-case scatter) | kbm_hypercube_gamma_parity |

## linear/MTM/mode_structure

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [mtm_core_vs_tail_gamma_error](linear/MTM/mode_structure/mtm_core_vs_tail_gamma_error.ipynb) | Gamma error vs extent and core fraction | mtm_core_tail |
| [mtm_core_vs_tail_gamma_error_mtm_only](linear/MTM/mode_structure/mtm_core_vs_tail_gamma_error_mtm_only.ipynb) | The same, MTM-only population | mtm_only_rescore |
| [gftm_apar_phase_winding_mtm_only](linear/MTM/mode_structure/gftm_apar_phase_winding_mtm_only.ipynb) | $A_\parallel$ phase winding, MTM-only population | mtm_only_rescore |
| [gs2_v_gftm_eigenfunctions](linear/MTM/mode_structure/gs2_v_gftm_eigenfunctions.ipynb) | GS2 vs GFTM eigenfunction of one MTM deck (user's notebook) | - |

## linear/MTM/extent_law

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [mtm_extent_law_refit_nstx](linear/MTM/extent_law/mtm_extent_law_refit_nstx.ipynb) | $\theta_{95}(k_y,\hat s,q)$ law refit on NSTX | mtm_extent_law_refit |
| [mtm_extent_vs_all_parameters](linear/MTM/extent_law/mtm_extent_vs_all_parameters.ipynb) | Extent vs every parameter | mtm_extent_parameters |
| [mtm_extent_vs_all_parameters_mtm_only](linear/MTM/extent_law/mtm_extent_vs_all_parameters_mtm_only.ipynb) | The same, MTM-only population | mtm_only_rescore |

## linear/MTM/settings

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [mtm_default_vs_m11_settings](linear/MTM/settings/mtm_default_vs_m11_settings.ipynb) | Default vs m11 settings | nstx_mtm_lhc_default_vs_m11 |
| [mtm_gftm_settings_recommendation](linear/MTM/settings/mtm_gftm_settings_recommendation.ipynb) | Recipe grid scored, frozen settings recommendation | mtm_settings_recommendation |
| [mtm_max_basis_nstx_n300](linear/MTM/settings/mtm_max_basis_nstx_n300.ipynb) | Max-basis arm B on NSTX_MTM n300 | mtm_maxbasis_n300 |
| [mtm_max_basis_per_case_width](linear/MTM/settings/mtm_max_basis_per_case_width.ipynb) | Max fixed basis with per-case WIDTH | mtm_maxbasis |
| [mtm_nbasis_ladder_fixed_width](linear/MTM/settings/mtm_nbasis_ladder_fixed_width.ipynb) | NBASIS ladder at fixed NXGRID and per-case WIDTH | mtm_maxbasis |
| [mtm_only_population_rescore](linear/MTM/settings/mtm_only_population_rescore.ipynb) | All MTM settings re-scored on the MTM-only population | mtm_only_rescore |
| [mtm_extent_rule_law2](linear/MTM/settings/mtm_extent_rule_law2.ipynb) | Extent-rule arm with the new law | mtm_extent_rule_law2 |

## linear/general/diagnostics

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [gftm_apar_phase_winding](linear/general/diagnostics/gftm_apar_phase_winding.ipynb) | $A_\parallel$ phase winding: physics or Hermite-basis artefact | gftm_phase_winding |
| [gftm_bpar_ratio_vs_gamma_error](linear/general/diagnostics/gftm_bpar_ratio_vs_gamma_error.ipynb) | Do large-$B_\parallel$ cases have bad growth rates | gftm_bpar_ratio |
| [gftm_high_width_gamma_error_cause](linear/general/diagnostics/gftm_high_width_gamma_error_cause.ipynb) | What causes the high-WIDTH gamma error | gftm_highwidth_cause |
| [gftm_r4_diagnosis](linear/general/diagnostics/gftm_r4_diagnosis.ipynb) | What GFTM gets wrong on R4, and where else | gftm_r4_diagnosis |
| [r4_gs2_time_convergence](linear/general/diagnostics/r4_gs2_time_convergence.ipynb) | R4 GS2 time-resolved convergence | r4_gs2_convergence |
| [pyro_bpar_normalisation](linear/general/diagnostics/pyro_bpar_normalisation.ipynb) | GFTM $B_\parallel/A_\parallel$ vs GS2 before and after pyro PR #613 | pyro_bpar_normalisation |
| [mode_classification_calibration](linear/general/diagnostics/mode_classification_calibration.ipynb) | Mode classifier calibration on the GS2 databases | mode_classification |
| [gyrorun_gftm_end_to_end_smoke_test](linear/general/diagnostics/gyrorun_gftm_end_to_end_smoke_test.ipynb) | GyroRun end-to-end GFTM scan and cube smoke test | gyrorun_gftm_smoke |

## linear/general/plotting

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [Linear_Plotting](linear/general/plotting/Linear_Plotting.ipynb) | User's linear plotting (machine-specific data path) | - |
| [linear_plotting_beta](linear/general/plotting/linear_plotting_beta.ipynb) | User's beta-scan plotting (machine-specific data path) | - |
| [Plot_KBM_and_MTM_eigenfunctions](linear/general/plotting/Plot_KBM_and_MTM_eigenfunctions.ipynb) | User's KBM and MTM eigenfunction plots | - |
| [compare_specific_iterations](linear/general/plotting/compare_specific_iterations.ipynb) | User's comparison of specific GFTM iterations (machine-specific data path) | - |
| [gary_settings_comparison](linear/general/plotting/gary_settings_comparison.ipynb) | User's Gary settings comparison (machine-specific data path) | - |
| [m3_9_my_comparisons](linear/general/plotting/m3_9_my_comparisons.ipynb) | User's m3-m9 comparisons (machine-specific data path) | - |
| [width_and_nxgrid_plotting](linear/general/plotting/width_and_nxgrid_plotting.ipynb) | WIDTH and NXGRID plots. **Does not open:** master holds unresolved merge markers | width_nxgrid_improved |
| [beta_stabilisation_modes](linear/general/plotting/beta_stabilisation_modes.ipynb) | $\beta$ stabilisation and mode type, GFTM and TGLF vs GS2 | beta_stabilisation_f05 |

## nonlinear

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [Nonlinaer_Plotting](nonlinear/Nonlinaer_Plotting.ipynb) | User's nonlinear plotting (machine-specific data path) | - |

`_templates/` holds the starter notebook and `examples/` a worked example.
