# Feature Specification: Core movement

**Feature**: Escape the Labyrinth, core slice
**Status**: Approved (Gate 1 is signed in plan.md)
**Input**: "Move between rooms with look and go, in any letter case; unknown commands get a helpful reply. Not yet: items or winning."

## User Scenarios & Testing

### User Story 1: Explore the labyrinth (Priority: P1)

As a player, I want to look around and move between rooms by typing simple commands, so that I can explore the labyrinth.

**Why this priority**: without looking and moving there is no game.

**Independent test**: start a game, look, walk north, walk into a wall and quit.

**Acceptance scenarios**

- **AC-01**: **Given** a new game, **When** it starts, **Then** the Iron Gate is shown with its name, its description and `Exits: north`.
- **AC-02**: **Given** I am at the Iron Gate, **When** I type `look`, **Then** I see three lines: the room name, its description and `Exits: north`.
- **AC-03**: **Given** I am at the Iron Gate, **When** I type `go north`, **Then** I am in the Long Corridor and it is shown.
- **AC-04**: **Given** I am in the Long Corridor, **When** I type `go up`, **Then** I see `You can't go up from here.` and I stay in the Long Corridor.
- **AC-05**: **Given** I am in the Long Corridor, **When** I type `go`, **Then** I see `Go where? Exits: east, south, west.`
- **AC-06**: **Given** I am at the Iron Gate, **When** I type `  GO North  `, **Then** I am in the Long Corridor.
- **AC-07**: **Given** any room, **When** I type `dance`, **Then** I see `I don't understand 'dance'. Try: look, go <direction>, quit.` and nothing changes.
- **AC-08**: **Given** any room, **When** I type an empty line, **Then** I see `Try: look, go <direction>, quit.`
- **AC-09**: **Given** the game is running, **When** I type `quit`, **Then** I see `Goodbye.` and the game ends.

### Edge cases

- `look` followed by other words (`look around`) is an unknown command (AC-07).
- Extra spaces between words are ignored (`go    north` works).
- The end of input (Ctrl+Z or Ctrl+D) ends the game like `quit`.

## Requirements

### Functional requirements

- **FR-001**: The game starts in the start room defined in `labyrinth/world.py` and shows it. (AC-01)
- **FR-002**: `look` shows the current room: name, description, and its exits in compass order: north, east, south, west, then any others. (AC-02)
- **FR-003**: `go <direction>` moves the player through an exit of the current room and shows the new room. (AC-03)
- **FR-004**: A direction without an exit leaves the player where they are and says so. (AC-04)
- **FR-005**: `go` without a direction lists the exits of the current room. (AC-05)
- **FR-006**: Commands are case-insensitive; spaces before, after and between words are ignored. (AC-06)
- **FR-007**: Anything else gets a reply that repeats what the player typed and lists the commands. (AC-07)
- **FR-008**: An empty line lists the commands. (AC-08)
- **FR-009**: `quit` says goodbye and ends the game. (AC-09)

### Key entities

- **Room**: id, name, description, exits (direction to room id), items (not used in this slice).
- **Game**: the current room and whether the game has finished.

## Success criteria

- **SC-001**: every acceptance criterion has exactly one passing test named after its ID.
- **SC-002**: a new player reaches the Watch Tower without reading the code.

## Out of scope for this slice

Items and inventory, the locked door, winning, single-letter directions (`n`, `e`, `s`, `w`) and saving the game.

## Clarifications

### Session 2026-11-25

- Q: Should single-letter directions such as `n` work? → A: Not in this slice.
- Q: In what order are exits listed? → A: Compass order: north, east, south, west, then any others.
- Q: What happens at the end of input? → A: The game ends quietly, like `quit`.
