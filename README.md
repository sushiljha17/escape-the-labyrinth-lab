# Escape the Labyrinth: an agentic SDLC lab

A tiny text adventure in Python, used to show the agentic development lifecycle end to end: **spec it** with GitHub Spec Kit, **squad it** with a team of Copilot agents, **check it** with the tests and GitHub Copilot code review, and **ship it** through a pull request that Copilot reviews too.

You don't need to know Python.

## How the session works

The speaker builds everything live, step by step. You choose how to join:

- **Watch.** Nothing to install.
- **Follow along on your laptop.** Type the same steps in your own clone, on your own. Fall behind, or something fails? Just watch: every step is below, in the same order.
- **Follow along in your browser, in a GitHub codespace.** Nothing to install: the tools are ready in the codespace. See [Follow along in a codespace](#follow-along-in-a-codespace).
- **Build later.** This repository and its steps stay online after the session.

This repository starts clean on purpose: there's no Spec Kit and no Squad in it yet. You add both during the session, the way you would in any repo.

## Before the session: on your laptop

1. Install the tools: VS Code with GitHub Copilot (signed in with your Copilot licence), Git, Python 3.11 or later, uv, the Spec Kit CLI (`uv tool install specify-cli`) and the Squad CLI (`winget install --id bradygaster.Squad --exact`). The full list, with install commands, came with your invitation.
2. Clone this repository and open the folder in VS Code. Trust the workspace when VS Code asks.
3. In the terminal, at the root of the repository: `python scripts/preflight.py`. Every required line should say OK.
4. Optional: `python -m unittest -v` runs the three map checks and ends with `OK` (the game itself isn't built yet). The tests use Python's built-in unittest, so there's nothing to download.

Please don't run `specify init` or `squad init` before the session: that's what we do together.

## Follow along in a codespace

A codespace is VS Code in your browser, running on GitHub, with the tools from the laptop list already installed: Python, Git, uv, the Spec Kit CLI, the Squad CLI and GitHub Copilot Chat. Spec Kit and Squad are not in the repository yet: you add them in the session, like everyone else.

1. Sign in to github.com with the GitHub account you'll use. A personal account works. A company-managed GitHub account (Enterprise Managed Users) can't open codespaces on repositories outside its company: use your laptop instead, or a personal account.
2. On this repository's page: **Code**, **Codespaces**, **Create codespace on main**. The first start takes a few minutes, so do it before the session starts. This README opens when the codespace is ready.
3. In the terminal (bottom of the screen): `python scripts/preflight.py`. Every required line should say OK. A line says MISSING? Run `bash .devcontainer/post-create.sh` and check again.
4. Open Copilot Chat and pick **Agent**. Copilot uses the plan of the GitHub account you're signed in with. No Copilot licence on that account? You get Copilot Free: enough to follow Part 1, but with a limited allowance and without Copilot code review (Part 3, step 3).
5. Follow Part 1 below from step 1. Everything works the same as on a laptop; the terminal is Linux (bash) instead of PowerShell.

When you're done: **github.com/codespaces**, then **...** next to your codespace, **Delete**. Personal accounts include a free monthly allowance for Codespaces (on GitHub Free: 120 core hours, about 60 hours on the standard 2-core machine), and an idle codespace stops by itself after 30 minutes. You don't need to push anything: your work stays in your codespace.

## Part 1: spec it

In the terminal, at the root of the repository:

| Step | Type | What happens |
|---|---|---|
| 1 | `specify init . --integration copilot` | Spec Kit joins the repository. Confirm when it warns that the folder isn't empty. If it asks for a script type, take the default. Your laptop blocks PowerShell scripts? Add `--script py` to use Spec Kit's Python scripts instead. |
| 2 | `git status` | What Spec Kit added: `.specify/` and its commands as skills under `.github/skills/`. |
| 3 | `git add -A`, then `git commit -m "Add Spec Kit"` | A clean point to come back to. |

Then in Copilot Chat, in **Agent** mode:

| Step | Type in Copilot Chat | What happens |
|---|---|---|
| 4 | `/speckit` | The Spec Kit commands appear. If not: Command Palette, **Developer: Reload Window**. |
| 5 | `/speckit-constitution` + the text in `materials/1-constitution.md` | `.specify/memory/constitution.md`: five rules that every later step is checked against. |
| 6 | `/speckit-specify` + the feature in `materials/2-feature.md` | `specs/001-…/spec.md`, with requirement IDs and Given/When/Then scenarios. Spec Kit may switch to a new branch. |
| 7 | `/speckit-clarify` | Up to five questions. Answer them your own way, or use the suggestions in `materials/2-feature.md`. |
| 8 | `/speckit-plan` + the stack text in `materials/2-feature.md` (section "For /speckit-plan"), then `/speckit-tasks` | `plan.md` with a check against the constitution, and `tasks.md` with small tasks. |
| 9 | `/speckit-analyze` | A read-only check for gaps and conflicts. Fix anything critical in the spec, not in the code. |
| 10 | In the terminal: `git add -A`, then `git commit -m "Spec, plan and tasks"` | Don't sign Gate 1 yet: the squad checks for it. |

## Part 2: squad it

| Step | Type | What happens |
|---|---|---|
| 1 | In the terminal: `squad init` | Squad joins the repository: `.github/agents/squad.agent.md` (the coordinator) and `.squad/`. |
| 2 | In Copilot Chat, pick **Squad** in the agent picker and paste the prompt in `materials/3-cast-the-squad.md` | Squad proposes a team with names. Say `yes`. It writes the team, the routing and the rules to `.squad/` (the decisions log is `.squad/decisions.md`). |
| 3 | With **Squad** still selected: `Team, implement specs/001-…/tasks.md` (use your folder name) | The lead should refuse: Gate 1 isn't signed. People decide. |
| 4 | Open `specs/001-…/plan.md`, add `Gate 1: APPROVED by <your name>` as its last line and save. Then type `Team, implement specs/001-…/tasks.md: game logic and UI in parallel, one test per acceptance criterion, reviewer read-only.` | The team builds the slice. Allow file changes when VS Code asks. It takes a while: watch the speaker's screen meanwhile. |

## Part 3: check it

| Step | Type | What happens |
|---|---|---|
| 1 | `python -m unittest -v` | One test per acceptance criterion, listed by name; the run ends with `OK`. Send any failure back to the squad: "fix the code, not the test". |
| 2 | `python -m labyrinth` | Play: `look`, `go north`, `go up`, `dance`, `quit`. |
| 3 | Source Control view: hover over **Changes**, then **Copilot Code Review - Uncommitted Changes** | GitHub Copilot code review checks your changes against the review rules in `.github/`. Findings appear as comments in the code; some also in the Problems tab. Already committed? Select code in `labyrinth/engine.py`, right-click, **Review**. |
| 4 | Fix what matters (ask the squad), or write down why not | You decide. |
| 5 | Optional: `/speckit-converge` | Checks the code against the spec, plan and tasks. |

Write down one correction you had to make to an agent, and what would have prevented it. The afternoon session on context engineering uses them.

## Part 4: ship it (watch)

The speaker shows the last step on GitHub: a pull request with the same work, reviewed by GitHub Copilot code review with the same rules, and merged by a person.

## If something doesn't work

| Problem | Try |
|---|---|
| `specify` or `squad` isn't found | Open a new terminal. For Spec Kit, run `uv tool update-shell` once, then open a new terminal. In a codespace: `bash .devcontainer/post-create.sh`. |
| `specify init` doesn't know `--integration` | Your Spec Kit is old: `uv tool install --force specify-cli`. |
| `specify init .` isn't accepted | Use `specify init --here --integration copilot`. |
| uv shows a TLS or certificate error | Your network checks TLS traffic. Add `--system-certs` to the uv command (older uv versions: `--native-tls`), for example `uv tool install specify-cli --system-certs`. |
| The `/speckit` commands don't appear | Reload the window. Check that Copilot Chat is in Agent mode and that agent skills are on in Settings (search for "skills"). |
| Squad isn't in the agent picker | Reload the window, and check that `.github/agents/squad.agent.md` exists. |
| No **Copilot Code Review** option | Your Copilot plan or your organisation's policy doesn't include code review (Copilot Free doesn't). Ask the squad's reviewer for findings instead. |
| No **Codespaces** tab, or creating one fails | Your GitHub account can't open codespaces for this repository (for example a company-managed account). Follow on your laptop, or watch. |
| Anything else | Watch, and try again after the session from this page. |

## What's in the repository

| Path | What it is |
|---|---|
| `labyrinth/world.py` | The map (data only) |
| `labyrinth/engine.py`, `labyrinth/cli.py` | Game logic and the play loop: the squad builds them |
| `tests/` | Map checks now; one test per acceptance criterion after the squad's build. Python's built-in unittest: `python -m unittest -v` |
| `materials/` | The texts you paste: the constitution, the feature and the prompt that casts the squad |
| `.github/copilot-instructions.md` | Rules for Copilot in the editor and in code review |
| `.github/instructions/tests.instructions.md` | Extra rules for test files, in the editor and in code review |
| `.github/workflows/ci.yml` | GitHub Actions: runs the tests on every pull request |
| `scripts/preflight.py` | Checks that your laptop or codespace is ready |
| `.devcontainer/` | The codespace set-up: installs the tools (not Spec Kit or Squad in the repo) |

## About this lab

A learning exercise: use invented data only, never customer data, personal data or credentials. Spec Kit (github.com/github/spec-kit) and Squad (github.com/github/squad) are open-source projects. The lab is inspired by the GitHub Copilot Summer Bootcamp session on Squad and spec-driven development.
