---
name: jira-project-creator
description: Automatically creates a complete Jira project structure (Epics, dependencies, timeline, and Plan) from a project specification document. Use this skill when the user wants to create a Jira project, set up Jira structure, scaffold Jira epics, create project plan in Jira, or generate Jira from specification. Triggers include "create Jira project", "set up Jira", "scaffold epics", "populate Jira from spec", "generate Jira structure", "create project timeline".
version: 1.0.0
tags: [jira, project-setup, epics, automation, planning]
---

# Jira Project Creator from Specification

## Auto-Invocation Triggers

This skill should be automatically invoked when the user:
- Wants to **create a Jira project** from a specification document
- Says "**set up Jira**", "**scaffold Jira**", or "**initialize Jira project**"
- Mentions "**create epics from spec**" or "**populate Jira from specification**"
- References "**generate Jira structure**" or "**create project timeline in Jira**"
- Wants to **set up Jira dependencies**, **create Jira plan**, or **build Jira roadmap**
- Has a specification document and needs to **convert it to Jira**

**Keywords:** create Jira project, set up Jira, scaffold Jira, create epics, Jira structure, project timeline, Jira dependencies, specification to Jira, Jira roadmap

## Description
Automatically creates a complete Jira project structure (Epics, dependencies, timeline, and Plan) from a project specification document.

## When to Use
- You have a project specification document (Word, PDF, or Markdown)
- You want to automatically create Jira Epics with dependencies
- You want to set up a timeline and Gantt chart view
- You're starting a new project and need to set up Jira quickly

## Prerequisites
- Jira Cloud account with API access
- Jira API token
- Project specification document with:
  - Project stages/epics
  - Timeline information
  - Dependencies (optional)
  - Start/end dates

## Usage

```bash
# Basic usage
python jira-project-creator.py --spec path/to/spec.docx --config config.json

# With custom timeline compression (1 week = 1 day)
python jira-project-creator.py --spec spec.docx --config config.json --compress-timeline 7

# Dry run (preview without creating)
python jira-project-creator.py --spec spec.docx --config config.json --dry-run
```

## Configuration

Create a `config.json` file:

```json
{
  "jira": {
    "instanceUrl": "https://yourcompany.atlassian.net",
    "email": "your.email@company.com",
    "apiToken": "your-api-token",
    "projectKey": "PROJ"
  },
  "timeline": {
    "startDate": "2026-02-14",
    "compressionFactor": 7,
    "workDaysPerWeek": 7
  },
  "options": {
    "createPlan": true,
    "addDescriptions": true,
    "addDependencies": true,
    "addLabels": true
  }
}
```

## What It Does

1. **Reads Specification Document**
   - Extracts project name, stages/epics, timeline
   - Identifies dependencies between stages
   - Parses acceptance criteria and deliverables

2. **Creates Jira Epics**
   - Creates Epic for each stage
   - Adds detailed descriptions
   - Sets priority levels
   - Adds relevant labels

3. **Sets Up Dependencies**
   - Creates "blocks" relationships between epics
   - Ensures proper development sequence

4. **Adds Timeline**
   - Calculates start and due dates
   - Supports timeline compression (e.g., 1 week = 1 day)
   - Handles working days vs calendar days

5. **Creates Jira Plan** (if Advanced Roadmaps available)
   - Sets up a new Plan with all epics
   - Configures Gantt chart view
   - Shows dependencies visually

## Output

The skill will:
- Create all epics in Jira
- Print summary of created issues
- Provide direct links to view in Jira
- Export a summary report (optional)

## Examples

### Example 1: Standard Project Setup
```bash
python jira-project-creator.py \
  --spec AuragenAI-System-Spec.docx \
  --config jira-config.json \
  --project-key AURA
```

### Example 2: Compressed Timeline
```bash
python jira-project-creator.py \
  --spec project-spec.docx \
  --config config.json \
  --compress-timeline 7 \
  --start-date tomorrow
```

### Example 3: Dry Run (Preview Only)
```bash
python jira-project-creator.py \
  --spec spec.docx \
  --config config.json \
  --dry-run \
  --output preview.json
```

## Customization

You can customize:
- Epic naming convention
- Label taxonomy
- Priority assignment logic
- Dependency inference rules
- Timeline calculation method

## Limitations

- Requires Jira Premium/Enterprise for Advanced Roadmaps (Plans)
- Cannot create Epics if project doesn't exist
- Dependency detection is based on keywords (can be improved with AI)

## Future Enhancements

- [ ] Auto-create Stories under each Epic
- [ ] Import from multiple document formats
- [ ] AI-powered dependency detection
- [ ] Story point estimation
- [ ] Team assignment based on skills
- [ ] Integration with GitHub Projects
