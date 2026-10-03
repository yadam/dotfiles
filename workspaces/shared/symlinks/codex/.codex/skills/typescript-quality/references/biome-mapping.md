# Biome mapping

This is implementation guidance, not an installed project configuration. Biome 2.5.15 was the npm stable/latest release inspected on October 2, 2026. Confirm the selected version at implementation time and pin its matching schema/lockfile. Follow the project's actual runtime, framework, and compatibility constraints. A migration needs its own authorization and coverage audit.

## Pstack practices and enforcement

| Practice | Tool candidate | Review still required |
| --- | --- | --- |
| Discriminated unions and constructive modeling | TypeScript discriminant narrowing; selected `useExhaustiveSwitchCases` lint | Domain states, legal transitions, and invariants cannot be designed by a generic lint rule |
| Branded primitives | TypeScript branded types | Constructor validation, meaningful separation, and limited assertion exceptions |
| Simplest total types | `strict`, `noUncheckedIndexedAccess`, `noNonNullAssertion` | Legitimate empty states, arbitrary array indexes, and honest result types |
| Unknown external data | `noExplicitAny`; consider `noImplicitAnyLet` | Inferred/imported `any` propagation remains incompletely covered |
| Schemas before guards, boundary validation | TypeScript checks inferred schema types | Actual runtime checks, boundary placement, and invalid-input tests |
| Avoid assertions; prefer satisfies | Nursery `noUnsafeTypeAssertion`, stable `noNonNullAssertion` | The assertion rule allows `as const` but also flags validated brand casts; scope justified exceptions. `satisfies` is not runtime validation |
| Narrowing hierarchy and honest guards | TypeScript narrowing | A predicate may lie; check its implementation and malformed inputs |
| Exhaustive unions | Compiler `never` check; nursery `useExhaustiveSwitchCases` | Ensure a fallback does not silently accept new variants |
| Schema-derived types | `useImportType`, TypeScript utilities/inference | Check ownership and semantic correspondence; no direct complete lint |
| Named object arguments | No direct complete lint | Review confusing same-primitive positions; avoid mandatory rewrites of all signatures |
| Real tests | `noFocusedTests`, `noSkippedTests` as policy warrants | Test actual behavior and boundary mocks; no snapshot/coverage theater |
| Structured diagnostics | Scoped `noConsole` where a project needs it | Event context, privacy, and errors visible to the caller; stdout/stderr may be the CLI contract |

## Core checks

Keep applicable recommended checks, then explicitly select useful additional checks. Do not enable every rule/domain indiscriminately. Treat these names as candidates until behavior fixtures confirm the selected configuration.

- Stable candidates: `noUnusedVariables`, `noUnusedImports`, `noShadow`, `noDoubleEquals`, `useConst`, `useImportType`, `noExplicitAny`, `noNonNullAssertion`, and project-specific `noRestrictedImports`. Scope `noConsole` to a real project policy; allow legitimate CLI, tooling, and test output.
- Project-aware candidates: `noImportCycles`, `noUndeclaredDependencies`, `noUnresolvedImports`. Validate aliases, package exports, monorepo resolution, framework conventions, and runtime-specific extensions before enforcing. Import restrictions express specified boundaries, not every possible indirect architectural dependency.
- Experimental candidates to evaluate individually: `noUnsafeTypeAssertion`, `noFloatingPromises`, `noMisusedPromises`, `useAwaitThenable`, `useExhaustiveSwitchCases`. Explicit activation and meaningful severity are required. Pinning the binary does not prove experimental detection is complete.
- Retain the project's appropriate TypeScript base and a separate compiler check. Prefer `strict` and `noUncheckedIndexedAccess` for new configurations; evaluate `noImplicitReturns` and `exactOptionalPropertyTypes` against library/framework compatibility. Do not silently retrofit stricter options across an existing project outside the task. These are compiler options, not Biome rules.

## Conditional framework checks

For React projects, evaluate stable `useHookAtTopLevel`, `useExhaustiveDependencies`, `useJsxKeyInIterable`, `noArrayIndexKey`, and `noNestedComponentDefinitions`, plus experimental `useReactCompiler`. Validate the selected React version, compiler integration, and generated/framework code before enforcing. Do not apply React policies to non-React projects.

For React Native projects, evaluate experimental `noReactNativeRawText` and `noReactNativeDeepImports`. The React Native domain currently consists of nursery rules, so `reactnative: recommended` alone does not activate them. Scope native rules to native-component files, including shared RN components rendered on web. Use DOM checks for actual DOM files, not a blanket exception for every `.web.tsx` file. Retain an Expo TypeScript base only where Expo is used; validate Metro platform resolution before enforcing import checks.

For other frameworks, inspect their supported tooling and the actual Biome coverage rather than assuming React checks apply. Unsupported framework rules remain visible gaps. Native accessibility, text scaling, and actual browser/device behavior require appropriate tests and review.

Keep Biome as the formatting authority where selected. Run formatting writes before checks read files; CI checks should not rewrite source. Follow the runtime/module system's import-extension requirements, including Node ESM, bundlers, Bun, or Metro as applicable. Allow framework-required exports and justified entry points instead of applying blanket default-export bans.

## Known automatic gaps

The released schema lacks direct `noUnsafeArgument`, `noUnsafeAssignment`, `noUnsafeCall`, `noUnsafeMemberAccess`, and `noUnsafeReturn` equivalents. `noExplicitAny` and strict TypeScript do not establish this coverage. Other compiler-backed ESLint behaviors, inherited options, resolver details, and framework assumptions need explicit assessment. Biome inference and TypeScript ESLint analysis are different implementations. See [coverage limits](coverage-limits.md) and the historical [inventory](eslint-coverage.md).

## Sources

- [Versioned Biome schema](https://unpkg.com/@biomejs/biome@2.5.15/configuration_schema.json), [rule-source mappings](https://biomejs.dev/linter/javascript/sources/), [migration caveats](https://biomejs.dev/guides/migrate-eslint-prettier/)
- [Unsafe assertions](https://biomejs.dev/linter/rules/no-unsafe-type-assertion/), [non-null assertions](https://biomejs.dev/linter/rules/no-non-null-assertion/), [exhaustive switches](https://biomejs.dev/linter/rules/use-exhaustive-switch-cases/)
- [Floating promises](https://biomejs.dev/linter/rules/no-floating-promises/), [native text](https://biomejs.dev/linter/rules/no-react-native-raw-text/), [React Compiler lint](https://biomejs.dev/linter/rules/use-react-compiler/), [console use](https://biomejs.dev/linter/rules/no-console/)
