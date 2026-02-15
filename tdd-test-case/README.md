# TDD Test Case Implementation Skill

A Claude Code skill that automates Test-Driven Development workflow using the RED-GREEN-REFACTOR cycle.

## Quick Start

```
Use tdd-test-case to implement TC-009 JWT token generation
```

The skill will:
1. 🔴 Write failing tests
2. 🟢 Implement code to pass tests
3. 🔵 Refactor and clean up
4. ✅ Verify no regressions

## What It Does

This skill guides you through the complete TDD cycle for implementing test cases. It handles:

- Writing comprehensive test files with proper structure
- Running tests to verify RED phase (failing tests)
- Implementing minimum code to pass tests (GREEN phase)
- Refactoring code while keeping tests green (REFACTOR phase)
- Running all tests to ensure no regressions
- Generating implementation summaries

## Features

### Automated TDD Workflow
- Follows strict RED-GREEN-REFACTOR methodology
- Verifies tests fail before implementing
- Ensures tests pass after implementation
- Checks for regressions in existing tests

### Jira Integration
- Fetches test case details from Jira tickets
- Uses test case IDs (TC-XXX) for test names
- Links tests to parent stories
- Can update test case status (optional)

### Multi-Framework Support
- **Jest** for backend unit/integration tests
- **Vitest** for frontend unit tests
- **Playwright** for E2E tests
- **React Testing Library** for component tests

### Intelligent Error Handling
- Fixes TypeScript type errors
- Resolves import issues
- Handles test framework configuration
- Provides clear error messages

## Usage Examples

### Single Test Case
```
Use tdd-test-case to implement TC-009 JWT token generation
```

### Multiple Test Cases
```
Use tdd-test-case to implement TC-013, TC-014, and TC-015
```

### Test Case Range
```
Use tdd-test-case to implement TC-200 through TC-205
```

### Feature-Based (No Jira)
```
Use tdd-test-case to implement password validation
```

### With Context
```
Use tdd-test-case to implement user registration validation for backend
```

## File Structure

The skill creates tests following your project structure:

```
backend/
├── src/
│   └── services/
│       ├── jwt.service.ts           # Implementation
│       └── jwt.service.test.ts      # Unit tests
└── tests/
    └── integration/
        └── auth/
            └── jwt.test.ts          # Integration tests

frontend/
├── src/
│   └── components/
│       ├── LoginForm.tsx            # Component
│       └── LoginForm.test.tsx       # Unit tests
└── tests/
    └── e2e/
        └── auth/
            └── login.spec.ts        # E2E tests
```

## Test File Template

Tests follow a consistent structure:

```typescript
/**
 * JIRA: EPIC-XXX, Story: AURA-YY
 * Test Cases: TC-XXX to TC-YYY
 * Layer: N (Unit/Integration/E2E)
 *
 * [Feature Description]
 */

describe('Feature Name', () => {
  /**
   * Test Case: TC-XXX
   * Type: Positive/Negative/Security/Edge Case
   * Description: [What this validates]
   */
  it('TC-XXX: should [expected behavior]', () => {
    // Arrange
    // Act
    // Assert
  });
});
```

## Configuration

The skill automatically detects:
- Project root directory
- Test framework configurations
- TypeScript settings
- Package.json scripts
- Jira credentials (from environment or config)

## Requirements

### For Backend Tests
- Node.js installed
- Jest configured (`jest.config.js`)
- TypeScript configured (`tsconfig.json`)

### For Integration Tests
- Docker installed and running
- `docker-compose.test.yml` present
- PostgreSQL and Redis services configured

### For Frontend Tests
- Vite + Vitest configured
- React Testing Library installed

### For E2E Tests
- Playwright installed (`npm install @playwright/test`)
- Browsers installed (`npx playwright install`)

## Workflow

### Phase 1: Analysis
- Identifies test case requirements
- Checks existing files
- Plans test structure

### Phase 2: RED
- Creates test file
- Writes failing tests
- **Verifies tests FAIL**

### Phase 3: GREEN
- Creates implementation
- **Makes tests PASS**
- Fixes compilation errors

### Phase 4: REFACTOR
- Reviews code quality
- Refactors if needed
- **Keeps tests passing**

### Phase 5: Verification
- Runs ALL tests
- Checks for regressions
- Generates summary

## Output Example

```
🔴 RED PHASE: Writing Failing Tests
  ✓ Created: backend/src/services/jwt.service.test.ts
  ✓ Wrote 4 tests (TC-009 to TC-012)
  ✗ Tests FAILING (expected) ✓

🟢 GREEN PHASE: Making Tests Pass
  ✓ Created: backend/src/services/jwt.service.ts
  ✓ All 4 tests PASSING

🔵 REFACTOR PHASE: Cleaning Up
  ✓ Code reviewed - looks clean
  ✓ No refactoring needed

✅ VERIFICATION: All Tests
  ✓ 16/16 tests passing
  ✓ No regressions

📊 SUMMARY
  Tests: TC-009, TC-010, TC-011, TC-012
  Files: 2 (1 test, 1 implementation)
  Time: ~15 minutes
  Status: ✅ COMPLETE
```

## Best Practices

1. **Start Simple**: Begin with self-contained features
2. **One Feature at a Time**: Don't combine unrelated tests
3. **Watch the RED**: Always verify tests fail first
4. **Minimal Implementation**: Only add code to pass tests
5. **Refactor Confidently**: Tests protect you during refactoring
6. **Run All Tests**: Check for regressions after changes

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Tests can't find module | Skill creates missing files |
| Type errors | Skill resolves TypeScript issues |
| Docker not running | Skill provides start command |
| Browsers not installed | Skill suggests Playwright install |
| Tests still failing | Skill iterates until passing |

## Integration Points

### Works With
- Jira (fetches test cases, can update status)
- Jest (backend unit/integration tests)
- Vitest (frontend unit tests)
- Playwright (E2E tests)
- TypeScript (type-safe implementation)
- React Testing Library (component tests)

### Can Be Combined With
- `test-runner` skill for advanced test execution
- `coverage-report` skill for detailed coverage
- `jira-sync` skill for automatic status updates

## Success Metrics

A successful session results in:
- ✅ All new tests passing
- ✅ No existing tests broken
- ✅ Type-safe implementation
- ✅ Proper error handling
- ✅ Clean, documented code

## Version History

- **1.0.0** (2026-02-14): Initial release
  - Full RED-GREEN-REFACTOR cycle
  - Jest, Vitest, Playwright support
  - Jira integration
  - Multi-test case support

## License

MIT License - Free to use and modify

## Author

Created by Claude as part of the Auragen AI project TDD setup.

## Contributing

To improve this skill:
1. Test with different project structures
2. Report issues or edge cases
3. Suggest additional features
4. Share successful usage patterns

## Support

For questions or issues:
- Check the examples.md file
- Review the skill.md documentation
- Test with a simple case first
