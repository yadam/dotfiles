# Coverage limits

Biome plus a review skill does not offer full automatic parity with Biome plus the reference ESLint configuration. Keep these distinctions visible during migrations and reviews.

## Checks that remain weaker or absent automatically

- Unsafe inferred/imported `any`: assignment, arguments, calls, member access, and returns. Strict TypeScript permits many operations involving `any`; `noExplicitAny` checks explicit syntax, not all propagation. The reviewed Biome 2.5.15 schema lacks direct counterparts for the five corresponding TypeScript ESLint unsafe rules.
- Other type-aware semantics: restricted template interpolation, unbound instance methods, and some enum/coercion behavior. Consult the actual inventory and compiler options rather than assuming strict mode covers them.
- Related rules with different detection or options: experimental promise, assertion, exhaustiveness, and React Compiler checks are useful, but rule-name correspondence is not option or behavior parity. Validate important allowed/rejected cases with the pinned tools.
- Imports and framework plugins: runtime resolvers, aliases, framework-specific policies, legacy React conventions, and custom/project plugins may differ or have no counterpart. Apply only policies relevant to the current project.
- Enforcement: configured ESLint checks run consistently over selected files in editors/CI. A skill depends on agent invocation, inspected scope, and judgment; it can miss a violation and cannot make CI fail by itself.

For example:

```ts
export function decodeCount(text: string): number {
  const data: { count: number } = JSON.parse(text);
  return data.count + 1;
}
```

`JSON.parse` returns `any`. The annotation does not validate the input, and strict TypeScript accepts the unsafe assignment. The reference `@typescript-eslint/no-unsafe-assignment` rule rejects it. Assign the raw value to `unknown` and validate before use. This example illustrates the semantic gap; it is not a claim that every possible Biome configuration passes the file.

## Interpreting the historical inventory

The 355-rule inventory has 234 official mapped candidates, 28 additional related candidates, and 93 rules without a direct mapped candidate. These counts are availability evidence for one effective UI configuration. They do not mean 93 entirely lost behaviors: syntax/compiler errors, formatting, obsolete style policies, or inapplicable framework checks can account for some rows. Conversely, the mapped counts do not prove selected severities or exact behavioral parity.

The skill adds type-design, boundary-validation, domain-invariant, and test-evidence review that neither linter can fully automate. Those benefits coexist with the loss of deterministic checks. If a missing check becomes essential as an automatic gate, surface that requirement and assess a narrowly scoped static check or the tooling decision with the user; do not silently add another linter or declare the checklist equivalent.

Sources: [TypeScript ESLint unsafe assignment](https://typescript-eslint.io/rules/no-unsafe-assignment/), [Biome migration caveats](https://biomejs.dev/guides/migrate-eslint-prettier/), [versioned schema](https://unpkg.com/@biomejs/biome@2.5.15/configuration_schema.json), and the local effective ESLint inventory.
