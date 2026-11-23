#!/usr/bin/env bash
# Runs once, when a codespace is created. It installs the tools from the laptop list, so you
# can follow the session in the browser without installing anything yourself.
#
# It does NOT add Spec Kit or Squad to this repository: `specify init` and `squad init` are
# steps of the session, exactly as on a laptop.
#
# The versions are fixed, so that every codespace behaves the same on the day.
set -u

SPEC_KIT_VERSION="1.4.3"   # Spec Kit CLI: specify-cli on PyPI
SQUAD_VERSION="1.1.0"      # Squad CLI: @bradygaster/squad-cli on npm

export PATH="$HOME/.local/bin:$PATH"
problems=0

echo "== uv (installs Spec Kit)"
python -m pip install --user --quiet --disable-pip-version-check uv || problems=$((problems + 1))

echo "== Spec Kit CLI ${SPEC_KIT_VERSION}"
if ! uv tool install "specify-cli==${SPEC_KIT_VERSION}"; then
  echo "   That version isn't available: installing the latest Spec Kit CLI instead."
  uv tool install specify-cli || problems=$((problems + 1))
fi
uv tool update-shell >/dev/null 2>&1 || true

echo "== Squad CLI ${SQUAD_VERSION}"
if ! npm install -g --no-fund --no-audit "@bradygaster/squad-cli@${SQUAD_VERSION}"; then
  echo "   That version isn't available: installing the latest Squad CLI instead."
  npm install -g --no-fund --no-audit @bradygaster/squad-cli || problems=$((problems + 1))
fi

echo
echo "== Codespace check"
python scripts/preflight.py || true

if [ "$problems" -gt 0 ]; then
  echo
  echo "Some tools could not be installed (${problems}). Open a terminal and run: bash .devcontainer/post-create.sh"
fi
exit 0
