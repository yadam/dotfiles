---
name: typescript-quality
description: "Design, implement, configure quality tools for, or review TypeScript projects, including libraries, services, CLIs, web apps, and mobile apps. Use for .ts/.tsx changes, TypeScript type and boundary design, Biome configuration, or ESLint migration coverage. Combine automated checks with explicit review of type-safety and semantic gaps; apply framework checks only where relevant."
license: MIT
metadata:
  source: "Adapted from cursor/plugins pstack TypeScript practices and Adam's bun-vite-react-trpc effective ESLint configuration"
---

# TypeScript quality

Use strong type design, automated checks, and explicit semantic review in any TypeScript project. Prefer Biome as the sole linter, formatter, and import organizer for new setups or an authorized migration; retain a separate TypeScript compiler check. Respect existing repository tooling and approved requirements. Applying this skill alone does not authorize removing ESLint, changing dependencies, or migrating a project's configuration.

This skill supplies agent review instructions, not deterministic lint coverage. Never report its review as equivalent to TypeScript ESLint or as a passing CI check.

## Scope and evidence

Read applicable repository instructions, the current task, package scripts, compiler/linter configuration, and relevant domain documentation before changing code. Identify runtime, module system, framework, package boundaries, and generated files. Honor any repository-specific work or recording gate. Do not copy policies or dependencies from another project, or relax requirements to satisfy a check.

When configuring quality tools, read [Biome mapping](references/biome-mapping.md). When writing or reviewing TypeScript, apply relevant checks in [review checks](references/review-checks.md); skip framework checks where that framework is absent. Read [coverage limits](references/coverage-limits.md) when comparing enforcement approaches. Read the full [ESLint coverage inventory](references/eslint-coverage.md) only for migration audits or inherited-rule questions. It records one reference UI configuration, not universal TypeScript policy.

## Type design

- Represent mutually exclusive states with a shared literal discriminant and variant-specific payloads. Derive redundant state where possible. Avoid optional fields that permit contradictory combinations.
- Strengthen types only when justified by actual invariants. Model legitimate empty or missing states honestly. A tuple can express fixed length but cannot prove item uniqueness or make every dynamic index valid. Use runtime validation for properties types cannot prove.
- Separate semantic IDs where accidental interchange is possible. Reuse the existing branding convention and validate at construction. Do not brand every primitive or introduce constructors that merely cast.
- Treat parsed JSON, persisted data, network/process input, external messages, and weakly typed library results as `unknown` until validated. Reuse a runtime schema system if present; derive types from it. Do not add a schema dependency solely to satisfy this skill.
- Prefer control-flow narrowing, accurate annotations, and `satisfies` over assertions. `satisfies` checks assignability, not external data at runtime. Allow `as const`. A necessary branded-type/library assertion must have a local proof and a narrow documented exception, never a file-wide suppression or an `as unknown as T` escape.
- Prove type guards and assertion functions against malformed inputs. TypeScript trusts their declared predicates and does not prove their implementation.
- Make union handling fail compilation when a case is added, using a `never` check or the established exhaustive helper. A default fallback can hide a missing variant. Experimental lint is supplementary.
- Derive related types using schema inference or appropriate utility types. Do not duplicate an authoritative shape, or contort utility types when a new domain concept deserves a named type.
- Prefer named object arguments where same-primitive positional arguments can be swapped. Keep simple established signatures and measured hot paths practical.

## Review and verification

Trace suspicious values through assignments, calls, property access, arguments, and returns to their origin. Inspect casts, suppressions, and untyped boundaries in changed files and affected callers; text matches identify review targets, not violations. Check dependencies against the project's actual architectural boundaries rather than assuming every project has a shared domain layer.

Test production behavior through public interfaces with independently specified expected outcomes. Exercise relevant invalid inputs and invariants. Mock only boundaries a test cannot reasonably exercise. Select evidence appropriate to the project: library/API contracts, CLI output and exit status, web interactions, or native behavior. Component tests alone do not establish build, browser, device, or accessibility behavior. Respect the existing test strategy and task scope; do not add a new test stack solely for this skill.

Run the repository's existing non-mutating lint, TypeScript, and relevant test/build commands when the task permits. Inspect scripts before choosing commands. Do not blindly run `tsc --noEmit` in projects with incompatible build/reference settings; use their documented compiler checks. Do not install tools or enable auto-fixes during a review without scope to do so.

Report concrete findings with file/line, trigger, impact, and the violated check. Separate automated results, agent-reviewed checks, documented exceptions, and unverified areas. If no issues are found, state the scope inspected rather than claiming complete safety. Keep important missing automatic checks visible; a skill can miss them.

## Provenance

Adapted from [pstack TypeScript practices](https://github.com/cursor/plugins/blob/e8d856f0273b42ebafe0ec3546bd645709e7c1b0/pstack/skills/typescript-best-practices/SKILL.md), its patterns and type-system/boundary principles, plus Adam's effective reference ESLint rules. The adaptation is self-contained and does not require other pstack skills. [Upstream MIT notice](LICENSE) is retained. Coverage was assessed against Biome 2.5.15 on October 2, 2026; recheck it when the pinned toolchain changes.
