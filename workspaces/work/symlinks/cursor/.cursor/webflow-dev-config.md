# Webflow Development Configuration

## Server Restart Times

When making changes to files that render on the server (such as files in `packages/systems/` or `public/js/designer-flux/`), the local dev server takes **1-2 minutes** to restart and be available for testing.

**Important**: After editing server-rendered code, wait for the dev server to fully restart before running Cypress tests. The user will confirm when the server is ready.

## Cypress Test Commands

### Run specific test file
```bash
npm run cypress-run -- --spec "path/to/test.spec.ts"
```

### Run tests in headed mode (visible browser)
```bash
npm run cypress-run -- --headed --spec "path/to/test.spec.ts"
```

### Run a single test by name
```bash
npm run cypress-run -- --spec "path/to/test.spec.ts" --env grep="test name"
```

### Common test paths
- Content Editor tests: `entrypoints/designer/client-ui-tests/content-editor/`
- Localization tests: `entrypoints/designer/client-ui-tests/localization/`
- Dashboard tests: `entrypoints/dashboard/client-ui-tests/`

## Buildkite Configuration

- **org_slug**: `webflow`
- **pipeline_slug**: `webflow`

Use these values when checking build status with Buildkite MCP tools.

## Jest Test Commands

### Run all Jest tests
```bash
npx nx run-many -t test
```

### Run tests for a specific file
```bash
npx nx test --testFile="path/to/file.test.ts"
```

### Run tests matching a pattern
```bash
npx nx test --testPathPattern="pattern"
```
