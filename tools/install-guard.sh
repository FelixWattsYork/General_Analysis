#!/usr/bin/env sh
# One-line installer: sh tools/install-guard.sh   (pre-commit hook for this clone)
printf '#!/usr/bin/env sh\nexec sh "$(git rev-parse --show-toplevel)/tools/block-gk-inputs.sh"\n' > "$(git rev-parse --git-path hooks)/pre-commit" && chmod +x "$(git rev-parse --git-path hooks)/pre-commit" && echo "guard installed"
