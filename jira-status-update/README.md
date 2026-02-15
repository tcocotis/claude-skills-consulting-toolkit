# Jira Status Update Tool

A Python script for updating Jira stories and their associated test cases. Automatically synchronizes test case statuses when parent story status changes.

## Features

- ✅ Update story status in Jira
- ✅ Automatically find and update all linked test cases
- ✅ Support for subtasks and linked issues
- ✅ Detailed reporting of updates, skips, and failures
- ✅ Status shortcuts (e.g., "done" → "Done", "progress" → "In Progress")
- ✅ Verification of updates

## Installation

1. **Clone this repository**

```bash
git clone https://github.com/tcocotis/jira-project-claude-skills.git
cd jira-project-claude-skills
```

2. **Install Python dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure environment variables**

Copy `.env.example` to `.env` and fill in your Jira credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```bash
JIRA_BASE_URL=https://your-company.atlassian.net
JIRA_EMAIL=your.email@company.com
JIRA_API_TOKEN=your-api-token-here
```

**How to get your Jira API token:**
1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Give it a name (e.g., "Jira Status Update Tool")
4. Copy the token and paste it in your `.env` file

4. **Load environment variables**

**Bash/Linux/Mac:**
```bash
export $(cat .env | xargs)
```

**Windows PowerShell:**
```powershell
Get-Content .env | ForEach-Object {
    $name, $value = $_.split('=')
    Set-Item -Path "env:$name" -Value $value
}
```

**Windows CMD:**
```cmd
for /F "tokens=*" %i in (.env) do set %i
```

## Usage

### Basic Usage

```bash
python jira-update.py <STORY-ID> <STATUS>
```

**Examples:**

```bash
# Mark story and all test cases as Done
python jira-update.py PROJ-123 Done

# Start progress on story and test cases
python jira-update.py PROJ-123 "In Progress"

# Mark as not needed
python jira-update.py PROJ-123 "Not Needed"
```

### Status Shortcuts

Use shortcuts instead of full status names:

```bash
python jira-update.py PROJ-123 done       # → "Done"
python jira-update.py PROJ-123 progress   # → "In Progress"
python jira-update.py PROJ-123 start      # → "In Progress"
python jira-update.py PROJ-123 cancel     # → "Not Needed"
```

### Batch Updates

Update multiple stories at once:

```bash
for story in PROJ-120 PROJ-121 PROJ-122; do
  python jira-update.py $story Done
done
```

## What It Does

1. **Finds Story**: Retrieves story details from Jira
2. **Finds Test Cases**: Discovers all linked test cases (subtasks and linked issues)
3. **Updates Story**: Transitions story to target status
4. **Updates Test Cases**: Transitions each test case to same status
5. **Reports Results**: Shows detailed summary of all updates

## Output Example

```
[UPDATING] PROJ-123 to Done
==================================================

[STORY DETAILS]
  Key: PROJ-123
  Summary: Create Login Endpoint
  Current Status: In Progress
  Type: Story

[FINDING TEST CASES]
  Found 4 test case(s):
    - PROJ-456: TC-001: Test valid login (Status: To Do)
    - PROJ-457: TC-002: Test invalid login (Status: To Do)
    - PROJ-458: TC-003: Test password reset (Status: To Do)
    - PROJ-459: TC-004: Test MFA flow (Status: To Do)

[TRANSITION STORY] PROJ-123...
[SUCCESS] PROJ-123 -> Done
[VERIFIED] Story status is now 'Done'

[UPDATING TEST CASES]
  [TRANSITION] PROJ-456... [OK]
  [TRANSITION] PROJ-457... [OK]
  [TRANSITION] PROJ-458... [OK]
  [TRANSITION] PROJ-459... [OK]

[SUMMARY]
  Story: Updated
  Test Cases: 4 total
    - 4 updated: PROJ-456, PROJ-457, PROJ-458, PROJ-459

==================================================
[COMPLETE] Update Complete!
==================================================

View in Jira: https://your-company.atlassian.net/browse/PROJ-123
```

## Supported Statuses

- **Done** - Mark as completed
- **In Progress** (or "Start Progress") - Currently being worked on
- **To Do** - In backlog
- **Not Needed** - Cancelled or not required

The script automatically detects available transitions for your Jira workflow.

## How Test Cases Are Found

The script looks for test cases in two ways:

1. **Subtasks**: Issues marked as subtasks of the parent story
2. **Linked Issues**: Issues linked with relationships like "tests" or "is tested by"

Any issues with "Test" in the issue type name or keys starting with "TC-" are considered test cases.

## Troubleshooting

### "Missing required environment variables"

Make sure you've:
1. Created a `.env` file with your credentials
2. Loaded the environment variables (see Installation step 4)

### "Status 'X' not available"

The script will show available transitions for your story. Use one of those exact names or check your Jira workflow configuration.

### "Story not found"

- Verify the story key is correct (e.g., PROJ-123, not proj-123)
- Ensure you have permission to view the story
- Check your JIRA_BASE_URL is correct

## Use with Claude Code

This tool is designed to work as a Claude Code skill. Place it in your Claude skills directory:

```
~/.claude/skills/jira-status-update/
```

Then use via Claude:
```
Use jira-status-update to mark PROJ-123 as Done
```

## Contributing

Contributions welcome! This is a personal consulting toolkit maintained by Tom Cocotis.

## License

MIT License - Free to use for personal and commercial projects.

## Author

**Tom Cocotis**
- Consulting: Reversal Solutions, ArcFoundry, and others
- GitHub: [@tcocotis](https://github.com/tcocotis)

---

**Version:** 1.1.0
**Last Updated:** 2026-02-14
