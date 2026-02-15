# Jira Story Creator Skill

Automatically create detailed Jira Stories from implementation plan markdown files with complete user story format, acceptance criteria, implementation method, and testing method.

## Features

✅ **Intelligent Story Generation**
- Automatically detects story type (infrastructure, backend API, frontend UI)
- Generates appropriate user story format for each type
- Creates detailed acceptance criteria
- Provides step-by-step implementation guidance
- Includes comprehensive testing methods

✅ **Professional Formatting**
- Uses Atlassian Document Format (ADF)
- Proper headings and structure
- Links stories to parent Epics
- Auto-generates relevant labels

✅ **Flexible Input**
- Parses markdown implementation plans
- Extracts tasks from stage sections
- Supports selective stage creation
- Dry-run mode for preview

## Quick Start

### 1. Install Dependencies

```bash
# Python 3.8+ required
python --version
```

### 2. Create Configuration

```bash
cp config.template.json config.json
```

Edit `config.json`:
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

### 3. Run the Skill

```bash
python jira-story-creator.py \
  --plan path/to/implementation-plan.md \
  --config config.json \
  --stages 1,2,3
```

## Usage

### Create Stories for All Stages

```bash
python jira-story-creator.py \
  --plan IMPLEMENTATION-PLAN.md \
  --config config.json
```

### Create Stories for Specific Stages

```bash
python jira-story-creator.py \
  --plan IMPLEMENTATION-PLAN.md \
  --config config.json \
  --stages 1,2,3
```

### Dry Run (Preview)

```bash
python jira-story-creator.py \
  --plan IMPLEMENTATION-PLAN.md \
  --config config.json \
  --stages 1 \
  --dry-run
```

### Custom Epic Prefix

```bash
python jira-story-creator.py \
  --plan IMPLEMENTATION-PLAN.md \
  --config config.json \
  --epic-prefix MYPROJ
```

## Implementation Plan Format

Your markdown file should follow this structure:

```markdown
### Stage 1: Foundation & Authentication (Week 1-2, 80 hours)
**Tasks:**
- [ ] AWS account setup (EC2 t3.medium, S3 buckets, CloudFront)
- [ ] PostgreSQL 15 installation & configuration
- [ ] NGINX installation & SSL setup (Let's Encrypt)
- [ ] Create Backend API Scaffold (Node.js/Express)
- [ ] Implement JWT Verification Middleware
- [ ] Create User Registration Endpoint
- [ ] Create Login/Register UI Components

**Acceptance Criteria:**
- ✅ Users can register with email/password
- ✅ Email verification works
- ✅ Users can log in and receive JWT tokens

---

### Stage 2: User Profile & Onboarding (Week 2-3, 65 hours)
**Tasks:**
- [ ] Goal categories table & seed data
- [ ] User goals table & endpoints
- [ ] Onboarding flow UI (6 steps)
...
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

## Configuration Options

### config.json Structure

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

### Finding Your Story Type ID

```bash
curl -u email:token "https://yourcompany.atlassian.net/rest/api/3/issuetype/project?projectId=YOUR_PROJECT_ID"
```

Look for the Story issue type and note its `id`.

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

Stage 2: User Profile & Onboarding (AURA-2)
  Tasks: 3
  ✓ AURA-29: Create Goal Categories Table
  ✓ AURA-30: Build Onboarding Flow UI - Step 4
  ✓ AURA-31: Implement Onboarding State Tracking

=== Complete ===
Created 14 stories
```

## Automatic Label Assignment

The skill automatically adds relevant labels based on task content:

- **stage-XXX**: Always added (e.g., stage-001, stage-002)
- **backend**: Added for API, service, controller tasks
- **frontend**: Added for UI, component, page tasks
- **database**: Added for table, schema, database tasks
- **testing**: Added for test-related tasks

## Story Structure

Each created story includes:

### User Story
> As a [role], I want to [action] so that [benefit].

### Acceptance Criteria
- Measurable success criteria
- Completion checkpoints
- Quality standards

### Implementation Method
1. Step-by-step technical approach
2. Key decisions and considerations
3. Dependencies and prerequisites

