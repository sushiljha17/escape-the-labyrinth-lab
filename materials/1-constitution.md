# 1. The constitution

In Copilot Chat (Agent mode), type `/speckit-constitution`, a space, and paste the text below. Spec Kit writes the constitution to `.specify/memory/constitution.md`.

```text
Escape the Labyrinth is a tiny text adventure in Python 3.11 or later, standard library only, tested with unittest from the standard library (no pytest or other third-party packages). Write the constitution with exactly these five principles:
I. Every acceptance criterion has an ID. Requirements are FR-001, FR-002 and so on; acceptance criteria are Given/When/Then scenarios with the IDs AC-01, AC-02 and so on, unique across the repository and never reused. Plans, tasks, tests and commit messages refer to them.
II. One test per acceptance criterion. Every acceptance criterion has exactly one unittest test method, named test_ac_01_<short_name>; data checks are named test_data_<short_name>. A criterion without a passing test is not done.
III. Small tasks. Every task in tasks.md fits in 15 to 30 minutes and names the IDs it covers, the files it changes and the test that proves it. Agents take one task at a time.
IV. No secrets or personal data in code, tests, logs, specs or prompts. Never write what the player types to logs or debug output; only the game's own reply may repeat it. Test data is invented.
V. No code before Gate 1. Implementation starts only when the feature's plan.md contains the line "Gate 1: APPROVED by <names>". Agents propose; people decide.
Technology constraints: the map is data in labyrinth/world.py, the game logic is pure in labyrinth/engine.py (no input() and no print()), and all input and output happens in labyrinth/cli.py.
Workflow: specify, clarify, plan, tasks and analyze come before code. A gap is fixed in the spec first, then in the code.
Governance: this constitution takes precedence over other guidance in the repository; changing it needs a pull request approved by a person. Version 1.0.0, ratified 2026-11-25.
```
