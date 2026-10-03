# Review checks beyond Biome

Apply checks to changed behavior and affected callers in the actual runtime and framework. R1-R4 and R6 are general checks; apply R5 only when the relevant UI framework is present. These are agent review instructions and may miss defects. They do not recreate an AST linter or compiler-backed ESLint diagnostics. Document narrow exceptions and unverified checks rather than declaring parity.

## R1: Untyped values, assertions, and numeric semantics

Trace `JSON.parse`, weakly typed modules, third-party returns, and inferred `any` through assignments, arguments, calls, member access, and returned values. Put the raw result in `unknown` and validate into a named domain type at the boundary. An annotation such as `const data: RecordData = JSON.parse(text)` is not validation.

Do not invoke or inspect an `any` value before validation. Validate every promised field and invariant. A cast or predicate name does not prove its claim. Review assertion functions, unchecked generic helpers, double casts, non-null assertions, definite assignment, ignored diagnostics, and blanket lint suppressions. Keep necessary platform/branding exceptions narrow and justified by actual validation or a documented library contract.

Check coercions in template strings, arithmetic, unary minus, and comparisons. Reject accidental object-to-string output, promise interpolation, mixed numeric/string operations, and unrelated enum comparisons. Format intentionally with domain-specific functions. `number` alone does not prove a finite integer, nonnegative duration, valid count, or bounded numeric range. Validate those properties when external input requires them.

Keep derived and union types meaningful. Remove redundant/duplicate variants when they obscure handling. Prefer const literals over an unnecessary assertion. Do not use a redundant check as evidence that an external value was validated.

## R2: Total operations, mutation, and control flow

Every returning branch must match the declared result. Do not silence a missing return by widening to `undefined` unless that is a real domain outcome. Make state/action/result unions exhaustive at compilation. Validate arbitrary indexes even for nonempty tuples; the type of a dynamic index can still include `undefined` with `noUncheckedIndexedAccess`.

Respect ownership when mutating input data, props, exported bindings, or shared arrays. `noParameterAssign` only catches parameter rebinding and does not prove immutability. Use the existing ownership convention; intentional mutation of an owned local value or an API designed for mutation can be appropriate. Validate domain invariants where readonly annotations cannot establish them. Do not delete array elements accidentally and leave sparse arrays.

Inspect loop termination and transitions. Awaiting sequential work in a loop can be correct; do not apply the reference config's broad loop ban. Verify the bound or state change that makes a loop terminate. Review dynamically constructed regular expressions for invalid patterns and untrusted input; parser/compiler rejection of invalid syntax does not validate runtime strings. Avoid legacy reflection/prototype manipulation, `arguments.caller/callee`, dynamic evaluation, and unintended constructor side effects in production code. Use ordinary module exports and supported runtime/library APIs.

## R3: Async work, callbacks, and errors

Check promise handling across file/module boundaries, callbacks passed to void-returning APIs, and request/event handlers. An ignored `void promise` expression needs an actual rejection strategy where failure is possible; `void` alone does not catch errors. Avoid async `forEach`. Await only thenables, keep async declarations meaningful, and use `return await` when local `try/catch/finally` behavior requires it.

Do not pass an instance method as an unbound callback unless it does not depend on `this` or is bound. Handle cleanup and late results when work is cancelled, operations are replaced, or components unmount where applicable. Promise executor return values do not settle promises. Propagate useful `Error` values and expected domain failures, and do not swallow errors in empty handlers. Use structured context without logging secrets or full private payloads. Do not introduce telemetry infrastructure solely for compliance.

## R4: Modules, exports, and suppressions

Verify named/default/namespace imports against the real package exports and platform resolution. Review imports for ambiguous default-versus-named access, duplicate side effects, cross-package relative paths, accidental private entries, and mutated exported values. Organize imports with Biome; review any semantic difference from the old ordering rules. Match the actual runtime and module system: Node ESM/CommonJS, Bun, bundler output, or Metro as applicable. Verify package exports and initialization behavior rather than copying another project's resolver assumptions.

For each diagnostic suppression or triple-slash reference, identify the narrow reason and why ordinary types/imports cannot express it. Remove obsolete directives when tooling has been migrated; retain suppressions still required by active tools and evaluate their reasons. A formatter or rule-migration omission is not a reason to restore another linter automatically. Review unused suppression intent even when tooling cannot report it.

## R5: Conditional UI and framework checks

For React projects, check render purity, state/prop mutation, hook order/dependencies, stale closures, ref reads/writes, needless synchronous state updates in effects, and changes to existing memoization. Experimental `useReactCompiler` is useful supplemental evidence, not proof that the whole Hooks preset has been reproduced. Review context value creation for meaningful rerender costs; do not require memoization everywhere.

Keep component definitions stable and use stable semantic item IDs as keys. No direct state mutation, update loops, or deprecated React APIs. New function components are preferred, but do not rewrite working class code without task need. If class/PropTypes code exists, review its lifecycle names, render paths, required/default props, unused state/props/methods, and `this` use. These checks replace relevant behavior from older React rules without importing every class-style preference.

For native UI, use controls' names/roles and selected/disabled state consistently. Verify the supported platforms' screen readers, touch targets, larger text, safe areas, and relevant orientations through tests/device evidence. For DOM components, inspect keyboard support, focus, accessible names, valid elements/attributes, and text/media alternatives. Native components rendered on web still need real-browser checks. For other UI frameworks, inspect their documented lifecycle/reactivity conventions and applicable accessibility checks. Skip this section for projects without UI. No linter establishes that interactions are usable.

## R6: Maintainability and test evidence

Use names that expose domain meaning, derive redundant values, and keep related behavior together. Inspect confusing return conventions, argument positions, casing, anonymous diagnostics, overlarge class/module responsibilities, hidden globals, and surprising require/import timing. Treat the old line-spacing, underscore, class-order, and destructuring preferences as review concerns only when they obscure behavior; formatting belongs to Biome. Do not expand a scoped change to reproduce every historical style rule.

Exercise production behavior through public interfaces with independent examples and invariants. Test malformed input when a parser/guard is introduced. Choose relevant evidence for libraries, services, CLIs, web, or mobile; test visible interactions through accessible controls where UI exists. Mock the unavailable external boundary, not the implementation whose behavior is under test. Check cleanup/disposables when resources are acquired. State what was run, reviewed, and remains unverified. Do not equate an agent checklist with a deterministic gate.
