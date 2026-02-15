# Jira Project Creator Skill

🤖 **AI-Powered Jira Project Creation** - Automatically generate complete implementation plans and create Jira Epics with dependencies, timelines, and roadmaps from specification documents.

## What's New: AI-Powered Plan Generation

This skill uses **Claude API** to analyze your specification document and automatically generate a comprehensive implementation plan with:
- 12-15 well-structured stages/epics
- Critical feature detection (safety, ML models, compliance)
- Clean sequential dependencies
- Proper timeline distribution

**No manual planning required!** Just provide your spec document and the AI handles the rest.

## Quick Start

### 1. Install Dependencies

```bash
pip install python-docx anthropic
```

### 2. Set Environment Variables

```bash
# Windows
set ANTHROPIC_API_KEY=your-api-key-here

# Linux/Mac
export ANTHROPIC_API_KEY=your-api-key-here
```

Get your API key from: https://console.anthropic.com/settings/keys

### 3. Create Configuration File

Copy `config.template.json` to `config.json` and fill in your details:

```bash
cp config.template.json config.json
```

Edit `config.json`:
- Set your Jira instance URL
- Add your email and API token
- Set the project key
- Configure timeline preferences
- The `anthropic.apiKey` will be loaded from environment variable

### 4. Run the Skill

```bash
python jira-project-creator.py \
  --spec path/to/your-spec.docx \
  --config config.json \
  --dry-run  # Preview first!
```

## Features

✅ **AI-Powered Implementation Planning**
- Uses Claude API to analyze specifications
- Generates 12-15 logical implementation stages
- **Automatically detects critical features:**
  - Safety systems (self-harm detection, crisis management)
  - ML/AI models (voice analysis, sentiment detection)
  - Compliance requirements (HIPAA, security)
  - Infrastructure needs (foundation, database, auth)
- Domain-aware planning (healthcare, fintech, e-commerce)

✅ **Automatic Epic Creation**
- Creates Jira Epic issues from generated stages
- Includes detailed descriptions
- Adds relevant labels and metadata
- Sets proper priorities

✅ **Smart Dependency Detection**
- Infers dependencies between stages
- Creates "blocks" relationships in Jira
- Ensures proper development sequence
- No circular dependencies

✅ **Flexible Timeline Management**
- Timeline compression (e.g., 1 week = 1 day)
- Automatic date calculation
- Start date customization
- Works with compressed schedules

✅ **Complete Metadata**
- Detailed descriptions from AI analysis
- Relevant labels (stage-001, stage-002, etc.)
- Priority levels
- Custom fields (start date, due date)

✅ **Gantt Chart Ready**
- Sets start and due dates for all epics
- Works with Jira Roadmap
- Compatible with Advanced Roadmaps (Plans)
- Visual timeline in Jira

## Usage Examples

### AI-Powered Project Setup (Recommended)

**Step 1: Preview what AI will create (dry run)**
```bash
python jira-project-creator.py \
  --spec AuragenAI-Spec.docx \
  --config config.json \
  --dry-run
```

This will:
- Analyze your specification with Claude AI
- Generate 12-15 implementation stages
- Show you the epics and dependencies it would create
- **No changes to Jira** (safe to test)

**Step 2: Create the project for real**
```bash
python jira-project-creator.py \
  --spec AuragenAI-Spec.docx \
  --config config.json
```

This will create all epics and dependencies in Jira.

### Compressed Timeline (1 week = 1 day)
Perfect for demo projects or rapid prototyping:

```bash
python jira-project-creator.py \
  --spec my-spec.docx \
  --config config.json \
  --compress-timeline 7 \
  --start-date tomorrow
```

This creates a 14-week project as a 14-day sprint.

### Custom Start Date
```bash
python jira-project-creator.py \
  --spec spec.docx \
  --config config.json \
  --start-date 2026-03-01
```

Or use relative dates:
```bash
--start-date tomorrow
```

## How AI Planning Works

### What the AI Analyzes

The skill uses **Claude Sonnet 4.5** to read your specification document and intelligently generate an implementation plan.

**The AI automatically detects:**

1. **Safety & Compliance Features**
   - Self-harm detection systems
   - Crisis intervention workflows
   - Mental health safety protocols
   - Medical/health compliance (HIPAA, etc.)
   - Content moderation needs
   - User safety mechanisms

2. **AI/ML Model Development**
   - Voice analysis models
   - Sentiment analysis systems
   - Emotion detection
   - Open-source ML models
   - Model training pipelines
   - AI recommendation engines

3. **Core Infrastructure**
   - Foundation/infrastructure setup
   - Authentication & authorization
   - Database architecture
   - API development
   - Frontend applications

