---
name: create-epic
description: Draft a well-structured product Epic using a consistent template — User Story, Outcome, business-value Acceptance Criteria, and References. Writes the epic as a Markdown file by default, or files it directly in Jira when a Jira site is provided. Use when someone wants to draft or create a feature epic, write an epic in the standard format, or turn a feature idea into an epic doc or Jira issue. Triggers on "create an epic", "draft an epic", "new feature epic", "write an epic for <feature>".
version: 1.0.0
tags: [epic, jira, agile, user-stories, acceptance-criteria, markdown, planning]
---

# Create Epic

Produces an Epic in a structured, repeatable format. The fixed part is the set of
section headers, in order. Everything inside a section is free prose whose depth
follows the feature — write what's true, let detail emerge, never pad to fill a
shape.

**Two output modes**, chosen by whether a Jira site is provided:

- **Markdown file (default).** No Jira site → write the epic to a `.md` file that
  can be uploaded to Jira later, or kept as a standalone doc. This is the path for
  projects without a Jira instance.
- **Jira issue.** A Jira site/project is provided → create the epic directly via
  the Atlassian MCP.

Either way: **draft → confirm with the user → write/create**. Do not skip
confirmation; do not invent facts to fill the template (see Guardrails).

## Inputs to collect (ask, or infer from provided docs)

| Input | Notes |
|---|---|
| Title | Short feature title. Required. |
| Initiative / release | Program bracket for the title, e.g. a release name. Optional. |
| Persona | Who the user is — role, context. |
| Want / so-that | The capability and the value it unlocks. |
| Mechanism | How it works — only as deep as the feature warrants. |
| Outcome | What's observably true when it's working. |
| Acceptance criteria | Measurable, business-value framed. |
| References | Originating idea/ticket, design docs, downstream dependents. |
| Feature ID | A short feature code. **Optional and usually omitted** — include only if the team uses one. |
| Output location | Markdown file path (default), or Jira site + project key. |
| Priority / labels / assignee | Optional metadata. Defaults: priority `Medium`, no labels. |

If the repo or attached context contains a requirements or architecture document,
read it and draft from it instead of making the user retype everything — then
confirm.

## Title format

```
[<Initiative>] <Short Title>
```

- The `[<Initiative>]` bracket is optional — drop it if the team doesn't use one.
- If (and only if) the team uses feature IDs, append it at the **end**:
  `[<Initiative>] <Short Title> — <Fxx>`. By default, no feature ID.
- This string is the Jira summary in Jira mode, and the H1 in Markdown mode.

## Markdown file output

When writing a file, use this layout — YAML frontmatter (so it can be uploaded to
Jira later) followed by the epic body:

```markdown
---
title: <Short Title>
type: Epic
status: To Do
# initiative, feature_id, priority, labels, implements — include only if used
---

# [<Initiative>] <Short Title>

<epic body — the sections below>
```

**Filename convention.** Keep epics organized and sortable. Default to an `epics/`
directory and a lowercased, kebab-case name carrying enough to identify the epic:

```
epics/[<initiative-slug>-][<feature-id>-]<title-slug>.md
```

Examples:
- `epics/release-1-per-item-topic-tagging.md`
- `epics/release-1-f17-per-item-topic-tagging.md`
- `epics/per-item-topic-tagging.md`  (no initiative, no feature id)

Confirm the directory/path with the user before writing, and don't overwrite an
existing file without asking.

## Epic body template (sections are fixed; prose emerges)

> In Jira mode pass this as `description` with `contentFormat: markdown` — use REAL
> newlines, never literal `\n`. In Markdown mode it's the body under the H1.
>
> The `##` headers are the fixed structure. Each angle-bracket note describes what
> the section is *for* — replace it with prose that fits the actual feature. Write
> only what applies; drop a sentence rather than pad it.

```markdown
<Optional opening context line — use it only if there's something a reader needs up
front: how this epic relates to sibling work, why it stands alone or combines, a
pointer to the governing design doc. Omit entirely if there's nothing to say.>

## User Story

**As a** <persona>,
**I want** <capability>,
**so that** <the value it unlocks>.

<Then explain it in prose, to whatever depth the feature needs: the persona's
situation today and what changes, and a **Mechanism:** sense of how it works.
Reach for specifics — where it runs, what it reads or writes, fallbacks,
assumptions, design-doc references — only where they genuinely apply.>

## Outcome

<What becomes observably true once this is operating, and why it matters. Note the
cost or tradeoff it introduces if there is one worth stating.>

## Acceptance Criteria (business-value measurement)

* **<Criterion>**: <a measurable, business-value-framed condition, with how/when
  it's verified>.
<One bullet per real, verifiable condition — let the count emerge from the feature.
Favor measurable outcomes (coverage, precision/recall, latency, cost envelope,
enforced invariants, graceful degradation) over task checklists. If something can't
be measured or verified, leave it out rather than invent a threshold.>

## Reference

<Pointers that ground the epic: the originating idea/ticket it implements, design
docs and their relevant sections, anything downstream that depends on it. Include
only links that exist.>
```

**Feature ID (optional).** Most epics have none — then it appears nowhere. When the
team does use one, either append it to the title (see above) and/or add a short
`## Feature ID` section (e.g. `**Feature ID:** <Fxx> — see <doc> §<section>`).

## Procedure

1. **Gather inputs** from the user and/or provided docs (see table). Ask only for
   what's missing.
2. **Pick the output mode** — Markdown file unless a Jira site/project is given.
3. **Draft** the title and body using the template — depth driven by the feature,
   not by filling sections.
4. **Confirm with the user** — show a compact preview (title + the section headers
   + the acceptance criteria), roughly one screen, and the target path/destination.
   Wait for explicit go.
5. **Write/create:**
   - *Markdown mode:* write the file to the agreed path using the filename
     convention; report the path.
   - *Jira mode:* `createJiraIssue` with `cloudId` = the site, `projectKey`,
     `issueTypeName` = `Epic`, `contentFormat` = `markdown`, the summary, and
     `additional_fields` = `{ "priority": {"name": "..."}, "labels": [...] }`.
6. **Link / status (Jira mode):** link to the originating ticket via
   `createIssueLink` if one exists; transition status if requested. (In Markdown
   mode these live in the frontmatter.)
7. **Report** the file path, or the new issue key and its browse URL.

## Guardrails

- **No fabricated specifics.** Don't invent feature IDs, doc section numbers,
  ticket keys, downstream dependents, or numeric thresholds the user/docs didn't
  supply. Ask, or leave a clear `<TBD>` placeholder in the draft.
- **Let content emerge.** No section has a required length, paragraph count, or
  checklist of sub-points. Write what the feature warrants and stop.
- **Feature ID stays optional.** Don't add it unless the team actually uses one.
- **No `\n` escapes** — use real newlines.
- **Confirm before writing.** Never auto-file or overwrite without the user's go.
