"""Command-line front end. All input and output lives here, not in the engine."""

from __future__ import annotations

import sys
from typing import TextIO

from .engine import Game


def run(stdin: TextIO = sys.stdin, stdout: TextIO = sys.stdout) -> None:
    """Play until the player quits or the input ends (FR-001, FR-009)."""
    game = Game()
    print("Escape the Labyrinth. Type 'quit' to leave.", file=stdout)
    print(game.describe(), file=stdout)
    while not game.finished:
        print("> ", end="", file=stdout, flush=True)
        line = stdin.readline()
        if line == "":  # end of input behaves like quit
            print("\nGoodbye.", file=stdout)
            break
        print(game.handle(line), file=stdout)


def main() -> None:
    run()
