# Jira Status Update - Implementation Guide

## How This Skill Works

This skill uses a Python script (`jira-update.py`) to update Jira story statuses via the Jira REST API.

## Usage in Claude Code

When the user requests a Jira status update, follow these steps:

### Step 1: Run the Update Script

```bash
cd C:\Users\tcoco\.claude\skills\jira-status-update
python jira-update.py <STORY-ID> <STATUS>
```

**Examples:**
```bash
# Mark story as Done
python jira-update.py AURA-21 Done

# Mark story as In Progress
python jira-update.py AURA-22 "In Progress"

# Using shortcuts
python jira-update.py AURA-23 done      # → Done
python jira-update.py AURA-24 progress  # → In Progress
python jira-update.py AURA-25 complete  # → Done
```

### Step 2: Verify the Update

```bash
# Check the story status in Jira
cd /c/CodeWork/Reversal/repos/AuragenPlan
python update_jira_status.py details <STORY-ID>
```

### Step 3: Report to User

Provide a summary:
```
✅ Jira Updated Successfully!

Story: AURA-21 - Setup NGINX with SSL
Status: To Do → Done
```

## Batch Updates

For multiple stories, run the script in a loop:

```bash
for story in AURA-20 AURA-21 AURA-22; do
  python jira-update.py $story Done
done
```

## Supported Status Values

### Full Status Names
- `Done` - Mark as complete
- `In Progress` - Currently working on
- `Not Needed` - Cancel/skip the story

### Shortcuts (case-insensitive)
- `done`, `complete`, `completed` → `Done`
- `progress`, `started`, `start`, `working` → `In Progress`
- `cancel`, `cancelled`, `skip` → `Not Needed`

## Error Handling

The script will:
1. Validate the story exists
2. Check available transitions
3. Report if the status is already correct
4. Show clear error messages if update fails

## Workflow Integration

### After Completing Work

1. **Run tests**: `npm run test:unit`
2. **Verify passing**: Check test results
3. **Update Jira**:
   ```bash
   python jira-update.py AURA-XX Done
   ```
4. **Verify**: Check story details

### When Starting Work

```bash
python jira-update.py AURA-XX "In Progress"
```

## Credentials

The script uses hardcoded credentials for the Reversal Solutions Jira instance:
- **Base URL**: https://reversalsolutions.atlassian.net
- **Email**: tom.cocotis@reversalsolutions.com
- **Token**: Stored in the script (rotates periodically)

## Troubleshooting

**Script Not Found**
```bash
# Make sure you're in the right directory
cd C:\Users\tcoco\.claude\skills\jira-status-update
```

**Story Not Found**
- Verify the story ID is correct
- Check you have permission to view the story

**Invalid Transition**
- The script will show available transitions
- Use one of the suggested status names

**Authentication Failed**
- Token may have expired
- Update the token in `jira-update.py`

## Testing

Test the script:

```bash
# Get story details
cd /c/CodeWork/Reversal/repos/AuragenPlan
python update_jira_status.py details AURA-21

# Update status
cd C:\Users\tcoco\.claude\skills\jira-status-update
python jira-update.py AURA-21 Done

# Verify update
cd /c/CodeWork/Reversal/repos/AuragenPlan
python update_jira_status.py details AURA-21
```

## Integration with Development Workflow

### Complete Story Implementation Pattern

```python
# 1. Implement feature with TDD
# 2. Run tests
npm run test:unit

# 3. If tests pass, update Jira
python jira-update.py AURA-XX Done

# 4. Verify
python update_jira_status.py details AURA-XX
```

### Verify Stage Progress Pattern

```bash
# Check all Stage 1 stories
for story in AURA-18 AURA-19 AURA-20 AURA-21 AURA-22 AURA-23 AURA-24 AURA-25 AURA-26 AURA-27 AURA-28; do
  echo "=== $story ==="
  python update_jira_status.py details $story | grep -E "Summary|Status"
  echo ""
done
```

## Best Practices

1. **Always verify tests pass** before marking as Done
2. **Check current status first** to avoid unnecessary updates
3. **Use the script** rather than manual Jira updates for consistency
4. **Verify after updating** to ensure the change took effect
5. **Batch updates carefully** - verify each story individually for critical work

## Future Improvements

- [ ] Add test case auto-update (update child test cases)
- [ ] Support bulk operations (multiple stories at once)
- [ ] Add dry-run mode for validation
- [ ] Integrate with git commit hooks
- [ ] Add rollback capability
- [ ] Cache credentials securely

---

**Last Updated**: 2026-02-14
**Version**: 1.0.0
