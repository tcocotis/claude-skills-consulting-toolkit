# Jira Story Creator - Quick Start

## 1. Copy Config Template

```bash
cd C:\Users\tcoco\.claude\skills\jira-story-creator
cp config.template.json config.json
```

## 2. Edit config.json

Use the same Jira credentials from your jira-project-creator config:

```json
{
  "jira": {
    "instanceUrl": "https://reversalsolutions.atlassian.net",
    "email": "tom.cocotis@reversalsolutions.com",
    "apiToken": "YOUR_TOKEN_HERE",
    "projectKey": "AURA",
    "storyTypeId": "10006"
  }
}
```

## 3. Run for Auragen Project

### Test with Stage 1 Only (Dry Run)

```bash
python jira-story-creator.py \
  --plan C:\CodeWork\Reversal\repos\AuragenPlan\IMPLEMENTATION-PLAN.md \
  --config config.json \
  --stages 1 \
  --dry-run
```

### Create Stories for Stages 1-6

```bash
python jira-story-creator.py \
  --plan C:\CodeWork\Reversal\repos\AuragenPlan\IMPLEMENTATION-PLAN.md \
  --config config.json \
  --stages 1,2,3,4,5,6 \
  --epic-prefix AURA
```

### Create Stories for All Stages

```bash
python jira-story-creator.py \
  --plan C:\CodeWork\Reversal\repos\AuragenPlan\IMPLEMENTATION-PLAN.md \
  --config config.json \
  --epic-prefix AURA
```

## What Gets Created

For each task in your implementation plan, the skill creates a Jira Story with:

### Example Task:
```
- [ ] Install PostgreSQL 15
```

### Generated Story (AURA-XX):

**Summary:** Install PostgreSQL 15

**Description:**

#### User Story
As a DevOps engineer, I want to install PostgreSQL 15 so that the application has the necessary infrastructure.

#### Acceptance Criteria
- PostgreSQL 15 installed successfully
- Configuration documented
- Service is running and accessible
- Health checks passing

#### Implementation Method
1. Install PostgreSQL 15: sudo dnf install postgresql15 postgresql15-server
2. Initialize database: sudo postgresql-setup --initdb
3. Start service: sudo systemctl start postgresql
4. Create database and user
5. Configure pg_hba.conf for local connections

#### Testing Method
1. Connect via psql: psql -U auragen_app -d auragen
2. Create test table and insert data
3. Test connection from Node.js using pg library
4. Verify connection pooling with multiple requests
5. Check systemctl status postgresql

**Labels:** stage-001, database, infrastructure

**Parent:** AURA-1 (Foundation & Authentication Epic)

## Intelligent Story Generation

The skill automatically detects story types and generates appropriate content:

### Infrastructure Stories
- Keywords: install, setup, configure, aws, nginx, postgresql
- Role: DevOps engineer
- Focus: Installation, configuration, service management

### Backend API Stories
- Keywords: endpoint, api, backend, service, controller
- Role: Backend developer
- Focus: API development, validation, error handling

### Frontend UI Stories
- Keywords: ui, component, page, interface, form, button
- Role: User
- Focus: User interaction, responsive design, accessibility

## Tips

1. **Always dry-run first** to see what will be created
2. **Create stages incrementally** (1-2 at a time) rather than all at once
3. **Verify Epic keys exist** in Jira before running
4. **Check story type detection** - adjust task names if needed for better categorization
5. **Review generated stories** in Jira and edit as needed

## Common Issues

### "Epic not found"
- Make sure Epic keys like AURA-1, AURA-2, etc. exist in Jira
- Create Epics first using the jira-project-creator skill

### "Story type cannot have parent"
- Configure Jira hierarchy: Settings → Issues → Issue Types → Hierarchy
- Make sure Story can be a child of Epic

### Missing tasks
- Check implementation plan format
- Tasks must start with `- [ ]`
- Sub-tasks (indented) are currently skipped

## Next Steps

After creating stories:
1. Review in Jira
2. Refine descriptions as needed
3. Add story points
4. Assign to team members
5. Link test cases (see TDD-IMPLEMENTATION-PLAN.md)
