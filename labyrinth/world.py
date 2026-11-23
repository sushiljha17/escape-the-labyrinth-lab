"""The map of the labyrinth. Data only: no game logic lives here.

Every room has a name, a description, its exits (direction -> room id)
and the items lying in it. Items are not used until a later slice.
"""

START_ROOM = "gate"

ROOMS = {
    "gate": {
        "name": "Iron Gate",
        "description": "Rusty bars behind you, a damp corridor ahead. A cold draught comes from the north.",
        "exits": {"north": "corridor"},
        "items": [],
    },
    "corridor": {
        "name": "Long Corridor",
        "description": "Torches flicker along the stone walls. Passages lead east and west; the gate is to the south.",
        "exits": {"south": "gate", "east": "library", "west": "well"},
        "items": ["torch"],
    },
    "library": {
        "name": "Dusty Library",
        "description": "Shelves of crumbling books. A narrow stair climbs to the north.",
        "exits": {"west": "corridor", "north": "tower"},
        "items": ["map"],
    },
    "well": {
        "name": "Old Well",
        "description": "A deep well in the middle of a round room. The only way out is the way you came.",
        "exits": {"east": "corridor"},
        "items": ["brass key"],
    },
    "tower": {
        "name": "Watch Tower",
        "description": "Wind howls through an arrow slit. A heavy door to the east is locked.",
        "exits": {"south": "library"},
        "items": [],
    },
}
