# Jira Status Update - Quick Usage Guide

## ✅ Skill Now Working!

The jira-status-update skill has been updated and tested. It now properly syncs Jira with your development progress.

## How to Use

### Quick Update Command

```bash
cd C:\Users\tcoco\.claude\skills\jira-status-update
python jira-update.py <STORY-ID> <STATUS>
```

### Examples

**Mark as Done:**
```bash
python jira-update.py AURA-21 Done
```

**Start Working (In Progress):**
```bash
python jira-update.py AURA-22 "In Progress"
# or
python jira-update.py AURA-22 progress
```

**Mark as Not Needed:**
```bash
python jira-update.py AURA-23 "Not Needed"
```

## Supported Status Values

### Exact Transition Names
- `Done` - Complete the story
- `Start Progress` - Begin working (results in "In Progress" status)
- `Not Needed` - Cancel the story

### Shortcuts (automatically mapped)
- `progress`, `In Progress` → `Start Progress`
- `done`, `complete` → `Done`
- `cancel`, `skip` → `Not Needed`

## Batch Update Multiple Stories

```bash
# Update multiple stories to Done
for story in AURA-20 AURA-21; do
  python jira-update.py $story Done
done
```

## Verify Stage Progress

```bash
# Check all Stage 1 stories
cd /c/CodeWork/Reversal/repos/AuragenPlan
for story in AURA-18 AURA-19 AURA-20 AURA-21 AURA-22 AURA-23 AURA-24 AURA-25 AURA-26 AURA-27 AURA-28; do
  echo "=== $story ==="
  python update_jira_status.py details $story | grep -E "Summary|Status"
  echo ""
done
```

## What the Script Does

1. **Connects to Jira** - Uses Reversal Solutions Jira instance
2. **Gets story details** - Shows current status
3. **Checks if update needed** - Skips if already in target status
4. **Transitions the story** - Updates to new status
5. **Verifies update** - Confirms the change

## Output Format

```
[UPDATING] AURA-21 to Done
==================================================

[STORY DETAILS]
  Key: AURA-21
  Summary: Setup NGINX with SSL
  Current Status: To Do
  Type: Story

[TRANSITION] AURA-21...
[SUCCESS] AURA-21 -> Done
[VERIFIED] Status is now 'Done'

==================================================
[COMPLETE] Update Complete!
==================================================

View in Jira: https://reversalsolutions.atlassian.net/browse/AURA-21
```

## Error Handling

**Story Not Found:**
```
[ERROR] Story AURA-99 not found
```

**Invalid Status:**
```
[ERROR] Status 'InvalidStatus' not available for AURA-22
Available: Not Needed, Start Progress, Done
```

**Already in Status:**
```
[OK] Already in 'Done' status
```

## Integration with Development Workflow

### After Completing a Story

```bash
# 1. Run tests
npm run test:unit

# 2. If passing, update Jira
python jira-update.py AURA-XX Done

# 3. Verify
cd /c/CodeWork/Reversal/repos/AuragenPlan
python update_jira_status.py details AURA-XX
```

### Starting a New Story

```bash
python jira-update.py AURA-XX progress
```

## Best Practices

1. ✅ **Always run tests first** before marking Done
2. ✅ **Update immediately** after completing work
3. ✅ **Verify the update** succeeded
4. ✅ **Use batch updates** for multiple stories
5. ✅ **Check stage progress** periodically

## Troubleshooting

**Wrong Directory:**
```bash
# Make sure you're in the skill directory
cd C:\Users\tcoco\.claude\skills\jira-status-update
```

**Python Not Found:**
```bash
# Check Python is installed
python --version
```

**Connection Issues:**
- Check internet connection
- Verify Jira credentials in script (token may expire)

## Recent Updates

- ✅ Removed emoji characters (Windows compatibility)
- ✅ Added status name mapping (In Progress → Start Progress)
- ✅ Improved error messages
- ✅ Added verification step
- ✅ Created comprehensive documentation

## Files

- `jira-update.py` - Main update script
- `skill.md` - Skill documentation
- `IMPLEMENTATION.md` - Implementation details
- `USAGE-GUIDE.md` - This guide

---

**Last Updated**: 2026-02-14
**Status**: ✅ Working and Tested
**Version**: 1.0.1
