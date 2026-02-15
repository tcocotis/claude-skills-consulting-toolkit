---
name: jira-story-creator
description: Automatically create detailed Jira Stories from implementation plan markdown files with user story format, acceptance criteria, implementation method, and testing method. Use this skill when the user wants to create Jira stories from a plan, populate Jira with stories, generate user stories from tasks, or set up Jira stories for a stage. Triggers include "create stories", "add stories to Jira", "populate Jira", "generate stories from plan", "create Jira tasks", "story creation".
version: 1.0.0
tags: [jira, stories, agile, user-stories, tdd, automation]
---

# Jira Story Creator

Automatically creates detailed Jira Stories from implementation plan markdown files with complete user story format, acceptance criteria, implementation method, and testing method.

## Auto-Invocation Triggers

This skill should be automatically invoked when the user:
- Wants to **create Jira stories** from an implementation plan
- Says "**populate Jira**" or "**add stories to Jira**"
- Mentions "**generate stories from plan**" or "**create stories for stage X**"
- References creating/adding **user stories**, **Jira tasks**, or **Jira issues** from a document
- Wants to **convert implementation plan to Jira**
- Says "**create Jira stories for Stage 1**" or similar stage references

**Keywords:** create stories, add stories, populate Jira, generate stories, Jira tasks, user stories, story creation, implementation plan to Jira, stage stories

## When to Use This Skill

Use this skill when:
- You have a markdown implementation plan with stages and tasks
- User wants to create Jira stories automatically from a plan
- Need to populate a Jira project with user stories
- Starting a new project stage and need stories created
- Converting planning documents into actionable Jira items

## What This Skill Does

### Intelligent Story Generation
- Automatically detects story type (infrastructure, backend API, frontend UI)
- Generates appropriate user story format for each type
- Creates detailed acceptance criteria
- Provides step-by-step implementation guidance
- Includes comprehensive testing methods

### Professional Formatting
- Uses Atlassian Document Format (ADF)
- Proper headings and structure
- Links stories to parent Epics
- Auto-generates relevant labels

### Flexible Input
- Parses markdown implementation plans
- Extracts tasks from stage sections
- Supports selective stage creation
- Dry-run mode for preview

## Usage

```bash
# Create stories for all stages
python jira-story-creator.py \
  --plan IMPLEMENTATION-PLAN.md \
  --config config.json

# Create stories for specific stages
python jira-story-creator.py \
  --plan IMPLEMENTATION-PLAN.md \
  --config config.json \
  --stages 1,2,3

# Dry run (preview without creating)
python jira-story-creator.py \
  --plan IMPLEMENTATION-PLAN.md \
  --config config.json \
  --dry-run
```

## Story Templates

### Infrastructure Stories
**Detected by keywords:** install, setup, configure, infrastructure, aws, nginx, postgresql, redis

**Generated format:**
- **User Story:** "As a DevOps engineer, I want to [task] so that the application has the necessary infrastructure."
- **Acceptance Criteria:** Installation complete, configuration documented, service running, health checks passing
- **Implementation:** Step-by-step setup instructions
- **Testing:** Verification steps and health check commands

### Backend API Stories
**Detected by keywords:** endpoint, api, backend, service, controller

**Generated format:**
- **User Story:** "As a backend developer, I want to [create endpoint] so that the frontend can [access data]."
- **Acceptance Criteria:** Endpoint created, validation working, error handling, API docs updated, tests passing
- **Implementation:** Route creation, controller logic, validation, error handling, testing
- **Testing:** Test with valid/invalid payloads, error cases, database verification, integration tests

### Frontend UI Stories
**Detected by keywords:** ui, component, page, interface, display, form, button

**Generated format:**
- **User Story:** "As a user, I want to [interact with UI] so that I can [accomplish goal]."
- **Acceptance Criteria:** Component created, responsive design, accessibility compliant, user feedback, loading states
- **Implementation:** Component creation, design implementation, validation, styling, accessibility, testing
- **Testing:** Render test, user interactions, validation, responsive design, accessibility checks

## Configuration

Create a `config.json` file:

```json
{
  "jira": {
    "instanceUrl": "https://yourcompany.atlassian.net",
    "email": "your.email@company.com",
    "apiToken": "YOUR_JIRA_API_TOKEN",
    "projectKey": "PROJ",
    "storyTypeId": "10006"
  }
}
```

## Command-Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--plan` | Path to implementation plan (required) | `--plan IMPLEMENTATION-PLAN.md` |
| `--config` | Path to config JSON (required) | `--config config.json` |
| `--stages` | Comma-separated stage numbers | `--stages 1,2,3` |
| `--epic-prefix` | Epic key prefix | `--epic-prefix AURA` |
| `--dry-run` | Preview without creating | `--dry-run` |

## Output Example

```
Parsing implementation plan: IMPLEMENTATION-PLAN.md
Found 6 stages to process

Stage 1: Foundation & Authentication (AURA-1)
  Tasks: 11
  ✓ AURA-18: AWS Infrastructure Setup
  ✓ AURA-19: Install PostgreSQL 15
  ✓ AURA-20: Install Redis 7
  ✓ AURA-21: Setup NGINX with SSL
  ✓ AURA-22: Create AWS Cognito User Pool
  ✓ AURA-23: Create Backend API Scaffold
  ✓ AURA-24: Implement JWT Verification Middleware
  ✓ AURA-25: Create User Registration Endpoint
  ✓ AURA-26: Create Login Endpoint with MFA
  ✓ AURA-27: Create Frontend Scaffold
  ✓ AURA-28: Create Login/Register UI Components

=== Complete ===
Created 11 stories
```

## Automatic Label Assignment

The skill automatically adds relevant labels based on task content:
- **stage-XXX**: Always added (e.g., stage-001, stage-002)
- **backend**: Added for API, service, controller tasks
- **frontend**: Added for UI, component, page tasks
- **database**: Added for table, schema, database tasks
- **testing**: Added for test-related tasks

## Troubleshooting

**Error: "Authentication failed"**
- Check Jira email and API token in config.json
- Verify instanceUrl is correct

**Error: "Issue type cannot have parent"**
- Ensure Story issue type is configured to allow Epic parents
- Go to Jira Settings → Issues → Issue Types → Hierarchy

**Stories Not Created**
- Check storyTypeId in config.json
- Verify Epic keys exist (e.g., AURA-1, AURA-2)
- Run with --dry-run to see what would be created

---

**Version:** 1.0.0
**Created:** February 14, 2026
