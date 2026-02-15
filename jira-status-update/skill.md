---
skill_name: jira-status-update
description: Update Jira story and test case statuses as development progresses. Use this skill when the user wants to mark a story as Done, update story status, move story to In Progress, complete a story, or sync Jira status. Triggers include "mark as Done", "update status", "complete AURA-", "mark story", "update Jira", "set status to", "story is complete".
version: 1.0.0
author: Claude
tags: [jira, project-management, tracking, workflow, status-update]
---

# Jira Status Update Skill

Automatically updates Jira stories and their associated test cases to reflect development progress.

## Auto-Invocation Triggers

This skill should be automatically invoked when the user:
- Wants to **mark a story as Done** or **complete a story**
- Says "**update AURA-XX status**" or "**mark AURA-XX as Done**"
- Mentions "**complete AURA-**", "**finish story**", or "**done with AURA-**"
- References "**move to In Progress**", "**start story**", or "**working on AURA-**"
- Wants to **update Jira status**, **sync Jira**, or **change story status**
- Says "**mark multiple stories**" or "**batch update stories**"
- After completing work: "**update the Jira ticket**"

**Keywords:** mark as Done, update status, complete AURA-, mark story, update Jira, move to In Progress, story complete, finish story, sync Jira status, batch update

## What This Skill Does

1. **Updates Story Status**: Transitions stories to appropriate status (In Progress, Done, etc.)
2. **Updates Test Cases**: Automatically updates all child test cases
3. **Batch Updates**: Can update multiple stories at once
4. **Verification**: Confirms all updates succeeded
5. **Progress Tracking**: Shows what was updated

## When to Use This Skill

- After completing a story implementation
- When all tests pass for a feature
- When starting work on a story (move to In Progress)
- When batch updating multiple completed stories
- To sync Jira with actual development status

## Usage

```
Use jira-status-update to mark STORY-ID as STATUS
```

**Examples:**
- "Use jira-status-update to mark AURA-26 as Done"
- "Use jira-status-update to mark AURA-18 as In Progress"
- "Use jira-status-update to mark AURA-27, AURA-28, AURA-29 as Done"
- "Use jira-status-update to complete AURA-26"

## What You Need to Provide

- **Story ID(s)**: One or more Jira story keys (e.g., AURA-26)
- **Status**: Target status (Done, In Progress, To Do, etc.)
  - Can use shortcuts: "complete" → "Done", "start" → "In Progress"

## What the Skill Does

### Phase 1: Validation
- Checks that story exists in Jira
- Verifies story is not already in target status
- Confirms valid transition exists
- Identifies all child test cases

### Phase 2: Story Update
- Retrieves available transitions for the story
- Finds the correct transition ID for target status
- Transitions the story
- Verifies story was updated

### Phase 3: Test Cases Update
- Finds all test cases linked to the story
- Transitions each test case to same status
- Tracks success/failure for each
- Reports any issues

### Phase 4: Verification & Report
- Confirms all updates completed
- Shows summary of what was changed
- Provides links to updated items
- Reports any failures

## Output Format

The skill provides clear feedback at each step:

```
🔄 Updating AURA-26 to Done

📋 Story Details:
  Key: AURA-26
  Summary: Create Login Endpoint with MFA
  Current Status: In Progress

🔍 Finding Test Cases...
  Found 3 test cases:
    - AURA-73: TC-016
    - AURA-74: TC-017
    - AURA-75: TC-018

✅ Story Update:
  ✓ AURA-26 → Done

✅ Test Cases Update:
  ✓ AURA-73 → Done
  ✓ AURA-74 → Done
  ✓ AURA-75 → Done

✅ COMPLETE
  Story: 1 updated
  Test Cases: 3 updated
  Total: 4 items

🔗 View in Jira:
  https://your-domain.atlassian.net/browse/AURA-26
```

## Supported Statuses

### Common Transitions
- **To Do**: Initial state
- **In Progress**: Currently being worked on
- **Done**: Completed and verified
- **Not Needed**: Story/test case not required

### Status Shortcuts
- "complete" or "completed" → "Done"
- "start" or "started" or "working" → "In Progress"
- "todo" or "backlog" → "To Do"
- "skip" or "cancel" → "Not Needed"

## Jira Configuration

The skill automatically:
- Detects available transitions for each story
- Maps status names to transition IDs
- Handles custom workflows
- Works with different Jira configurations

