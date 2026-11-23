# Implementation Plan: Core movement

**Spec**: `specs/001-core-movement/spec.md`

## Summary

A pure `Game` class in `labyrinth/engine.py` answers one command at a time. `labyrinth/cli.py` runs the play loop. The map stays in `labyrinth/world.py`.

## Technical context

- **Language**: Python 3.11+, standard library only
- **Tests**: unittest from the standard library, run with `python -m unittest -v`
- **Structure**: `labyrinth/world.py` (data), `labyrinth/engine.py` (logic, no input or output), `labyrinth/cli.py` (input and output), `tests/test_core_slice.py` (one test per acceptance criterion)

## Constitution check

| Principle | How this plan meets it |
|---|---|
| I. IDs on every acceptance criterion | AC-01 to AC-09 and FR-001 to FR-009 in spec.md |
| II. One test per criterion | `tests/test_core_slice.py`: `test_ac_01_…` to `test_ac_09_…` |
| III. Small tasks | Eight tasks of 15 to 30 minutes in tasks.md |
| IV. No secrets or personal data | No configuration; player input never goes to logs or debug output |
| V. No code before Gate 1 | The Gate 1 line at the end of this plan |

## Design

- `Game(rooms=ROOMS, start=START_ROOM)` keeps `room` (the current room id) and `finished`.
- `Game.describe() -> str` returns three lines: name, description, `Exits: …`.
- `Game.handle(line: str) -> str` trims the line, lower-cases it and splits it into words, then handles `look`, `go` and `quit`; anything else gets the help reply.
- `cli.run(stdin, stdout)` prints a welcome line and the start room, then reads lines until the game is finished or the input ends. `cli.main()` runs it in the terminal; `python -m labyrinth` starts it.
- Reply texts, exactly as in spec.md: `You can't go <direction> from here.` · `Go where? Exits: <exits>.` · `I don't understand '<what was typed>'. Try: look, go <direction>, quit.` · `Try: look, go <direction>, quit.` · `Goodbye.`

## Risks

- The tests compare exact reply texts: copy them from spec.md, don't paraphrase.

Gate 1: APPROVED by Sushil
