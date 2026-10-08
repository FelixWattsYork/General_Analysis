# Analysis notebooks

New analysis notebooks are grouped by topic. Each writes figures to `Plots/<analysis_name>` and its Fusion_PhD results dir holds the published copy.

| notebook | shows | Fusion_PhD results |
|---|---|---|
| [GFTM_numerics/gftm_bpar_ratio_vs_gamma_error.ipynb](GFTM_numerics/gftm_bpar_ratio_vs_gamma_error.ipynb) | Do GFTM cases with large B_par have bad growth rates | results/gftm_bpar_ratio |
| [GFTM_numerics/gftm_high_width_gamma_error_cause.ipynb](GFTM_numerics/gftm_high_width_gamma_error_cause.ipynb) | What causes the high-WIDTH gamma error | results/gftm_highwidth_cause |
| [GFTM_numerics/gftm_apar_phase_winding.ipynb](GFTM_numerics/gftm_apar_phase_winding.ipynb) | A_par phase winding: physics or Hermite-basis artefact | results/gftm_phase_winding |
| [GFTM_numerics/gftm_apar_phase_winding_mtm_only.ipynb](GFTM_numerics/gftm_apar_phase_winding_mtm_only.ipynb) | Phase winding, MTM-only population | results/gftm_phase_winding_mtm_only (dir not found) |
| [GFTM_numerics/gftm_gauss_hermite_extent_and_omega_vs_width.ipynb](GFTM_numerics/gftm_gauss_hermite_extent_and_omega_vs_width.ipynb) | Gauss-Hermite extent and omega error vs WIDTH | results/gftm_quadrature_extent |
| [GFTM_numerics/gyrorun_gftm_end_to_end_smoke_test.ipynb](GFTM_numerics/gyrorun_gftm_end_to_end_smoke_test.ipynb) | GyroRun end-to-end GFTM scan+cube smoke test | results/gyrorun_gftm_smoke |
| [GS2_reference/r4_gs2_time_convergence.ipynb](GS2_reference/r4_gs2_time_convergence.ipynb) | R4 GS2 time-resolved convergence | results/r4_gs2_convergence |
| [KBM/kbm_gftm_extent_filter_mode_selection.ipynb](KBM/kbm_gftm_extent_filter_mode_selection.ipynb) | Does an extent cut fix GFTM KBM mode selection | results/kbm_extent_filter |
| [KBM/kbm_tglf_extent_filter_mode_selection.ipynb](KBM/kbm_tglf_extent_filter_mode_selection.ipynb) | Extent filter on top of TGLF's frequency filter | results/kbm_extent_filter_tglf |
| [KBM/kbm_gftm_accuracy_vs_filter_and_width.ipynb](KBM/kbm_gftm_accuracy_vs_filter_and_width.ipynb) | GFTM KBM accuracy vs FILTER and WIDTH | results/kbm_filter_width |
| [KBM/kbm_width_oracle_extent_physics.ipynb](KBM/kbm_width_oracle_extent_physics.ipynb) | Which extent the oracle-chosen width selects | results/kbm_width_oracle_physics |
| [MTM/mtm_core_vs_tail_gamma_error.ipynb](MTM/mtm_core_vs_tail_gamma_error.ipynb) | MTM gamma error vs extent, core fraction | results/mtm_core_tail |
| [MTM/mtm_core_vs_tail_gamma_error_mtm_only.ipynb](MTM/mtm_core_vs_tail_gamma_error_mtm_only.ipynb) | Core/tail, MTM-only population | results/mtm_core_tail_mtm_only (dir not found) |
| [MTM/mtm_extent_law_refit_nstx.ipynb](MTM/mtm_extent_law_refit_nstx.ipynb) | theta95(ky,shat,q) law refit on NSTX | results/mtm_extent_law_refit |
| [MTM/mtm_extent_vs_all_parameters.ipynb](MTM/mtm_extent_vs_all_parameters.ipynb) | MTM extent vs every parameter | results/mtm_extent_parameters |
| [MTM/mtm_extent_vs_all_parameters_mtm_only.ipynb](MTM/mtm_extent_vs_all_parameters_mtm_only.ipynb) | Extent vs parameters, MTM-only population | results/mtm_extent_parameters_mtm_only (dir not found) |
| [MTM/mtm_max_basis_per_case_width.ipynb](MTM/mtm_max_basis_per_case_width.ipynb) | Max fixed basis with per-case WIDTH | results/mtm_maxbasis |
| [MTM/mtm_max_basis_nstx_n300.ipynb](MTM/mtm_max_basis_nstx_n300.ipynb) | Max-basis arm B on NSTX_MTM n300 | results/mtm_maxbasis_n300 |
| [MTM/mtm_nbasis_ladder_fixed_width.ipynb](MTM/mtm_nbasis_ladder_fixed_width.ipynb) | NBASIS ladder at fixed NXGRID and per-case WIDTH | results/mtm_nbladder (dir not found) |
| [MTM/mtm_only_population_rescore.ipynb](MTM/mtm_only_population_rescore.ipynb) | All MTM settings re-scored on MTM-only population | results/mtm_only_rescore |
| [MTM/mtm_gftm_settings_recommendation.ipynb](MTM/mtm_gftm_settings_recommendation.ipynb) | Recipe grid scored; frozen MTM settings recommendation | results/mtm_settings_recommendation |
| [MTM/mtm_default_vs_m11_settings.ipynb](MTM/mtm_default_vs_m11_settings.ipynb) | MTM default vs m11 settings | results/mtm_default_vs_m11 (dir not found) |

Older notebooks (`FuseNet_Poster/`, `TGLF_GFTM_KBM_PAPER/`, the paper-figure notebooks, `examples/`, `_templates/`) are unchanged in place.
