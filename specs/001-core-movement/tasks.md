# Tasks: Core movement

Work from top to bottom, one task at a time. Each task names the IDs it covers, the files it changes and the test that proves it. [P] means the task can run in parallel with the one before it.

- [ ] **T001** Game state: `Game` holds the current room (the start room from world.py) and a `finished` flag. Files: `labyrinth/engine.py`. Covers FR-001.
- [ ] **T002** [P] Describe a room: `Game.describe()` returns the name, the description and the exits in compass order. Files: `labyrinth/engine.py`, `tests/test_core_slice.py`. Covers FR-002, AC-02. Test: `test_ac_02_look_shows_name_description_and_exits`.
- [ ] **T003** Look and clean input: `handle("look")` returns `describe()`; input is trimmed, lower-cased and split into words. Files: engine, tests. Covers FR-002, FR-006, AC-06. Test: `test_ac_06_commands_ignore_case_and_spaces`.
- [ ] **T004** Go: move through an exit and describe the new room; no exit gives `You can't go … from here.`; no direction gives `Go where? Exits: ….` Files: engine, tests. Covers FR-003 to FR-005, AC-03 to AC-05. Tests: `test_ac_03_…`, `test_ac_04_…`, `test_ac_05_…`.
- [ ] **T005** Help replies for an unknown command and an empty line. Files: engine, tests. Covers FR-007, FR-008, AC-07, AC-08. Tests: `test_ac_07_…`, `test_ac_08_…`.
- [ ] **T006** Quit: reply `Goodbye.` and set `finished`. Files: engine, tests. Covers FR-009, AC-09. Test: `test_ac_09_quit_ends_the_game`.
- [ ] **T007** [P] Play loop: `cli.run(stdin, stdout)` prints a welcome line and the start room, then loops until the game is finished or the input ends. Files: `labyrinth/cli.py`, tests. Covers FR-001, AC-01. Test: `test_ac_01_new_game_shows_the_iron_gate`.
- [ ] **T008** Check: run `python -m unittest -v`, play once with `python -m labyrinth`, then run `/speckit-converge`.