### Testing Method
1. Unit test scenarios
2. Integration test approach
3. Verification steps
4. Expected outcomes

## Troubleshooting

### Error: "Authentication failed"
- Check Jira email and API token in config.json
- Verify instanceUrl is correct

### Error: "Issue type cannot have parent"
- Ensure Story issue type is configured to allow Epic parents
- Go to Jira Settings → Issues → Issue Types → Hierarchy
- Verify Story is a child of Epic

### Stories Not Created
- Check storyTypeId in config.json
- Verify Epic keys exist (e.g., AURA-1, AURA-2)
- Run with --dry-run to see what would be created

### Parsing Issues
- Verify implementation plan follows the expected format
- Check that tasks start with `- [ ]`
- Ensure stage headers use `### Stage X:` format

## Real World Example

### Input: IMPLEMENTATION-PLAN.md
```markdown
### Stage 1: Foundation & Authentication (Week 1-2, 80 hours)
**Tasks:**
- [ ] Install PostgreSQL 15
- [ ] Create User Registration Endpoint
- [ ] Build Login Form Component
```

### Generated Stories:

**AURA-18: Install PostgreSQL 15**
- **User Story:** As a DevOps engineer, I want to install PostgreSQL 15 so that the application has the necessary infrastructure.
- **Acceptance Criteria:**
  - PostgreSQL 15 installed successfully
  - Configuration documented
  - Service is running and accessible
  - Health checks passing
- **Implementation:**
  1. Install PostgreSQL 15: sudo dnf install postgresql15
  2. Initialize database
  3. Configure authentication
  4. Verify installation
  5. Document configuration
- **Testing:**
  1. Connect via psql
  2. Create test database
  3. Verify permissions
  4. Check service status

**AURA-19: Create User Registration Endpoint**
- **User Story:** As a backend developer, I want to create user registration endpoint so that the frontend can register users.
- **Acceptance Criteria:**
  - POST /api/auth/register endpoint created
  - Request/response validated
  - Error handling implemented
  - API documentation updated
  - Tests passing
- **Implementation:**
  1. Create route: POST /api/auth/register
  2. Implement controller logic
  3. Add input validation (Zod/Joi)
  4. Add error handling
  5. Update API documentation
  6. Write unit tests
- **Testing:**
  1. Test with valid payload (expect 201)
  2. Test with invalid email (expect 400)
  3. Test duplicate registration (expect 409)
  4. Verify database record created
  5. Run integration tests

**AURA-20: Build Login Form Component**
- **User Story:** As a user, I want to build login form component so that I can authenticate.
- **Acceptance Criteria:**
  - Login Form component created
  - Responsive design (mobile + desktop)
  - Accessibility compliant
  - User feedback on interactions
  - Loading states shown
- **Implementation:**
  1. Create LoginForm component
  2. Implement form inputs (email, password)
  3. Add form validation
  4. Add loading/error states
  5. Style with TailwindCSS
  6. Add accessibility attributes
  7. Write component tests
- **Testing:**
  1. Render component
  2. Test form submission
  3. Test validation errors
  4. Test responsive design on mobile
  5. Test accessibility

## Advanced Usage

### Custom Story Templates

You can extend the `StoryTemplate` class in the Python script to add custom templates for your specific needs.

### Integration with CI/CD

```yaml
# .github/workflows/create-stories.yml
name: Create Jira Stories

on:
  push:
    paths:
      - 'IMPLEMENTATION-PLAN.md'

jobs:
  create-stories:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Create Stories
        run: |
          python jira-story-creator.py \
            --plan IMPLEMENTATION-PLAN.md \
            --config config.json \
            --stages ${{ github.event.inputs.stages }}
        env:
          JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
```

## Version History

- **1.0.0** (2026-02-14): Initial release
  - Intelligent story type detection
  - Three story templates (infrastructure, backend, frontend)
  - ADF formatting
  - Automatic label assignment
  - Dry-run mode

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify your implementation plan format
3. Test with --dry-run first
4. Check Jira API permissions

## License

MIT License

---

**Created for Auragen AI Project**
**Version:** 1.0.0
**Last Updated:** February 14, 2026
