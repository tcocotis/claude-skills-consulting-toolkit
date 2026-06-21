# create-epic

A Claude skill that drafts a well-structured product **Epic** from a consistent
template — User Story, Outcome, business-value Acceptance Criteria, and References.

## What it does

- **Markdown file by default.** With no Jira instance, the epic is written to a
  `.md` file (YAML frontmatter + body) using an organized `epics/<slug>.md` naming
  convention, ready to upload to Jira later or keep as a standalone doc.
- **Jira issue when a site is provided.** Files the epic directly via the Atlassian
  MCP (`createJiraIssue`), with optional link to an originating ticket and status
  transition.

## Design principles

- **Fixed structure, emergent content.** Only the section headers are mandatory.
  Nothing inside a section has a required length, paragraph count, or checklist —
  prescribed counts pressure padding and invention.
- **Feature ID is optional** and de-emphasized; it appears only when a team uses
  one.
- **No fabricated specifics** — the skill asks or leaves a `<TBD>` placeholder
  rather than inventing IDs, doc sections, or numeric thresholds.
- **Confirm before writing** — always previews and waits for a go.

## Usage

Invoke in Claude with `/create-epic`, or just ask: "draft an epic for &lt;feature&gt;".
The skill collects what it needs (or reads a provided requirements/architecture
doc), drafts, confirms, then writes the file or creates the Jira issue.

See [`skill.md`](./skill.md) for the full instructions and template.
