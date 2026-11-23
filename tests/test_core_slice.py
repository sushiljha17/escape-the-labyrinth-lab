"""One test per acceptance criterion in specs/001-core-movement/spec.md."""

import io
import unittest

from labyrinth.cli import run
from labyrinth.engine import Game
from labyrinth.world import ROOMS


class CoreSliceTests(unittest.TestCase):
    def test_ac_01_new_game_shows_the_iron_gate(self):
        out = io.StringIO()
        run(stdin=io.StringIO("quit\n"), stdout=out)
        text = out.getvalue()
        self.assertIn("Iron Gate", text)
        self.assertIn(ROOMS["gate"]["description"], text)
        self.assertIn("Exits: north", text)

    def test_ac_02_look_shows_name_description_and_exits(self):
        reply = Game().handle("look")
        self.assertEqual(reply.splitlines(), ["Iron Gate", ROOMS["gate"]["description"], "Exits: north"])

    def test_ac_03_go_moves_through_an_exit(self):
        game = Game()
        reply = game.handle("go north")
        self.assertEqual(game.room, "corridor")
        self.assertEqual(reply.splitlines()[0], "Long Corridor")

    def test_ac_04_a_wall_keeps_you_in_place(self):
        game = Game()
        game.handle("go north")
        self.assertEqual(game.handle("go up"), "You can't go up from here.")
        self.assertEqual(game.room, "corridor")

    def test_ac_05_go_without_a_direction_lists_the_exits(self):
        game = Game()
        game.handle("go north")
        self.assertEqual(game.handle("go"), "Go where? Exits: east, south, west.")

    def test_ac_06_commands_ignore_case_and_spaces(self):
        game = Game()
        game.handle("  GO North  ")
        self.assertEqual(game.room, "corridor")

    def test_ac_07_unknown_command_gets_a_helpful_reply(self):
        game = Game()
        self.assertEqual(game.handle("dance"), "I don't understand 'dance'. Try: look, go <direction>, quit.")
        self.assertEqual(game.room, "gate")
        self.assertFalse(game.finished)

    def test_ac_08_empty_line_lists_the_commands(self):
        self.assertEqual(Game().handle("   "), "Try: look, go <direction>, quit.")

    def test_ac_09_quit_ends_the_game(self):
        game = Game()
        self.assertEqual(game.handle("QUIT"), "Goodbye.")
        self.assertTrue(game.finished)

    def test_quick_check(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
