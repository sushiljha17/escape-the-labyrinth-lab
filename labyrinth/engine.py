"""Game logic for Escape the Labyrinth.

Build this from your spec: specs/<your feature>/spec.md, plan.md and tasks.md.
Constitution rule: game logic is pure. No input() and no print() in this file;
labyrinth/cli.py does all input and output.
"""

from __future__ import annotations

from .world import ROOMS, START_ROOM


class Game:
    """Holds the player's position and answers one command at a time."""

    def __init__(self, rooms: dict | None = None, start: str = START_ROOM) -> None:
        self.rooms = rooms if rooms is not None else ROOMS
        self.room = start
        self.finished = False

    def handle(self, line: str) -> str:
        """Return the reply to one line typed by the player."""
        raise NotImplementedError("Not built yet: implement it from tasks.md")
