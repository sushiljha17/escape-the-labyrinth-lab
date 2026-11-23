# 2. The feature, the clarify answers and the stack

## For /speckit-specify

In Copilot Chat (Agent mode), type `/speckit-specify`, a space, and paste:

```text
Escape the Labyrinth, core slice. A player explores the labyrinth by typing commands.
"look" shows the room the player is in: its name, its description and the exits.
"go <direction>" moves the player through an exit and shows the new room.
Commands work in any letter case and ignore extra spaces.
Anything the game doesn't understand gets a helpful reply that says which commands exist.
"quit" ends the game.
Not yet: items, inventory, the locked door or winning.
The map is already defined in labyrinth/world.py.
```

## For /speckit-clarify

Answer the questions your own way. If you want the speaker's answers (they match the pull request in the Ship it demo):

| If it asks about | Answer |
|---|---|
| Single-letter directions such as `n` | Not in this slice. |
| The order of the exits | Compass order: north, east, south, west, then any others. |
| `go` without a direction | Reply `Go where? Exits: <exits>.` |
| A direction without an exit | Reply `You can't go <direction> from here.` and stay in the room. |
| An unknown command | Reply `I don't understand '<what was typed>'. Try: look, go <direction>, quit.` |
| An empty line | Reply `Try: look, go <direction>, quit.` |
| `quit`, or the end of the input | Reply `Goodbye.` and end the game, without asking for confirmation. |

## For /speckit-plan

Type `/speckit-plan`, a space, and paste:

```text
Python 3.11+, standard library only. Tests use unittest from the standard library (no pytest), run with python -m unittest -v. Keep the game logic pure in labyrinth/engine.py (no input or print), all input and output in labyrinth/cli.py, and the map in labyrinth/world.py. One unittest test method per acceptance criterion, in tests/test_core_slice.py.
```

Then type `/speckit-tasks`. There's nothing to paste.
