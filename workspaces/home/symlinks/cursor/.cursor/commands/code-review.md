# Code Review

Check the diff against main, and code review the changes.

This includes:
- Looking for opportunities to simplify the code
- Looking for opportunities to improve readability
- Looking for opportunities to improve consistency
- Looking for opportunities to improve reusability
- Looking for opportunities to reduce nesting
- Looking for opportunities to reduce repetition
- Looking for opportunities to reduce complexity
- Looking for opportunities to improve maintainability
- Looking for opportunities to improve performance
- Looking for security vulnerabilities
- Looking for side effects in other areas of the code
- Looking for opportunities to improve test coverage
- Looking for opportunities to remove unused code
- Looking for opportunities to remove redundant unit tests
- Looking for opportunities to remove redundant end to end tests
- Looking for opportunities to group unit tests into logical groups to improve readability
- Running unit tests around the effected code changes
- Running end to end tests around the effected code changes
- Looking for cy.wait() commands in effected cypress tests and trying to optimize away from them
- Ensuring the tests are semantically correct
- Ensuring the test comments and descriptions are clear and concise
- Ensuring there are no linting errors
- Ensuring there are no TypeScript errors
- Ensuring the changes follow best practices
- Ensuring the changes follow established patterns in the codebase