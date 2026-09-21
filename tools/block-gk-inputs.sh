#!/usr/bin/env sh
# Pre-commit guard: block gyrokinetic INPUT decks (GS2/GENE/TGLF/CGYRO) and
# pyrokinetics-serialised data bundles from being committed.
#
# Why: GK input files (and pyro outputs, which embed the input geometry) encode
# sensitive STEP geometry/profiles and must never reach a repo. See CLAUDE.md
# "Data Handling Policy". Rendered plots, CSV summaries and analysis scripts are fine.
#
# Conscious override for a genuine false positive:
#   ALLOW_GK_INPUT=1 git commit ...

if [ "${ALLOW_GK_INPUT:-0}" = "1" ]; then
  echo "block-gk-inputs: override active (ALLOW_GK_INPUT=1) — skipping GK input checks." >&2
  exit 0
fi

# With arguments, check those files instead of the staged set (used by CI, which
# passes the PR's changed files); with none, check what is staged.
if [ $# -gt 0 ]; then staged="$*"; else staged=$(git diff --cached --name-only --diff-filter=AM); fi
[ -z "$staged" ] && exit 0

blocked=""

# Unambiguous GK input-deck filenames, or STEP/SPR case markers in the path.
name_is_gk_input() {
  bn=$(basename "$1")
  case "$bn" in
    *.in|*.nml|input.tglf|input.tglf.gen|input.gacode|input.profiles|\
input.cgyro|input.gene|gs2.in|parameters*) return 0 ;;
  esac
  case $(printf '%s' "$1" | tr 'A-Z' 'a-z') in
    *spr-045*|*spr045*|*spr_045*|*step-ec-hd*) return 0 ;;
  esac
  return 1
}

# Extensions never content-scanned: docs, scripts, plots, summaries.
# .jsonl belongs here alongside .json: the beads export (.beads/issues.jsonl)
# is issue prose, and this backlog discusses TGLF parameters by name -- CLAUDE.md
# requires their native upper-case form -- so NBASIS_MIN/WIDTH_MIN/FIND_WIDTH/
# THETA_TRAPPED appear hundreds of times and trip the >=3-key heuristic below on
# every beads commit. Name-based blocking still applies to .jsonl; only the
# content heuristic is skipped.
# .qmd is the same class as .md (Quarto's markdown format) and hits the same
# false positive: a slide deck explaining GFTM/TGLF numerics by name
# (Fusion_PhD-ubi) trips the >=3-key heuristic on prose alone, with no
# namelist values or geometry present.
skip_scan() {
  case "$1" in
    *.md|*.qmd|*.rst|*.py|*.ipynb|*.sh|*.json|*.jsonl|*.yaml|*.yml|*.toml|*.cfg|*.ini|\
*.csv|*.tsv|*.png|*.pdf|*.svg|*.jpg|*.jpeg|*.bib|*.tex|*.gitignore) return 0 ;;
  esac
  return 1
}

# Notebooks must be committed output-free: any cell output can carry a printed
# pyro dataset / local_geometry. ALL outputs are blocked (images included) so
# the rule has no exceptions a future agent could get wrong. Source cells are
# not scanned; .ipynb stays in skip_scan for the text heuristic.
nb_has_outputs() {
  # Verdict as a STRING, not an exit code: a python traceback also exits 1, so
  # keying "clean" off rc=1 let an unparseable notebook through -- the opposite
  # of fail-closed. Only a definite CLEAN passes; a crash, a malformed cell, or
  # a missing python3 all yield empty output and block.
  v=$(python3 -c 'import json,sys
try:
    nb = json.load(open(sys.argv[1]))
    cells = nb.get("cells") or [c for w in nb.get("worksheets", []) for c in w.get("cells", [])]
    print("BLOCK" if any(c.get("outputs") for c in cells) else "CLEAN")
except Exception:
    print("BLOCK")' "$1" 2>/dev/null)
  [ "$v" != "CLEAN" ]
}

# Text file looks like a GK input deck (Fortran namelist groups, or >=3 TGLF keys).
text_has_gk_signature() {
  grep -Eiq '^[[:space:]]*&(theta_grid|species_parameters|dist_fn|kt_grids|gs2_diagnostics|knobs|geometry|box|general|nonlinear|info|units)' "$1" && return 0
  n=$(grep -Eio '(rlts_[0-9]|rlns_[0-9]|as_[0-9]|zs_[0-9]|mass_[0-9]|taus_[0-9]|theta_trapped|nbasis_max|nbasis_min|nxgrid|use_bper|use_bpar|geometry_flag|kygrid_spectrum_shift|find_width|width_min|width_max)' "$1" 2>/dev/null | tr 'A-Z' 'a-z' | sort -u | wc -l)
  [ "${n:-0}" -ge 3 ] && return 0
  return 1
}

# NetCDF/HDF5 header carries GK-input / pyrokinetics / geometry signatures.
nc_has_gk_signature() {
  hdr=""
  if command -v ncdump >/dev/null 2>&1; then
    hdr=$(ncdump -h "$1" 2>/dev/null)
  fi
  if [ -z "$hdr" ] && command -v h5dump >/dev/null 2>&1; then
    hdr=$(h5dump -H "$1" 2>/dev/null)
  fi
  if [ -z "$hdr" ]; then
    # No inspector available — cannot verify a binary GK-format file; fail closed.
    return 0
  fi
  printf '%s' "$hdr" | grep -Eiq 'pyrokinetics|theta_grid|species_parameters|local_geometry|miller|flux_surface|dist_fn|(^|[^a-z])(gs2|gene|cgyro|tglf)([^a-z]|$)' && return 0
  return 1
}

for f in $staged; do
  [ -f "$f" ] || continue
  if name_is_gk_input "$f"; then
    blocked="$blocked\n  [name]    $f"
    continue
  fi
  case "$f" in
    *.nc|*.cdf|*.h5|*.hdf5)
      nc_has_gk_signature "$f" && blocked="$blocked\n  [data]    $f"
      continue ;;
  esac
  case "$f" in
    *.ipynb) nb_has_outputs "$f" && blocked="$blocked\n  [notebook-outputs] $f"; continue ;;
  esac
  skip_scan "$f" && continue
  text_has_gk_signature "$f" && blocked="$blocked\n  [content] $f"
done

if [ -n "$blocked" ]; then
  printf '\n\033[31mBLOCKED: gyrokinetic input / data files staged for commit.\033[0m\n' >&2
  printf 'These can embed STEP geometry/profiles and must never reach a repo (see CLAUDE.md).\n' >&2
  printf '%b\n' "$blocked" >&2
  printf '\nIf this is genuinely a derived, input-free artifact, re-commit with:\n  ALLOW_GK_INPUT=1 git commit ...\n\n' >&2
  exit 1
fi
exit 0