**Required:**
- Jira credentials (email + API token)
- API token stored in environment or skill config
- Permission to transition stories and test cases

## Configuration File

Create `.jira-credentials` in skill directory:

```json
{
  "baseUrl": "https://your-domain.atlassian.net",
  "email": "your-email@example.com",
  "apiToken": "your-api-token-here"
}
```

Or use environment variables:
- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`

## Batch Updates

Update multiple stories at once:

```
Use jira-status-update to mark AURA-24, AURA-25, AURA-26 as Done
```

The skill will:
1. Process each story sequentially
2. Update all test cases for each story
3. Show progress for each story
4. Provide combined summary

## Error Handling

The skill handles common issues:

**Story Not Found**
```
❌ Error: AURA-999 not found in Jira
```

**Invalid Transition**
```
❌ Error: Cannot transition AURA-26 to "Done"
Available transitions: In Progress, Not Needed
```

**Partial Failure**
```
⚠️  Partial Success
  Story: ✓ Updated
  Test Cases: ✓ 2 updated, ❌ 1 failed (AURA-75)
  
Check AURA-75 manually
```

**Permission Denied**
```
❌ Error: No permission to transition AURA-26
Contact your Jira administrator
```

## Integration with Development Workflow

### After Completing a Story

1. **Run all tests**:
   ```bash
   npm run test:unit
   ```

2. **Verify tests pass**:
   ```
   All tests passing? ✅
   ```

3. **Update Jira**:
   ```
   Use jira-status-update to mark AURA-26 as Done
   ```

### Starting a New Story

```
Use jira-status-update to mark AURA-27 as In Progress
```

### Batch Completion

After completing multiple stories:
```
Use jira-status-update to mark AURA-24, AURA-25, AURA-26, AURA-27 as Done
```

## Advanced Features

### Dry Run Mode
Preview what would be updated without making changes:
```
Use jira-status-update to preview AURA-26 as Done
```

### Status Check
Check current status of stories:
```
Use jira-status-update to check status of AURA-24, AURA-25, AURA-26
```

### Test Cases Only
Update only test cases, not the story:
```
Use jira-status-update to mark test cases for AURA-26 as Done
```

## Best Practices

1. **Update After Verification**: Only mark as Done after all tests pass
2. **Batch Similar Work**: Update multiple related stories together
3. **Check Before Update**: Verify tests pass first
4. **Document Changes**: Add comments in Jira if needed
5. **Track Progress**: Use status updates to track team progress

## Workflow Integration

### With TDD Skill
```bash
# 1. Implement feature with TDD
Use tdd-test-case to implement TC-016 to TC-018

# 2. Verify all tests pass
npm run test:unit

# 3. Update Jira
Use jira-status-update to mark AURA-26 as Done
```

### Manual Workflow
```bash
# 1. Start story
Use jira-status-update to mark AURA-27 as In Progress

# 2. Implement and test
# ... development work ...

# 3. Complete story
Use jira-status-update to mark AURA-27 as Done
```

## Output Details

### Summary Report
```
📊 Update Summary for AURA-26

Story: Create Login Endpoint with MFA
  Status: In Progress → Done
  Updated: 2026-02-14 14:30:00

Test Cases Updated: 3
  ✓ AURA-73: TC-016 - Login with valid credentials
  ✓ AURA-74: TC-017 - Login with invalid credentials
  ✓ AURA-75: TC-018 - MFA code verification

All Tests Passing: ✅ 41/41 tests

Time Taken: 2.3 seconds
```

## Troubleshooting

**Can't find transition**
- Check available transitions manually in Jira
- Story might have custom workflow
- Use exact status name from Jira

**Test cases not updating**
- Verify test cases exist as subtasks
- Check they have same workflow as story
- May need different transition for test cases

**Slow updates**
- Large number of test cases takes time
- Network latency to Jira API
- Consider batch updates during off-peak hours

## Success Criteria

A successful update results in:
- ✅ Story status updated
- ✅ All test cases updated
- ✅ Verification confirmed
- ✅ Summary report generated
- ✅ No errors or warnings

## Related Skills

- **tdd-test-case**: Implement features with TDD
- **test-runner**: Run automated tests
- **jira-sync**: Full two-way Jira sync

---

**Created**: 2026-02-14
**Last Updated**: 2026-02-14
**Version**: 1.0.0
