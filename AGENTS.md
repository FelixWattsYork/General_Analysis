# Analysis first

The deliverable is an understandable, editable analysis notebook and its figures.
Use the supplied notebooks as scientific and visual references; preserve them unless
the user asks for changes. Start new investigations from `notebooks/template.ipynb`.
Use descriptive `.ipynb` filenames. Do not introduce paired Python scripts, plotting
YAML, custom runners, or provenance bundles.

## Keep code visible

A shared helper is justified only when ALL of these are true:

1. The operation needs substantially more than 10 readable lines of code.
2. The same operation is actually repeated multiple times.
3. The operation cannot be handled by `src/general_analysis/paper.mplstyle`.

Keep operations of 10 or fewer lines inline. Do not compress statements, hide
formatting in another cell, or invent speculative reuse to satisfy these criteria.
Repeated short code is acceptable. Avoid wrappers around straightforward Pyrokinetics,
xarray, Matplotlib, or pathlib calls. There are no general plotting/saving helpers.
If a scientific helper qualifies, group it by topic in `src/general_analysis/` and
verify its calculations. Different existing scientific definitions must not be
silently merged into one implementation.

## Notebooks

- Separate imports/settings, data loading, calculations/selections, plotting, and
  saving. Cosmetic edits should require only plotting and saving to rerun.
- Read the machine-specific data root from `GK_DATA_ROOT` in the root `local.env`
  file using python-dotenv. Never hard-code a machine-specific data root in a new
  notebook. Preserve the user's local.env; it is ignored by Git. Build scan paths
  relative to that root in the notebook.
- Follow `data_root / code / run_template / project / case / scan_information / output`.
  Expose these components as settings beside ky, reference values, and thresholds;
  do not bury them in combined path strings. Scan information is optional (an empty
  string omits it) and may contain nested scan-specific subdirectories. Keep output
  and metadata filenames explicit. Use per-code settings when comparing codes.
- Keep relative dataset paths, modes, thresholds, averaging windows, and other scientific
  choices explicit. Briefly explain the analysis and the interpretation of results.
- Use Pyro, PyroScan, or PyroHypercube as appropriate. Pyrokinetics handles units and
  normalisation; do not add another conversion layer. Check conventions before
  comparing models. Show actual coordinates when selecting nearest values.
- Do not silently skip failed inputs, fabricate replacements, regenerate simulation
  outputs, or write into source-data directories as a plotting fallback.
- Return/use ordinary Matplotlib figures and axes. Put defaults in the shared style.
  A simple growth-rate comparison should take at most 10 readable plotting lines
  after preparation and style loading. If routine formatting makes it longer, improve
  the style file. Plot-specific labels, limits, references, and annotations stay inline.
  Complex figures may require more lines; length alone does not justify a helper.
- When comparing gyrokinetic codes (e.g. GS2, CGYRO, GENE) against quasilinear models,
  explicitly plot the gyrokinetic reference curves in black. Distinguish multiple
  reference curves with line styles/markers as needed. This is the only fixed code
  colour convention: do not assign universal colours to TGLF or GFTM, or force
  gyrokinetic curves to black in other kinds of plots. Choose colours per analysis
  to distinguish models, numerical settings, or other meaningful quantities.
- Save explicitly with `fig.savefig(...)` under `Plots/<analysis-name>/`. A fixed
  filename is replaced when saved again. No automatic data or provenance archives.
- Verify delivered analyses from a fresh kernel, including save cells. Report missing
  inputs, dependency problems, or any unexecuted parts. Never claim a successful run
  from stale notebook outputs. Check numerical changes against the reference analysis.

## Working conventions

Keep changes focused on the requested investigation. Short-lived branches are useful
for reviewing analyses; create or switch branches when requested. Preserve unrelated
user changes. Read README.md for setup; some reference notebooks use a custom
Pyrokinetics checkout. Do not replace that environment or change scientific methods
simply to make an example execute.
