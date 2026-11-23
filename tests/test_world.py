"""Data checks for the map. Behaviour tests go in their own file, one per acceptance criterion.

Run every test from the root of the repository:  python -m unittest -v
"""

import unittest

from labyrinth.world import ROOMS, START_ROOM


class WorldDataTests(unittest.TestCase):
    def test_data_start_room_exists(self):
        self.assertIn(START_ROOM, ROOMS)

    def test_data_every_exit_leads_to_a_room(self):
        for room_id, room in ROOMS.items():
            for direction, target in room["exits"].items():
                with self.subTest(room=room_id, exit=direction):
                    self.assertIn(target, ROOMS, f"{room_id}: exit {direction} leads to unknown room {target}")

    def test_data_every_room_has_a_name_and_description(self):
        for room_id, room in ROOMS.items():
            with self.subTest(room=room_id):
                self.assertTrue(room["name"].strip())
                self.assertTrue(room["description"].strip())


if __name__ == "__main__":
    unittest.main()
