#!/usr/bin/env python3
"""Check that this laptop (or codespace) is ready to follow the Agentic SDLC session.

Run it from the root of the repository:  python scripts/preflight.py

It checks the tools you install before the session. It does not need Spec Kit or Squad in
this repository: you add both during the session. In a GitHub codespace the tools are
installed for you when the codespace is created.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

KIT = "lab kit v5"
ROOT = Path(__file__).resolve().parent.parent
WINDOWS = sys.platform.startswith("win")
MAC = sys.platform == "darwin"
CODESPACE = os.environ.get("CODESPACES", "").lower() == "true"
rows: list[tuple[str, str, str]] = []  # (status, what, how to fix)


def add(status: str, what: str, fix: str = "") -> None:
    rows.append((status, what, fix))


def hint(windows: str, mac: str, linux: str) -> str:
    if CODESPACE:
        return "Rerun the codespace set-up: bash .devcontainer/post-create.sh"
    return windows if WINDOWS else mac if MAC else linux


def output_of(*cmd: str) -> str | None:
    """First lines of a command's output, or None when the command isn't found."""
    exe = shutil.which(cmd[0])
    if not exe:
        return None
    try:
        done = subprocess.run([exe, *cmd[1:]], capture_output=True, text=True, timeout=60)
    except Exception:  # noqa: BLE001 - a broken tool is reported, not raised
        return ""
    return (done.stdout or "") + (done.stderr or "")


def version_in(text: str | None) -> str:
    match = re.search(r"\d+\.\d+(?:\.\d+)?", text or "")
    return match.group(0) if match else ""


def at_least(version: str, minimum: tuple[int, ...]) -> bool:
    try:
        return tuple(int(p) for p in version.split(".")) >= minimum
    except ValueError:
        return False


# Python
py = ".".join(str(p) for p in sys.version_info[:3])
if sys.version_info >= (3, 11):
    add("OK", f"Python {py} (3.11 or later)")
else:
    add("MISSING", f"Python {py} (3.11 or later)",
        hint("winget install -e --id Python.Python.3.12", "brew install python", "Install Python 3.11 or later"))

# Git
git = output_of("git", "--version")
if git is None:
    add("MISSING", "Git", hint("winget install -e --id Git.Git", "brew install git", "Install Git"))
else:
    add("OK", f"Git {version_in(git)}".strip())

# uv
uv = output_of("uv", "--version")
if uv is None:
    add("MISSING", "uv (installs Spec Kit)",
        hint("winget install -e --id astral-sh.uv   (or: python -m pip install --user uv)",
             "brew install uv", "python -m pip install --user uv"))
else:
    add("OK", f"uv {version_in(uv)} (installs Spec Kit)")

# Spec Kit CLI
specify = output_of("specify", "version")
if specify is None:
    local = Path.home() / ".local" / "bin" / ("specify.exe" if WINDOWS else "specify")
    if local.exists():
        add("MISSING", "Spec Kit CLI (specify) is installed but not on PATH",
            "Run: uv tool update-shell, then open a new terminal")
    else:
        add("MISSING", "Spec Kit CLI (specify)",
            hint("uv tool install specify-cli, then uv tool update-shell and open a new terminal",
                 "uv tool install specify-cli, then uv tool update-shell and open a new terminal",
                 "uv tool install specify-cli, then uv tool update-shell and open a new terminal"))
else:
    add("OK", f"Spec Kit CLI (specify) {version_in(specify)}".strip())

# Squad CLI
squad = output_of("squad", "--version")
if squad is None:
    add("MISSING", "Squad CLI (squad)",
        hint("winget install --id bradygaster.Squad --exact, then open a new terminal "
             "(or, with Node.js 22.5 or later: npm install -g @bradygaster/squad-cli)",
             "brew tap bradygaster/squad, then brew install --cask squad",
             "npm install -g @bradygaster/squad-cli (needs Node.js 22.5 or later)"))
else:
    add("OK", f"Squad CLI (squad) {version_in(squad)}".strip())

# VS Code with GitHub Copilot: a hint only, because Copilot can be built in
code = output_of("code", "--list-extensions")
if code is None:
    add("CHECK", "VS Code with GitHub Copilot (not checked: 'code' is not on PATH)",
        "Open VS Code: Copilot Chat should open and offer Agent mode")
elif "github.copilot" in code.lower():
    add("OK", "VS Code with GitHub Copilot")
else:
    add("CHECK", "VS Code: GitHub Copilot not found in the extension list",
        "Open VS Code, sign in to GitHub Copilot and check that Copilot Chat offers Agent mode")

# Optional tools
node = output_of("node", "--version")
if node is None:
    add("OPTIONAL", "Node.js", "Only needed to install Squad with npm (Node.js 22.5 or later)")
elif at_least(version_in(node), (22, 5)):
    add("OK", f"Node.js {version_in(node)} (optional)")
else:
    add("OPTIONAL", f"Node.js {version_in(node)}", "Squad with npm needs Node.js 22.5 or later")
if shutil.which("copilot"):
    add("OK", "GitHub Copilot CLI (optional)")
else:
    add("OPTIONAL", "GitHub Copilot CLI", "Only to run agents from the terminal; not needed for the session")

# The game package
sys.path.insert(0, str(ROOT))
try:
    from labyrinth.world import ROOMS, START_ROOM
    if START_ROOM in ROOMS:
        add("OK", "The game package loads")
    else:
        add("MISSING", "The game package loads", "Pull the latest main branch: git pull")
except Exception as exc:  # noqa: BLE001 - report any import problem to the participant
    add("MISSING", "The game package loads", f"Run this from the repository root ({exc})")

# The tests: Python's built-in unittest, so nothing is downloaded
try:
    import contextlib
    import io
    import unittest

    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), top_level_dir=str(ROOT))
    with contextlib.redirect_stdout(io.StringIO()):
        result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
    if result.testsRun and result.wasSuccessful():
        add("OK", f"The tests run: {result.testsRun} passed (Python's built-in unittest)")
    else:
        add("CHECK", "The tests run", "See what fails: python -m unittest -v")
except Exception as exc:  # noqa: BLE001 - report any problem to the participant
    add("CHECK", "The tests run", f"Pull the latest main branch: git pull ({exc})")

# Where we are, and what is already in this repository (information only)
add("INFO", "Running in: " + ("a GitHub codespace (tools installed for you)" if CODESPACE else "this computer"))
spec_kit_here = (ROOT / ".specify").is_dir()
squad_here = (ROOT / ".squad").is_dir() or (ROOT / ".github" / "agents" / "squad.agent.md").is_file()
add("INFO", "Spec Kit in this repo: " + ("added" if spec_kit_here else "not yet (we add it in the session)"))
add("INFO", "Squad in this repo: " + ("added" if squad_here else "not yet (we add it in the session)"))

width = max(len(what) for _, what, _ in rows)
place = "codespace" if CODESPACE else "laptop"
print(f"\nAgentic SDLC lab: {place} check ({KIT})\n")
for status, what, fix in rows:
    line = f"[{status:^8}] {what.ljust(width)}"
    print(line + (f"  -> {fix}" if fix else ""))

missing = [r for r in rows if r[0] == "MISSING"]
print()
if missing:
    print(f"{len(missing)} item(s) to fix before the session. Lines marked CHECK, OPTIONAL or INFO are fine as they are.")
    sys.exit(1)
print("Ready to follow along. Open Copilot Chat and pick Agent mode.")