4. **User-Facing Features**
   - Onboarding flows
   - User profiles
   - Assessment systems
   - Content delivery

5. **Quality & Launch**
   - Testing & QA
   - Security hardening
   - Performance optimization
   - Launch preparation

### AI Planning Guarantees

✅ **Critical features won't be missed** - The AI is prompted to look for domain-specific keywords like "detection", "safety", "ML", "AI", "crisis"

✅ **Proper stage count** - Always generates 12-15 stages (not too granular, not too high-level)

✅ **Clean dependencies** - Sequential dependencies with foundation blocking everything

✅ **Domain-aware** - Adapts to healthcare, fintech, e-commerce, and other specialized domains

### Example: Mental Health App

If your spec mentions:
- "Voice analysis for wellness"
- "Self-harm risk detection"
- "Daily mood assessment"

The AI will create dedicated stages for:
- Open-Source Voice Analysis ML Pipeline
- Mental Health Safety & Crisis Detection
- Daily Assessment System

**The AI understands that safety features deserve dedicated focus.**

## Specification Document Format

Your specification document can be a simple Word document (.docx). The AI will analyze the full content.

### What to Include in Your Spec

### Required Sections

1. **Project Name**
   ```
   Project: Auragen AI Wellness Platform
   ```

2. **Timeline**
   ```
   Timeline: 12-14 weeks
   ```

3. **Stages/Epics**
   ```
   Stage 1: Foundation & Authentication

   Description of what this stage entails...

   Tasks:
   - [ ] Task 1
   - [ ] Task 2

   Timeline: Week 1-2

   ---

   Stage 2: User Profile & Onboarding
   ...
   ```

### Optional Sections

- Dependencies (explicitly stated)
- Acceptance criteria
- Team assignments
- Story points
- Custom fields

## Configuration Options

### config.json Structure

```json
{
  "jira": {
    "instanceUrl": "https://company.atlassian.net",
    "email": "user@company.com",
    "apiToken": "your-token",
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

### Configuration Fields

| Field | Description | Default |
|-------|-------------|---------|
| `compressionFactor` | Days per week (7 = 1:1, 1 = 7:1) | 7 |
| `workDaysPerWeek` | Working days per week | 7 |
| `createPlan` | Create Advanced Roadmaps Plan | true |
| `addDescriptions` | Add detailed descriptions | true |
| `addDependencies` | Infer and create dependencies | true |
| `addLabels` | Add automatic labels | true |

## Getting API Keys

### Anthropic API Key (Required for AI Planning)

1. Go to: https://console.anthropic.com/settings/keys
2. Sign in or create an account
3. Click **"Create Key"**
4. Give it a name (e.g., "Jira Project Creator")
5. Copy the key (starts with `sk-ant-...`)
6. Set it as an environment variable:

**Windows:**
```bash
set ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
```

**Linux/Mac:**
```bash
export ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
```

Or add to your shell profile (~/.bashrc, ~/.zshrc):
```bash
export ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
```

⚠️ **Never commit your API key to version control!**

**Cost:** Uses Claude Sonnet 4.5 (~$3 per 1M input tokens, $15 per 1M output tokens)
- Typical spec analysis: ~$0.10-0.50 per project
- The AI-generated plans save hours of manual work

### Jira API Token (Required for Jira Integration)

1. Go to: https://id.atlassian.com/manage-profile/security/api-tokens
2. Click **"Create API token"**
3. Give it a name (e.g., "Jira Project Creator")
4. Copy the token
5. Paste it into `config.json`

⚠️ **Never commit your `config.json` with real credentials!**

## Dependency Detection Logic

The skill automatically infers dependencies using these rules:

1. **Sequential Dependencies**
   - Each stage depends on the previous stage

2. **Foundation Rule**
   - Stages with keywords "foundation", "infrastructure", "setup" block all others

3. **Keyword-Based**
   - "authentication" → blocks "profile", "user"
   - "database" → blocks stages needing data
   - "api" → blocks "frontend"

4. **Explicit Dependencies**
   - You can specify dependencies in the spec document

## Troubleshooting

### Error: "python-docx not installed"
```bash
pip install python-docx
```

### Error: "Authentication failed"
- Check your Jira email and API token
- Ensure the token is valid and not expired
- Verify the instance URL is correct

### Error: "Project not found"
- The project key must exist in Jira first
- Create the project in Jira before running the skill

### Epics created but no dependencies
- Check if `addDependencies` is true in config
- Verify the stages have proper sequencing in the spec

### Wrong dates
- Check `startDate` in config
- Verify `compressionFactor` is set correctly
- Ensure date format is YYYY-MM-DD

## Advanced Usage

### Custom Dependency Rules

Edit the `infer_dependencies` method in `jira-project-creator.py`:

```python
def infer_dependencies(self, stages: List[Dict]) -> Dict[int, List[int]]:
    dependencies = {}

    # Add your custom rules here
    for stage in stages:
        if "testing" in stage["name"].lower():
            # Testing depends on all previous stages
            dependencies[stage["number"]] = [
                s["number"] for s in stages if s["number"] < stage["number"]
            ]

    return dependencies
