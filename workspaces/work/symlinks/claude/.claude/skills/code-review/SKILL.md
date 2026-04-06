---
name: code-review
description: Validates the quality of the code and determines if it is ready to be merged. It focuses on correctness, maintainability, and adherence to project standards. Use as a final step when planning, utilizing TODO list, or when the user asks to "review this code".
---

# Code Reviewer

This skill guides the agent in conducting professional and thorough code reviews for both local development and remote Pull Requests.

## Workflow

### 1. Determine Review Target

- **Local Changes**: Compare the state of the current branch including committed, staged, and unstaged changes to the `dev` branch

### 2. In-Depth Analysis

Analyze the code changes based on the following pillars:

- **Correctness**: Does the code achieve its stated purpose without bugs or logical errors?
- Including
  - Ensuring there are no linting errors
  - Ensuring there are no TypeScript errors
- **Maintainability**: Is the code clean, well-structured, and easy to understand and modify in the future? Consider factors like code clarity, modularity, and adherence to established design patterns.
- Including
  - Looking for opportunities to simplify the code
  - Looking for opportunities to improve reusability
  - Looking for opportunities to reduce nesting
  - Looking for opportunities to reduce repetition
  - Looking for opportunities to reduce complexity
  - Looking for opportunities to improve maintainability
  - Looking for side effects in other areas of the code
  - Ensuring the changes follow best practices
  - Ensuring the changes follow established patterns in the codebase
- **Readability**: Is the code well-commented (where necessary) and consistently formatted according to our project's coding style guidelines?
- Including
  - Looking for opportunities to improve readability
  - Looking for opportunities to improve consistency
- **Efficiency**: Are there any obvious performance bottlenecks or resource inefficiencies introduced by the changes?
- Including
  - Looking for opportunities to improve performance
- **Security**: Are there any potential security vulnerabilities or insecure coding practices?
- **Edge Cases and Error Handling**: Does the code appropriately handle edge cases and potential errors?
- **Testability**: Is the new or modified code adequately covered by tests? Suggest additional test cases that would improve coverage or robustness.
- Including
  - Looking for opportunities to improve test coverage
  - Looking for opportunities to remove unused code
  - Looking for opportunities to remove redundant unit tests
  - Looking for opportunities to remove redundant end to end tests
  - Looking for opportunities to group unit tests into logical groups to improve readability
  - Running unit tests around the effected code changes using the command `npx nx test`
  - Running end to end tests around the effected code changes using the command `npm run cypress-run`
  - Looking for cy.wait() commands in effected cypress tests and trying to optimize away from them
  - Ensuring the tests are semantically correct
  - Ensuring the test comments and descriptions are clear and concise

### 3. Provide Feedback

#### Structure

- **Summary**: A high-level overview of the review.
- **Findings**:
  - **Critical**: Bugs, security issues, or breaking changes.
  - **Improvements**: Suggestions for better code quality or performance.
  - **Nitpicks**: Formatting or minor style issues (optional).
- **Conclusion**: Clear recommendation (Approved / Request Changes).

#### Tone

- Be constructive, professional, and friendly.
- Explain _why_ a change is requested.
- For approvals, acknowledge the specific value of the contribution.
