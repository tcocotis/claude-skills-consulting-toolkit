---
skill_name: tdd-test-case
description: Implement test cases using Test-Driven Development (RED-GREEN-REFACTOR cycle). Use this skill when the user wants to implement a feature with TDD, create test cases, write tests first, implement TC-XXX test cases, or follow test-driven development. Triggers include "implement with TDD", "write tests first", "implement TC-", "create test cases", "TDD approach", "RED-GREEN-REFACTOR", "test-first development".
version: 1.0.0
author: Claude
tags: [tdd, testing, jest, vitest, development, test-first]
---

# TDD Test Case Implementation

Implements test cases following the Test-Driven Development methodology with the RED-GREEN-REFACTOR cycle.

## Auto-Invocation Triggers

This skill should be automatically invoked when the user:
- Wants to **implement a feature with TDD** or **test-driven development**
- Says "**write tests first**" or "**test-first approach**"
- Mentions **"implement TC-XXX"** (any test case ID like TC-001, TC-016, etc.)
- References "**RED-GREEN-REFACTOR**" or "**TDD cycle**"
- Wants to **create test cases**, **write failing tests**, or **implement tests**
- Says "**use TDD**", "**follow TDD**", or "**TDD approach**"
- Wants to **implement test coverage** for a feature

**Keywords:** implement TC-, TDD, test-driven development, write tests first, RED-GREEN-REFACTOR, test cases, failing tests, test-first, test coverage

## What This Skill Does

1. **RED Phase**: Writes failing tests first based on test case requirements
2. **GREEN Phase**: Implements minimum code to make tests pass
3. **REFACTOR Phase**: Cleans up code while keeping tests green
4. **Verification**: Runs all tests to ensure no regressions
5. **Documentation**: Updates test case status and generates summary

## When to Use This Skill

- Implementing new features with TDD approach
- Creating test cases from Jira tickets
- Setting up unit, integration, or E2E tests
- Following strict test-first development

## Usage

```
Use the tdd-test-case skill to implement [test case ID or feature description]
```

**Examples:**
- "Use tdd-test-case to implement TC-009 JWT token generation"
- "Use tdd-test-case to implement user registration validation"
- "Use tdd-test-case to implement TC-013 through TC-015"

## What You Need to Provide

- **Test Case ID** (e.g., TC-009) or **Feature Description**
- **Jira Story ID** (optional, e.g., AURA-62)
- **Test Layer** (unit, integration, or e2e)
- **Test Location** (backend or frontend)

## What the Skill Does

### Phase 1: Analysis & Setup (RED Preparation)
- Fetches test case details from Jira (if ID provided)
- Identifies test file location (backend/frontend, unit/integration/e2e)
- Checks if test file exists or creates new one
- Reviews acceptance criteria and requirements

### Phase 2: RED - Write Failing Tests
- Creates test file with proper structure:
  - Jira references (story, test cases, layer)
  - Test description and type (positive/negative/security/edge case)
  - Arrange-Act-Assert structure
  - Proper imports and setup/teardown
- Writes comprehensive test cases covering:
  - Happy path (positive tests)
  - Error cases (negative tests)
  - Edge cases
  - Security validations (if applicable)
- Runs tests to verify they **FAIL**
- Shows clear failure messages

### Phase 3: GREEN - Make Tests Pass
- Implements minimum code to pass tests:
  - Creates service/component/function
  - Adds necessary imports and types
  - Implements core logic
  - Handles errors appropriately
- Runs tests iteratively until all **PASS**
- Fixes type errors and compilation issues
- Shows passing test results

### Phase 4: REFACTOR - Clean Up Code
- Reviews implementation for:
  - Code duplication
  - Naming clarity
  - Type safety
  - Documentation completeness
  - Performance concerns
- Refactors if needed while keeping tests green
- Runs tests again to verify no regressions

### Phase 5: Verification & Summary
- Runs **ALL** tests (not just new ones)
- Verifies no existing tests broke
- Generates implementation summary:
  - Test cases implemented
  - Files created/modified
  - Test results
  - Code coverage (if available)
  - Time taken
- Provides next steps

## Output Format

The skill provides clear visual feedback at each phase:

```
🔴 RED PHASE: Writing Failing Tests
  ✓ Created test file: src/services/jwt.service.test.ts
  ✓ Wrote 4 test cases (TC-009 to TC-012)
  ✓ Running tests...
  ✗ Tests FAILING as expected ✓

🟢 GREEN PHASE: Making Tests Pass
  ✓ Created implementation: src/services/jwt.service.ts
  ✓ Running tests...
  ✓ All 4 tests PASSING

🔵 REFACTOR PHASE: Cleaning Up
  ✓ Code review complete
  ✓ No refactoring needed
  ✓ Tests still passing

✅ VERIFICATION: All Tests
  ✓ 16/16 tests passing
  ✓ No regressions detected

📊 SUMMARY
  Test Cases: TC-009, TC-010, TC-011, TC-012
  Files Created: 2 (1 test, 1 implementation)
  Time: ~15 minutes
  Status: ✅ COMPLETE
```

## Best Practices

The skill follows TDD best practices:

1. **Test First**: Always writes tests before implementation
2. **Minimal Implementation**: Only adds code needed to pass tests
3. **One Test at a Time**: Can implement tests incrementally
4. **Clear Failure Messages**: Ensures test failures are understandable
5. **No Skipping RED**: Verifies tests actually fail first
6. **Regression Testing**: Runs all tests after changes
7. **Clean Code**: Refactors without changing behavior
8. **Documentation**: Includes Jira references and descriptions

## Test File Structure

Tests created by this skill follow this structure:

```typescript
/**
 * JIRA: EPIC-XXX, Story: AURA-YY
 * Test Cases: TC-XXX to TC-YYY
 * Layer: N (Unit/Integration/E2E)
 *
 * [Feature Description]
 */

import { ServiceName } from './service-name';

describe('Feature Name', () => {
  let service: ServiceName;

  beforeEach(() => {
    // Setup before each test
    service = new ServiceName();
  });

  afterEach(() => {
    // Cleanup after each test
  });

  /**
   * Test Case: TC-XXX
   * Type: Positive
   * Description: [What this test validates]
   */
  it('TC-XXX: should [expected behavior]', () => {
    // Arrange
    const input = 'test data';

    // Act
    const result = service.method(input);

    // Assert
    expect(result).toBe('expected');
  });
});
```

## Integration with Jira

If Jira test case IDs are provided, the skill:
- Fetches test case details from Jira
- Reads acceptance criteria
- Identifies parent story
- Uses test case description for test names
- Can update test case status after completion (optional)

## Supported Test Types

### Backend Tests (Jest)
- **Unit Tests**: `backend/src/**/*.test.ts`
- **Integration Tests**: `backend/tests/integration/**/*.test.ts`
- **Command**: `npm run test:unit` or `npm run test:integration`

### Frontend Tests (Vitest)
- **Unit Tests**: `frontend/src/**/*.test.tsx`
- **Component Tests**: `frontend/tests/unit/**/*.test.tsx`
- **Command**: `npm run test:unit`

### E2E Tests (Playwright)
- **E2E Tests**: `frontend/tests/e2e/**/*.spec.ts`
- **Command**: `npm run test:e2e`

## Error Handling

The skill handles common issues:
- Missing dependencies (suggests installation)
- Type errors (helps resolve TypeScript issues)
- Test framework configuration problems
- Existing tests breaking (shows diff and suggests fixes)
- Compilation errors (provides clear error messages)

## Example Session

```
User: Use tdd-test-case to implement TC-009 JWT token generation
