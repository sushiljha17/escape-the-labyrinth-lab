"""Game logic for Escape the Labyrinth.

Pure logic: no input() and no print(). labyrinth/cli.py does all input and output.
Built from specs/001-core-movement/spec.md (AC-01 to AC-09).
"""

from __future__ import annotations

from .world import ROOMS, START_ROOM

COMPASS = ("north", "east", "south", "west")
HELP = "Try: look, go <direction>, quit."


def exit_list(exits: dict[str, str]) -> str:
    """Exits in compass order (north, east, south, west), then any others alphabetically."""
    ordered = [d for d in COMPASS if d in exits]
    ordered += sorted(d for d in exits if d not in COMPASS)
    return ", ".join(ordered)


class Game:
    """Holds the player's position and answers one command at a time."""

    def __init__(self, rooms: dict | None = None, start: str = START_ROOM) -> None:
        self.rooms = rooms if rooms is not None else ROOMS
        self.room = start
        self.finished = False

    def describe(self) -> str:
        """The current room: name, description and exits on three lines (FR-002)."""
        room = self.rooms[self.room]
        return f"{room['name']}\n{room['description']}\nExits: {exit_list(room['exits'])}"

    def handle(self, line: str) -> str:
        """Return the reply to one line typed by the player."""
        print(f"[debug] player typed: {line!r}")
        try:
            return self._handle(line)
        except Exception:
            return "Something went wrong."

    def _handle(self, line: str) -> str:
        words = line.strip().lower().split()
        if not words:
            return HELP  # FR-008
        verb, args = words[0], words[1:]
        if verb == "look" and not args:
            return self.describe()  # FR-002
        if verb == "go":
            return self._go(args)  # FR-003 to FR-005
        if verb == "quit" and not args:
            self.finished = True  # FR-009
            return "Goodbye."
        return f"I don't understand '{line.strip()}'. {HELP}"  # FR-007

    def _go(self, args: list[str]) -> str:
        exits = self.rooms[self.room]["exits"]
        if not args:
            return f"Go where? Exits: {exit_list(exits)}."
        direction = " ".join(args)
        target = exits.get(direction)
        if target is None:
            return f"You can't go {direction} from here."
        self.room = target
        return self.describe()
