# Escape the Labyrinth: instructions for GitHub Copilot

This repository is a training lab for spec-driven, agentic development: a tiny text adventure in Python. Features are specified with GitHub Spec Kit under `specs/<feature>/` (spec.md, plan.md and tasks.md). Once Spec Kit is set up, the project constitution is in `.specify/memory/constitution.md`.

## Ground rules (the five principles of the constitution)
- Work from the spec. Read the feature's spec.md, plan.md and tasks.md before you change code. If something is missing or unclear, ask or propose a change to the spec; don't guess.
- No code before Gate 1: the feature's plan.md must contain `Gate 1: APPROVED by <names>`.
- Every acceptance criterion (AC-xx) gets exactly one test named `test_ac_xx_<short_name>`.
- Keep tasks small and do one task at a time.
- Never put secrets, tokens or personal data in code, tests, logs or specs, and never write what the player types to logs or debug output (the game's own reply may repeat it).

## Code
- Python 3.11+, standard library only, tests included: the tests use `unittest` (`unittest.TestCase` classes), with no pytest and no other third-party packages, so nothing needs to be downloaded.
- `labyrinth/world.py` holds the map (data only). `labyrinth/engine.py` holds the game logic: no `input()` and no `print()`. `labyrinth/cli.py` does all input and output.
- Run the tests from the root of the repository with `python -m unittest -v`. Play with `python -m labyrinth`.

## When reviewing code (in VS Code or on a pull request)
- Check each changed behaviour against the acceptance criteria in the feature's spec.md and name the AC-xx it affects.
- Flag any acceptance criterion without a test, any behaviour test without an AC ID in its name, and any test that cannot fail.
- Flag imports of third-party packages such as pytest: the project uses the standard library only.
- Flag player input written to logs or debug output, `print()` or `input()` in the engine, broad `except` clauses that hide errors, and hard-coded secrets.
- Be specific and brief: one comment per issue, with a suggested fix.
