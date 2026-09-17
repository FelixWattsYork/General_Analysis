# General gyrokinetic analysis

Editable Jupyter notebooks using Pyrokinetics and Matplotlib. The original notebooks
are reference analyses; new investigations can start from
[template.ipynb](notebooks/template.ipynb). A small real-data example is
[growth_rate_comparison.ipynb](notebooks/growth_rate_comparison.ipynb).

## Getting started

From the repository root, with Python 3.14 and uv:

```sh
uv sync
uv run jupyter lab
```

Select the project's Python kernel. In VS Code, open a notebook and select
`.venv/bin/python`. The notebooks locate the repository from either the root or a
notebook subdirectory; no package import or editable installation is needed for
the style file.

Set `GK_DATA_ROOT` in the repository's `local.env` to the directory containing
`GS2/`, `TGLF/`, `GENE/`, etc. A `local.env.example` is provided for new checkouts;
copy it to `local.env` only if you do not already have that file. The new notebooks
load it explicitly with python-dotenv, including when launched from VS Code.
Values in `local.env` take precedence over existing environment variables, so
rerunning the settings cell picks up edits. Rerun loading and analysis afterwards.
Local environment files are ignored by Git. Missing `GK_DATA_ROOT` raises an error
instead of falling back to a machine-specific path.

You can also use an existing working Pyrokinetics Jupyter environment. Some reference
notebooks use features from a custom Pyrokinetics checkout (including PyroHypercube),
which may not exist in the published package. Select that environment's kernel for
those analyses; the notebook setup does not replace it. That environment also needs
`python-dotenv` for the new notebooks.

## Everyday use

1. Duplicate the template and give it a descriptive analysis name.
2. Set the data root in `local.env`; choose relative scan paths and scientific
   settings in the notebook. Load with Pyrokinetics.
3. Calculate/select the data in its own cell; plot using ordinary Matplotlib.
4. Rerun only plotting when changing labels, colours, or limits. Rerun calculations
   when changing selections, and loading when changing input files.
5. Run the save cell to write `Plots/<analysis-name>/<figure-name>.png`.

Input paths follow `data_root / code / run_template / project / case /
scan_information / output_file`. Each component is an editable notebook setting,
alongside `ky`, reference values, and thresholds. Use an empty string for
`scan_information` when it is not applicable, or a relative subpath for nested scan
information. The comparison example uses a per-code mapping for those subdirectories;
`metadata_file` and `output_file` select the scan metadata and saved output.

The template is a skeleton: fill its loading, calculation, and plotting cells before
saving. The worked example compares GS2 and TGLF growth rates for the `scan_q/S1_3`
scan used by `Linear_Plotting.ipynb`. Its input paths are explicit and editable. It
requires the existing `pyroscan.json`, `pyroscan.nc`, and base inputs referenced by
Pyrokinetics; missing data produces an error rather than substitute results.

New notebooks are saved without embedded outputs. Run all cells from a fresh kernel
when reviewing an analysis. Generated figures and local data are ignored by Git;
copy figures elsewhere when you want to keep a particular version. Saving to the
same filename replaces it. Historical figure/data provenance is not implemented.

## Keep the code small

[paper.mplstyle](src/general_analysis/paper.mplstyle) owns shared formatting: fonts,
figure size, markers, line widths, grids, legends, and export settings. A simple
growth-rate comparison should need no more than 10 readable plotting lines after
data preparation. Repeated default formatting belongs in the style file.

When comparing gyrokinetic codes against quasilinear models, explicitly plot the
gyrokinetic reference curves in black (`color="black"`). This is the only fixed
code colour convention. TGLF/GFTM colours remain plot-specific, so colours can
distinguish numerical settings or other quantities. The black-reference rule does
not apply to plots without a gyrokinetic-versus-quasilinear comparison.

Shared Python helpers are introduced only when an operation needs substantially
more than 10 readable lines, is actually repeated, **and** cannot be handled by the
style file. Short plotting and saving code stays inline. There is no plotting
framework, notebook pairing, or custom batch runner.

[AGENTS.md](AGENTS.md) applies these rules to agent-generated notebooks. For review,
use a short-lived branch per investigation, inspect the notebook and any scientific
changes, then merge useful work into your main working branch. Git versions the
notebooks and shared code; it does not archive the simulation data.
