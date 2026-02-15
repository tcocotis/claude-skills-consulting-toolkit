# TDD Test Case Implementation - Examples

## Example 1: Simple JWT Token Generation (What We Just Did)

**Input:**
```
Use tdd-test-case to implement TC-009 JWT token generation
```

**What Happened:**
1. Fetched AURA-62 from Jira (TC-009: Test JWT token generation)
2. Created `backend/src/services/jwt.service.test.ts` with 4 tests
3. Ran tests → Failed (RED phase ✓)
4. Created `backend/src/services/jwt.service.ts` 
5. Implemented JwtService class with generateTokens() and verifyToken()
6. Ran tests → Passed (GREEN phase ✓)
7. Reviewed code → Clean (REFACTOR phase ✓)
8. Ran all tests → 16/16 passing

**Result:**
- 4 test cases implemented (TC-009 to TC-012)
- 2 files created (test + implementation)
- All tests passing
- Time: ~15 minutes

---

## Example 2: Multiple Related Test Cases

**Input:**
```
Use tdd-test-case to implement TC-013, TC-014, and TC-015 for user registration validation
```

**What Would Happen:**
1. Fetches AURA-67, AURA-68, AURA-69 from Jira
2. Creates `backend/src/services/registration.validation.test.ts`
3. Writes 3 test cases:
   - TC-013: Valid registration data
   - TC-014: Invalid password formats
   - TC-015: Duplicate email prevention
4. Implements validation logic to pass all tests
5. Verifies no regressions

---

## Example 3: Test Case Range

**Input:**
```
Use tdd-test-case to implement TC-200 through TC-202 for database integration tests
```

**What Would Happen:**
1. Fetches test cases TC-200, TC-201, TC-202
2. Identifies these are Layer 2 (integration tests)
3. Creates `backend/tests/integration/database/setup.test.ts`
4. Checks Docker is running (PostgreSQL + Redis)
5. Writes integration tests with actual database
6. Implements database setup logic
7. Runs integration tests

---

## Example 4: Feature Without Jira ID

**Input:**
```
Use tdd-test-case to implement password strength validation for backend
```

**What Would Happen:**
1. Asks for clarification on requirements (or uses common password rules)
2. Creates `backend/src/services/password.validator.test.ts`
3. Writes tests for:
   - Minimum length (8 chars)
   - Must have uppercase
   - Must have lowercase
   - Must have number
   - Must have special character
4. Implements PasswordValidator class
5. All tests pass

---

## Example 5: Frontend Component Test

**Input:**
```
Use tdd-test-case to implement LoginForm component tests
```

**What Would Happen:**
1. Creates `frontend/src/components/LoginForm.test.tsx`
2. Writes tests for:
   - Component renders correctly
   - Email validation
   - Password validation
   - Form submission
   - Error message display
3. Implements LoginForm component with React Hook Form
4. Uses React Testing Library for assertions
5. All tests pass

---

## Example 6: E2E Test

**Input:**
```
Use tdd-test-case to implement TC-301 complete registration flow E2E test
```

**What Would Happen:**
1. Fetches AURA-72 (TC-301: Complete user registration flow)
2. Creates `frontend/tests/e2e/auth/register.spec.ts`
3. Writes Playwright test for full user journey:
   - Navigate to registration page
   - Fill out form
   - Submit
   - Verify email sent
   - Click verification link
   - Verify user logged in
4. Runs with `npm run test:e2e`
5. Test passes on all browsers (Chromium, Safari, Chrome)

---

## Example 7: Integration Test with External Services

**Input:**
```
Use tdd-test-case to implement TC-213 S3 voice upload integration test
```

**What Would Happen:**
1. Fetches AURA-120 (TC-213: Test voice upload to S3)
2. Checks Docker Compose is running (for LocalStack S3 mock)
3. Creates `backend/tests/integration/voice/s3-upload.test.ts`
4. Writes test with actual S3 upload
5. Implements S3 upload service
6. Verifies file uploaded correctly
7. Cleans up test files after

---

## Example 8: Security Test

**Input:**
```
Use tdd-test-case to implement TC-012 invalid JWT signature test
```

**What Would Happen:**
1. Identifies this is a security test
2. Creates test that attempts to forge JWT with wrong secret
3. Verifies service rejects with proper error message
4. Ensures no security vulnerabilities introduced

---

## Common Patterns

### Backend Unit Test (Jest)
```typescript
// backend/src/services/example.service.test.ts
import { ExampleService } from './example.service';

describe('ExampleService', () => {
  it('TC-XXX: should do something', () => {
    const service = new ExampleService();
    expect(service.doSomething()).toBe('result');
  });
});
```

### Frontend Unit Test (Vitest)
```typescript
// frontend/src/components/Example.test.tsx
import { render, screen } from '@testing-library/react';
import { Example } from './Example';

it('TC-XXX: should render component', () => {
  render(<Example />);
  expect(screen.getByText('Hello')).toBeInTheDocument();
});
```

### Integration Test (Jest + Supertest)
```typescript
// backend/tests/integration/api/example.test.ts
import request from 'supertest';
import app from '../../../src/index';

it('TC-XXX: should return 200 on valid request', async () => {
  const response = await request(app).get('/api/example');
  expect(response.status).toBe(200);
});
```

### E2E Test (Playwright)
```typescript
// frontend/tests/e2e/example.spec.ts
import { test, expect } from '@playwright/test';

test('TC-XXX: user can complete flow', async ({ page }) => {
  await page.goto('/');
  await page.click('button');
  await expect(page.locator('h1')).toHaveText('Success');
});
```

---

## Tips for Success

1. **Start with Unit Tests**: They're fastest and easiest to debug
2. **Use Descriptive Test Names**: `TC-XXX: should do Y when X` format
3. **One Assert Per Test**: Focus each test on one thing
4. **Test Behavior, Not Implementation**: Test what it does, not how
5. **Keep Tests Independent**: Each test should run alone
6. **Use Setup/Teardown**: Clean state before/after each test

---

## Troubleshooting

**Problem**: Tests can't find module
**Solution**: Skill will check imports and create missing files

**Problem**: Type errors in tests
**Solution**: Skill resolves TypeScript issues iteratively

**Problem**: Integration tests fail - Docker not running
**Solution**: Skill checks Docker and provides start command

**Problem**: E2E tests fail - browsers not installed
**Solution**: Skill suggests `npx playwright install`

---

## Success Checklist

After using this skill, you should have:

- ✅ Test file created with proper structure
- ✅ All tests initially failing (RED)
- ✅ Implementation created
- ✅ All tests passing (GREEN)
- ✅ Code refactored if needed (REFACTOR)
- ✅ No regressions in other tests
- ✅ Clear summary of what was implemented