```

### Export Project Summary

```bash
python jira-project-creator.py \
  --spec spec.docx \
  --config config.json \
  --output project-summary.json
```

## Real World Example: Auragen AI Wellness Platform

Here's what the AI generated from a real specification document for a mental health/wellness app:

### Specification Input
- 30-page Word document describing a voice analysis wellness platform
- Features: daily assessments, voice recording, AI recommendations, progress tracking
- Safety requirements: self-harm detection, crisis management
- ML requirements: open-source voice analysis model

### AI-Generated Output (13 Stages)

```
STAGE-001: Foundation & Infrastructure Setup
STAGE-002: Database Schema & Core Models
STAGE-003: Authentication & User Management
STAGE-004: Frontend Foundation & User Onboarding
STAGE-005: Daily Assessment System
STAGE-006: Device Session Logging & Manual Tracking
STAGE-007: Open-Source Voice Analysis ML Pipeline ✅
STAGE-008: AI Recommendation Engine (Claude API Integration)
STAGE-009: Second-Level AI & Progress Analytics
STAGE-010: Audio Content Management & Streaming
STAGE-011: Mental Health Safety & Crisis Detection ✅
STAGE-012: Admin Dashboard & Content Moderation
STAGE-013: Testing, Security Hardening & Launch Preparation
```

### What the AI Caught

✅ **Explicit open-source ML stage** (Stage 7) - Not hidden in generic "voice" stage
✅ **Dedicated safety stage** (Stage 11) - Critical for mental health apps
✅ **Proper sequencing** - Foundation first, ML models before AI integration, safety before launch
✅ **13 manageable stages** - Not too granular (25+) or too high-level (5-8)

### Dependencies Created

- Foundation (Stage 1) blocks everything
- Each stage blocks the next (sequential)
- No circular dependencies
- Clean Gantt chart in Jira

### Result

All 13 epics created in Jira with:
- Detailed descriptions
- Start and due dates
- Clean dependency chain
- Ready for team to start work

**Time saved:** ~4-6 hours of manual planning work

## Roadmap

### Completed Features ✅

- [x] **AI-powered implementation plan generation** using Claude
- [x] **Smart dependency detection** with Claude API
- [x] **Domain-aware planning** (healthcare, fintech, etc.)
- [x] **Critical feature detection** (safety, ML, compliance)
- [x] **Automatic Epic creation** with descriptions and metadata
- [x] **Timeline management** with compression support
- [x] **Gantt chart generation** in Jira

### Future Enhancements

- [ ] Auto-create Stories under each Epic (with AI task breakdown)
- [ ] Support for PDF and Markdown specs
- [ ] Story point estimation using AI
- [ ] Team assignment based on skill matching
- [ ] Integration with GitHub Projects
- [ ] Slack notifications for epic creation
- [ ] Custom field mapping (configurable)
- [ ] Multi-project support (batch creation)
- [ ] Export to other project management tools (Asana, Monday.com)
- [ ] AI-powered risk analysis per stage
- [ ] Automatic sprint planning suggestions

## Contributing

Feel free to extend this skill:
1. Add support for more document formats
2. Improve dependency detection logic
3. Add custom field mappings
4. Create Stories automatically
5. Integrate with other tools

## License

MIT License - Use freely in your projects!

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the specification document format
3. Verify your Jira permissions
4. Check the Jira API documentation

---

## Quick Reference

### One-Line Setup
```bash
pip install python-docx anthropic && \
export ANTHROPIC_API_KEY=your-key && \
cp config.template.json config.json
```

### One-Line Usage (Dry Run)
```bash
python jira-project-creator.py --spec spec.docx --config config.json --dry-run
```

### One-Line Usage (Create Project)
```bash
python jira-project-creator.py --spec spec.docx --config config.json
```

### Key Command-Line Options
| Option | Description | Example |
|--------|-------------|---------|
| `--spec` | Path to specification .docx | `--spec AuragenAI-Spec.docx` |
| `--config` | Path to config JSON | `--config config.json` |
| `--dry-run` | Preview without creating | `--dry-run` |
| `--compress-timeline` | Compression factor (1-7) | `--compress-timeline 7` |
| `--start-date` | Project start date | `--start-date 2026-03-01` |

---

**Created for the Auragen AI project**
**Version:** 2.0 (AI-Powered)
**Last Updated:** February 14, 2026
