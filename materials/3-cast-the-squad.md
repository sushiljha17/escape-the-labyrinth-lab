# 3. Cast the squad

After `squad init`: in Copilot Chat, pick **Squad** in the agent picker and paste the text below. Squad proposes a team with names. Check it, then say `yes`.

```text
I'm setting up the team for a training lab. We're building Escape the Labyrinth, a small text adventure in Python 3.11 (standard library only), tested with unittest from the standard library (no pytest). The map is data in labyrinth/world.py, the game logic is pure in labyrinth/engine.py (no input or print), and all input and output is in labyrinth/cli.py. We work spec-driven with GitHub Spec Kit: each feature has a folder under specs/ with spec.md, plan.md and tasks.md, and the rules are in .specify/memory/constitution.md.

Cast a team of eight specialists:
1. Lead architect: owns scope, plan.md and the decisions log. Before anyone writes code, opens the feature's plan.md and checks that it contains "Gate 1: APPROVED by". If it doesn't, stops the team and says so.
2. Backend: owns labyrinth/engine.py and labyrinth/world.py.
3. Frontend: owns labyrinth/cli.py, the play loop and everything the player sees.
4. Tests: owns tests/. Writes exactly one unittest test method per acceptance criterion, named test_ac_<id>_<short_name>, and runs the tests with python -m unittest -v.
5. Reviewer: read-only. Reviews every change against spec.md and the constitution and reports findings as MUST, SHOULD or COULD. Never edits files.
6. Security: read-only. Checks input handling and error handling, and that no secrets or personal data appear in code, tests or logs.
7. Docs: owns README.md.
8. DevOps: owns .github/workflows/ci.yml.

Routing: game logic to Backend; the play loop and output to Frontend; tests to Tests; reviews to Reviewer; secrets and input safety to Security; README to Docs; CI to DevOps; scope questions and plans to the Lead architect.

Record these as permanent team directives: no code before Gate 1 is signed in the feature's plan.md; work only from the active feature's tasks.md, one task at a time; never change spec.md without asking me; write every decision to the decisions log. Propose the team now and don't write any code.
```

**Check afterwards:** `.squad/team.md` lists the members (Squad adds helpers of its own, such as Scribe), each member has a charter under `.squad/agents/`, and the four directives are in `.squad/decisions.md`. Then commit: `git add -A`, then `git commit -m "Add the squad"`.

**Models:** in VS Code every member uses the model you picked in Copilot Chat. Squad can give each member its own model when the squad runs in the GitHub Copilot CLI.
