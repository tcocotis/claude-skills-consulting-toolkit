# Jira Status Update - Examples

## Example 1: Complete a Single Story

**Scenario:** Just finished implementing AURA-26 (Login Endpoint) and all tests pass.

**Command:**
```
Use jira-status-update to mark AURA-26 as Done
```

**What Happens:**
1. Fetches AURA-26 details from Jira
2. Finds test cases: AURA-73, AURA-74, AURA-75
3. Transitions AURA-26 to "Done"
4. Transitions all 3 test cases to "Done"
5. Shows summary

**Output:**
```
🔄 Updating AURA-26 to Done

Story: AURA-26 - Create Login Endpoint with MFA
  Current Status: In Progress

Found 3 test cases:
  - AURA-73: TC-016 - Login with valid credentials
  - AURA-74: TC-017 - Login with invalid credentials
  - AURA-75: TC-018 - MFA code verification

✅ Updates Complete
  Story: ✓ AURA-26 → Done
  Test Cases: ✓ 3/3 updated

Time: 2.1 seconds
```

---

## Example 2: Start Working on a Story

**Scenario:** About to start implementing AURA-27.

**Command:**
```
Use jira-status-update to mark AURA-27 as In Progress
```

**What Happens:**
1. Transitions AURA-27 to "In Progress"
2. Shows confirmation
3. Does NOT update test cases (they stay in To Do)

**Output:**
```
✅ AURA-27 moved to In Progress
```

---

## Example 3: Batch Update Multiple Stories

**Scenario:** Completed AURA-24, AURA-25, and AURA-26 today.

**Command:**
```
Use jira-status-update to mark AURA-24, AURA-25, AURA-26 as Done
```

**What Happens:**
1. Processes AURA-24:
   - Story → Done
   - 4 test cases → Done
2. Processes AURA-25:
   - Story → Done
   - 3 test cases → Done
3. Processes AURA-26:
   - Story → Done
   - 3 test cases → Done
4. Shows combined summary

**Output:**
```
📦 Batch Update: 3 stories

Processing AURA-24...
  ✓ Story → Done
  ✓ 4 test cases → Done

Processing AURA-25...
  ✓ Story → Done
  ✓ 3 test cases → Done

Processing AURA-26...
  ✓ Story → Done
  ✓ 3 test cases → Done

✅ Batch Complete
  Stories: 3 updated
  Test Cases: 10 updated
  Total: 13 items

Time: 5.8 seconds
```

---

## Example 4: Using Shortcuts

**Commands with shortcuts:**

```
Use jira-status-update to complete AURA-26
```
→ Translates to "mark AURA-26 as Done"

```
Use jira-status-update to start AURA-27
```
→ Translates to "mark AURA-27 as In Progress"

```
Use jira-status-update to skip AURA-28
```
→ Translates to "mark AURA-28 as Not Needed"

---

## Example 5: Error - Story Not Found

**Command:**
```
Use jira-status-update to mark AURA-999 as Done
```

**Output:**
```
❌ Error: Story AURA-999 not found in Jira

Double-check the story key and try again.
```

---

## Example 6: Error - Invalid Transition

**Command:**
```
Use jira-status-update to mark AURA-26 as Done
```

**When story is already Done:**

**Output:**
```
ℹ️  AURA-26 is already Done

Current status: Done
No update needed.
```

---

## Example 7: Partial Failure

**Command:**
```
Use jira-status-update to mark AURA-26 as Done
```

**When one test case fails to update:**

**Output:**
```
⚠️  Partial Success for AURA-26

Story: ✓ Updated to Done

Test Cases:
  ✓ AURA-73 → Done
  ✓ AURA-74 → Done
  ❌ AURA-75 → Failed (permission denied)

Action Needed:
  Manually update AURA-75 or contact Jira admin
```

---

## Example 8: Check Status (Dry Run)

**Command:**
```
Use jira-status-update to check status of AURA-24, AURA-25, AURA-26
```

**Output:**
```
📊 Status Check

AURA-24: JWT Middleware Implementation
  Status: Done ✅
  Test Cases: 4/4 Done

AURA-25: User Registration Validation
  Status: Done ✅
  Test Cases: 3/3 Done

AURA-26: Login Endpoint with MFA
  Status: In Progress ⏳
  Test Cases: 0/3 Done (3 To Do)

Summary:
  2 stories complete
  1 story in progress
```

---

## Example 9: Update Test Cases Only

**Command:**
```
Use jira-status-update to mark test cases for AURA-26 as Done
```

**What Happens:**
1. Finds all test cases for AURA-26
2. Updates only the test cases
3. Leaves story status unchanged

**Output:**
```
🔄 Updating test cases for AURA-26

Story: AURA-26 (status unchanged: In Progress)

Test Cases:
  ✓ AURA-73 → Done
  ✓ AURA-74 → Done
  ✓ AURA-75 → Done

✅ 3 test cases updated
```

---

## Example 10: Integration with TDD Workflow

**Full workflow:**

```bash
# 1. Start story
Use jira-status-update to start AURA-27

# 2. Implement with TDD
Use tdd-test-case to implement TC-019 to TC-021

# 3. Verify tests pass
cd backend && npm run test:unit
# Output: 53/53 tests passing ✅

# 4. Mark complete
Use jira-status-update to complete AURA-27
```

**Result:**
- Story tracked through entire lifecycle
- Jira always reflects actual status
- Test cases automatically updated
- Clear audit trail

---

## Common Patterns

### Daily Workflow
```
Morning:
  Use jira-status-update to start AURA-27

Throughout day:
  # Development and testing

End of day:
  Use jira-status-update to complete AURA-27
```

### Sprint Completion
```
# Mark all completed stories
Use jira-status-update to mark AURA-24, AURA-25, AURA-26, AURA-27 as Done

# Mark postponed stories
Use jira-status-update to mark AURA-28 as To Do
```

### Code Review Integration
```
# After code review approval
Use jira-status-update to complete AURA-26
```

---

## Troubleshooting Examples

### Problem: Transition Not Available

**Error:**
```
❌ Cannot transition AURA-26 to "Done"
Available transitions: Not Needed

Current status: To Do
```

**Solution:**
Need to go through "In Progress" first:
```
Use jira-status-update to start AURA-26
# ... do work ...
Use jira-status-update to complete AURA-26
```

### Problem: Test Case Mismatch

**Scenario:** Test cases have different workflow than story

**Output:**
```
⚠️  Warning: Different workflows detected

Story AURA-26: Done ✓
Test Cases:
  ✓ AURA-73: Done
  ✓ AURA-74: Done
  ⚠️  AURA-75: Cannot transition (different workflow)

Manually check AURA-75
```

---

## Success Metrics

After using this skill, you should see:

**In Jira:**
- ✅ Story status updated
- ✅ All test cases updated
- ✅ Accurate progress tracking
- ✅ Clear audit trail

**In Development:**
- ✅ Jira matches actual progress
- ✅ No manual Jira updates needed
- ✅ Time saved on project management
- ✅ Better visibility for team

---

## Tips

1. **Update Immediately**: Mark stories Done right after tests pass
2. **Batch Related Work**: Update multiple stories together
3. **Use Shortcuts**: "complete" is faster than "mark as Done"
4. **Check First**: Verify tests pass before updating
5. **Track Progress**: Use status checks to monitor sprint progress
