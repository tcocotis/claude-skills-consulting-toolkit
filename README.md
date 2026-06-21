# Claude Skills — Consulting Toolkit

A collection of [Claude](https://claude.com/claude-code) skills for consulting and
delivery work — turning specs and plans into structured project artifacts, driving
Jira, and supporting test-driven development.

Each skill lives in its own folder with a `skill.md` (the instructions Claude
loads) and, where applicable, a `README.md`, `skill.json` manifest, and supporting
scripts or examples.

## Skills

| Skill | What it does |
|---|---|
| [create-epic](./create-epic) | Draft a structured product Epic (User Story, Outcome, business-value Acceptance Criteria, References) as a Markdown file by default, or directly in Jira when a site is provided. |
| [jira-project-creator](./jira-project-creator) | Create a complete Jira project structure (Epics, dependencies, timeline, and Plan) from a project specification document. |
| [jira-story-creator](./jira-story-creator) | Create detailed Jira Stories from implementation plans with user-story format, acceptance criteria, implementation method, and testing method. |
| [jira-status-update](./jira-status-update) | Update Jira story and test-case statuses as development progresses (In Progress, Done, status sync). |
| [tdd-test-case](./tdd-test-case) | Implement test cases using Test-Driven Development (RED-GREEN-REFACTOR), writing tests first. |
| [word-reader](./word-reader) | Read and extract content (text, structure, images) from Microsoft Word (`.docx`) files. |

## Using a skill

These are [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills).
Place a skill folder under your skills directory (e.g. `~/.claude/skills/`), then
invoke it by name (`/create-epic`) or simply describe the task — each skill's
`description` lists the phrases that trigger it.
