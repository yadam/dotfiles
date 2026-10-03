# Effective ESLint coverage inventory

Read this reference for migration audits, not every routine TypeScript edit. Inventory captured October 2, 2026 by running the existing ESLint installation with `--print-config packages/ui/src/App.tsx` in Adam's local `bun-vite-react-trpc` checkout. It includes inherited presets and the final override order, not just rules written in the file. Configuration SHA-256: `79f6e0a7a5f9a6673f2bf69fed787304481660b3ea5a5f2b5e5ce2ccd35b2a11`.

The effective UI configuration enabled **355 rules**: 234 have official source mappings to names in the published Biome 2.5.15 schema, 28 have additional related candidates, and 93 have no direct mapped candidate. A mapping is availability evidence, not selected configuration or behavioral equivalence. This is an inventory of reference UI policies, not an instruction to enable all of them. Server, library, CLI, test, and configuration-file overrides must be audited separately for each migration. Do not assume this UI inventory captures every rule in every project.

Biome formatting and the TypeScript compiler also catch some cases. Do not count that as complete rule-option parity. Domain applicability, experimental status, resolver behavior, and meaningful severities still need validation. Even a mapped rule can require semantic review under the ordinary review checks.

For missing or partial rules, R1-R6 refer to [review checks](review-checks.md). Retain their behavior as project review checks when applicable. Class/PropTypes, DOM, CommonJS, Vite refresh, and historical style policies apply only where that code exists. Formatter differences, class ordering, naming/spacing preferences, the reference loop bans, and framework-required exports are deliberate contextual adaptations, not hidden claims of equivalent enforcement. Do not create dead code, rewrite modules, or add a linter to reproduce an inapplicable rule.

All rows carry the effective reference severity for traceability; this does not assign project severity. Complete rules are listed so a future audit can detect omissions. The named skill's review is probabilistic and cannot promise it will detect every violation a removed linter would detect.

Sources: [official mapping](https://biomejs.dev/linter/javascript/sources/), [versioned schema](https://unpkg.com/@biomejs/biome@2.5.15/configuration_schema.json), [migration differences](https://biomejs.dev/guides/migrate-eslint-prettier/), and the local effective ESLint output. Manual related candidates are explicitly marked and were checked only for availability, not executed here.

## Checks retained through review

| Reference ESLint rule | Reference severity | Biome 2.5.15 candidate | Coverage/owner |
| --- | --- | --- | --- |
| `no-delete-var` | error | No direct mapped candidate | R2 |
| `no-invalid-regexp` | error | No direct mapped candidate | R2 |
| `no-octal` | error | No direct mapped candidate | R2 |
| `import/namespace` | error | No direct mapped candidate | R4 |
| `import/default` | error | No direct mapped candidate | R4 |
| `import/export` | error | No direct mapped candidate | R4 |
| `import/no-named-as-default` | error | No direct mapped candidate | R4 |
| `import/no-named-as-default-member` | error | No direct mapped candidate | R4 |
| `import/no-duplicates` | error | No direct mapped candidate | R4 |
| `no-new-symbol` | error | No direct mapped candidate | R2 |
| `@typescript-eslint/no-array-delete` | error | No direct mapped candidate | R2 |
| `@typescript-eslint/no-duplicate-type-constituents` | error | No direct mapped candidate | R1 |
| `@typescript-eslint/no-redundant-type-constituents` | error | No direct mapped candidate | R1 |
| `@typescript-eslint/no-unsafe-argument` | error | No direct mapped candidate | R1 |
| `@typescript-eslint/no-unsafe-assignment` | error | No direct mapped candidate | R1 |
| `@typescript-eslint/no-unsafe-call` | error | No direct mapped candidate | R1 |
| `@typescript-eslint/no-unsafe-enum-comparison` | error | No direct mapped candidate | R1 |
| `@typescript-eslint/no-unsafe-member-access` | error | No direct mapped candidate | R1 |
| `@typescript-eslint/no-unsafe-return` | error | No direct mapped candidate | R1 |
| `@typescript-eslint/no-unsafe-unary-minus` | error | No direct mapped candidate | R1 |
| `@typescript-eslint/restrict-template-expressions` | error | No direct mapped candidate | R1 |
| `@typescript-eslint/triple-slash-reference` | error | No direct mapped candidate | R4 |
| `@typescript-eslint/unbound-method` | error | No direct mapped candidate | R3 |
| `@typescript-eslint/ban-tslint-comment` | error | No direct mapped candidate | R4 |
| `@typescript-eslint/class-literal-property-style` | error | No direct mapped candidate | R6 |
| `@typescript-eslint/consistent-indexed-object-style` | error | No direct mapped candidate | R6 |
| `react/display-name` | error | No direct mapped candidate | R5 |
| `react/jsx-no-undef` | error | No direct mapped candidate | R5 |
| `react/jsx-uses-vars` | error | No direct mapped candidate | R5 |
| `react/no-deprecated` | error | No direct mapped candidate | R5 |
| `react/no-find-dom-node` | error | No direct mapped candidate | R5 |
| `react/no-is-mounted` | error | No direct mapped candidate | R5 |
| `react/no-unescaped-entities` | error | No direct mapped candidate | R5 |
| `react/require-render-return` | error | No direct mapped candidate | R5 |
| `lines-between-class-members` | error | No direct mapped candidate | R6 |
| `no-underscore-dangle` | error | No direct mapped candidate | R6 |
| `block-scoped-var` | error | No direct mapped candidate | R2 |
| `camelcase` | error | No direct mapped candidate | R6 |
| `consistent-return` | error | No direct mapped candidate | R2 |
| `func-names` | warning | No direct mapped candidate | R6 |
| `global-require` | error | No direct mapped candidate | R4 |
| `import/newline-after-import` | error | No direct mapped candidate | R4 |
| `import/no-absolute-path` | error | No direct mapped candidate | R4 |
| `import/no-amd` | error | No direct mapped candidate | R4 |
| `import/no-dynamic-require` | error | No direct mapped candidate | R4 |
| `import/no-import-module-exports` | error | No direct mapped candidate | R4 |
| `import/no-mutable-exports` | error | No direct mapped candidate | R4 |
| `import/no-named-default` | error | No direct mapped candidate | R4 |
| `import/no-relative-packages` | error | No direct mapped candidate | R4 |
| `import/no-useless-path-segments` | error | No direct mapped candidate | R4 |
| `import/no-webpack-loader-syntax` | error | No direct mapped candidate | R4 |
| `import/order` | error | No direct mapped candidate | R4 |
| `lines-around-directive` | error | No direct mapped candidate | R6 |
| `new-cap` | error | No direct mapped candidate | R6 |
| `no-buffer-constructor` | error | No direct mapped candidate | R2 |
| `no-caller` | error | No direct mapped candidate | R2 |
| `no-extra-bind` | error | No direct mapped candidate | R3 |
| `no-iterator` | error | No direct mapped candidate | R2 |
| `no-new-object` | error | No direct mapped candidate | R2 |
| `no-new-require` | error | No direct mapped candidate | R2 |
| `no-path-concat` | error | No direct mapped candidate | R4 |
| `no-promise-executor-return` | error | No direct mapped candidate | R3 |
| `no-restricted-exports` | error | No direct mapped candidate | R4 |
| `no-restricted-syntax` | error | No direct mapped candidate | R6 |
| `no-return-await` | error | No direct mapped candidate | R3 |
| `no-unreachable-loop` | error | No direct mapped candidate | R2 |
| `spaced-comment` | error | No direct mapped candidate | R6 |
| `strict` | error | No direct mapped candidate | R6 |
| `unicode-bom` | error | No direct mapped candidate | R6 |
| `react/jsx-filename-extension` | error | No direct mapped candidate | R5 |
| `react/default-props-match-prop-types` | error | No direct mapped candidate | R5 |
| `react/destructuring-assignment` | error | No direct mapped candidate | R5 |
| `react/forbid-foreign-prop-types` | warning | No direct mapped candidate | R5 |
| `react/forbid-prop-types` | error | No direct mapped candidate | R5 |
| `react/jsx-no-constructed-context-values` | error | No direct mapped candidate | R5 |
| `react/no-access-state-in-setstate` | error | No direct mapped candidate | R5 |
| `react/no-arrow-function-lifecycle` | error | No direct mapped candidate | R5 |
| `react/no-did-update-set-state` | error | No direct mapped candidate | R5 |
| `react/no-invalid-html-attribute` | error | No direct mapped candidate | R5 |
| `react/no-redundant-should-component-update` | error | No direct mapped candidate | R5 |
| `react/no-this-in-sfc` | error | No direct mapped candidate | R5 |
| `react/no-typos` | error | No direct mapped candidate | R5 |
| `react/no-unused-class-component-methods` | error | No direct mapped candidate | R5 |
| `react/no-unused-prop-types` | error | No direct mapped candidate | R5 |
| `react/no-unused-state` | error | No direct mapped candidate | R5 |
| `react/no-will-update-set-state` | error | No direct mapped candidate | R5 |
| `react/prefer-es6-class` | error | No direct mapped candidate | R5 |
| `react/prefer-exact-props` | error | No direct mapped candidate | R5 |
| `react/prefer-stateless-function` | error | No direct mapped candidate | R5 |
| `react/sort-comp` | error | No direct mapped candidate | R5 |
| `react/state-in-constructor` | error | No direct mapped candidate | R5 |
| `react/static-property-placement` | error | No direct mapped candidate | R5 |
| `react/style-prop-object` | error | No direct mapped candidate | R5 |

## Related candidates with review retained

| Reference ESLint rule | Reference severity | Biome 2.5.15 candidate | Coverage/owner |
| --- | --- | --- | --- |
| `import/no-unresolved` | error | `noUnresolvedImports` | partial/related; retain R4 |
| `@typescript-eslint/await-thenable` | error | `useAwaitThenable` (nursery) | partial/related; retain R1 |
| `@typescript-eslint/no-unnecessary-type-assertion` | error | `noUnsafeTypeAssertion` (nursery) | partial/related; retain R1 |
| `@typescript-eslint/no-unused-expressions` | error | `noUnusedExpressions` | partial/related; retain R1 |
| `@typescript-eslint/consistent-generic-constructors` | error | `useConsistentBuiltinInstantiation` | partial/related; retain R6 |
| `@typescript-eslint/consistent-type-assertions` | error | `noUnsafeTypeAssertion` (nursery) | partial/related; retain R1 |
| `@typescript-eslint/no-confusing-non-null-assertion` | error | `noNonNullAssertion` | partial/related; retain R1 |
| `@typescript-eslint/non-nullable-type-assertion-style` | error | `noNonNullAssertion` | partial/related; retain R1 |
| `react/no-direct-mutation-state` | error | `noReactPropAssignments`, `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react/no-render-return-value` | error | `noRenderReturnValue` | partial/related; retain R5 |
| `react-hooks/static-components` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/use-memo` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/preserve-manual-memoization` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/incompatible-library` | warning | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/immutability` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/globals` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/refs` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/set-state-in-effect` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/error-boundaries` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/purity` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/set-state-in-render` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/unsupported-syntax` | warning | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/config` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react-hooks/gating` | error | `useReactCompiler` (nursery) | partial/related; retain R5 |
| `react/jsx-pascal-case` | error | `useReactNamingConvention` (nursery) | partial/related; retain R5 |
| `react/no-namespace` | error | `noJsxNamespace` (nursery) | partial/related; retain R5 |
| `react/no-unstable-nested-components` | error | `noNestedComponentDefinitions` | partial/related; retain R5 |
| `react/self-closing-comp` | error | `useSelfClosingElements` | partial/related; retain R5 |

## Officially mapped candidates

| Reference ESLint rule | Reference severity | Biome 2.5.15 candidate | Coverage/owner |
| --- | --- | --- | --- |
| `constructor-super` | error | `noInvalidConstructorSuper` | source mapping; verify options |
| `for-direction` | error | `useValidForDirection` | source mapping; verify options |
| `getter-return` | error | `useGetterReturn` | source mapping; verify options |
| `no-async-promise-executor` | error | `noAsyncPromiseExecutor` | source mapping; verify options |
| `no-case-declarations` | error | `noSwitchDeclarations` | source mapping; verify options |
| `no-class-assign` | error | `noClassAssign` | source mapping; verify options |
| `no-compare-neg-zero` | error | `noCompareNegZero` | source mapping; verify options |
| `no-cond-assign` | error | `noAssignInExpressions` | inspired; options differ |
| `no-const-assign` | error | `noConstAssign` | source mapping; verify options |
| `no-constant-binary-expression` | error | `noConstantBinaryExpressions` | source mapping; verify options |
| `no-constant-condition` | warning | `noConstantCondition` | source mapping; verify options |
| `no-control-regex` | error | `noControlCharactersInRegex` | source mapping; verify options |
| `no-debugger` | error | `noDebugger` | source mapping; verify options |
| `no-dupe-args` | error | `noDuplicateParameters` | source mapping; verify options |
| `no-dupe-class-members` | error | `noDuplicateClassMembers` | source mapping; verify options |
| `no-dupe-else-if` | error | `noDuplicateElseIf` | source mapping; verify options |
| `no-dupe-keys` | error | `noDuplicateObjectKeys` | source mapping; verify options |
| `no-duplicate-case` | error | `noDuplicateCase` | source mapping; verify options |
| `no-empty` | error | `noEmptyBlockStatements` | source mapping; verify options |
| `no-empty-character-class` | error | `noEmptyCharacterClassInRegex` | source mapping; verify options |
| `no-empty-pattern` | error | `noEmptyPattern` | source mapping; verify options |
| `no-empty-static-block` | error | `noEmptyBlockStatements` | source mapping; verify options |
| `no-ex-assign` | error | `noCatchAssign` | source mapping; verify options |
| `no-extra-boolean-cast` | error | `noExtraBooleanCast` | source mapping; verify options |
| `no-fallthrough` | error | `noFallthroughSwitchClause` | source mapping; verify options |
| `no-func-assign` | error | `noFunctionAssign` | source mapping; verify options |
| `no-global-assign` | error | `noGlobalAssign` | source mapping; verify options |
| `no-import-assign` | error | `noImportAssign` | source mapping; verify options |
| `no-irregular-whitespace` | error | `noIrregularWhitespace` | source mapping; verify options |
| `no-loss-of-precision` | error | `noPrecisionLoss` | source mapping; verify options |
| `no-misleading-character-class` | error | `noMisleadingCharacterClass` | source mapping; verify options |
| `no-nonoctal-decimal-escape` | error | `noNonoctalDecimalEscape` | source mapping; verify options |
| `no-obj-calls` | error | `noGlobalObjectCalls` | source mapping; verify options |
| `no-prototype-builtins` | error | `noPrototypeBuiltins` | source mapping; verify options |
| `no-redeclare` | error | `noRedeclare` | source mapping; verify options |
| `no-regex-spaces` | error | `noAdjacentSpacesInRegex` | source mapping; verify options |
| `no-self-assign` | error | `noSelfAssign` | source mapping; verify options |
| `no-setter-return` | error | `noSetterReturn` | source mapping; verify options |
| `no-shadow-restricted-names` | error | `noShadowRestrictedNames` | source mapping; verify options |
| `no-sparse-arrays` | error | `noSparseArray` | source mapping; verify options |
| `no-this-before-super` | error | `noUnreachableSuper` | source mapping; verify options |
| `no-undef` | error | `noUndeclaredVariables` | source mapping; verify options |
| `no-unreachable` | error | `noUnreachable` | source mapping; verify options |
| `no-unsafe-finally` | error | `noUnsafeFinally` | source mapping; verify options |
| `no-unsafe-negation` | error | `noUnsafeNegation` | source mapping; verify options |
| `no-unsafe-optional-chaining` | error | `noUnsafeOptionalChaining` | source mapping; verify options |
| `no-unused-labels` | error | `noUnusedLabels` | source mapping; verify options |
| `no-unused-private-class-members` | error | `noUnusedPrivateClassMembers` | inspired; options differ |
| `no-useless-backreference` | error | `noUselessRegexBackrefs` | source mapping; verify options |
| `no-useless-catch` | error | `noUselessCatch` | source mapping; verify options |
| `no-useless-escape` | error | `noUselessEscapeInRegex` | source mapping; verify options |
| `no-with` | error | `noWith` | source mapping; verify options |
| `require-yield` | error | `useYield` | source mapping; verify options |
| `use-isnan` | error | `useIsNan` | source mapping; verify options |
| `valid-typeof` | error | `useValidTypeof` | source mapping; verify options |
| `import/named` | error | `noUnresolvedImports` | inspired; options differ |
| `no-var` | error | `noVar` | source mapping; verify options |
| `prefer-const` | error | `useConst` | source mapping; verify options |
| `prefer-rest-params` | error | `noArguments` | source mapping; verify options |
| `prefer-spread` | error | `useSpreadOverApply` | source mapping; verify options |
| `@typescript-eslint/ban-ts-comment` | error | `noTsIgnore` | inspired; options differ |
| `no-array-constructor` | error | `useArrayLiterals` | source mapping; verify options |
| `@typescript-eslint/no-array-constructor` | error | `useArrayLiterals` | source mapping; verify options |
| `@typescript-eslint/no-base-to-string` | error | `noBaseToString` (nursery) | source mapping; verify options |
| `@typescript-eslint/no-duplicate-enum-values` | error | `noDuplicateEnumValues` | source mapping; verify options |
| `@typescript-eslint/no-empty-object-type` | error | `noBannedTypes` | inspired; options differ |
| `@typescript-eslint/no-explicit-any` | error | `noExplicitAny` | source mapping; verify options |
| `@typescript-eslint/no-extra-non-null-assertion` | error | `noExtraNonNullAssertion` | source mapping; verify options |
| `@typescript-eslint/no-floating-promises` | error | `noFloatingPromises` (nursery) | source mapping; verify options |
| `@typescript-eslint/no-for-in-array` | error | `noForIn` | inspired; options differ |
| `no-implied-eval` | error | `noImpliedEval` (nursery) | source mapping; verify options |
| `@typescript-eslint/no-implied-eval` | error | `noImpliedEval` (nursery) | source mapping; verify options |
| `@typescript-eslint/no-misused-new` | error | `noMisleadingInstantiator` | source mapping; verify options |
| `@typescript-eslint/no-misused-promises` | error | `noMisusedPromises` (nursery) | source mapping; verify options |
| `@typescript-eslint/no-namespace` | error | `noNamespace` | source mapping; verify options |
| `@typescript-eslint/no-non-null-asserted-optional-chain` | error | `noNonNullAssertedOptionalChain` | source mapping; verify options |
| `@typescript-eslint/no-require-imports` | error | `noCommonJs` | source mapping; verify options |
| `@typescript-eslint/no-this-alias` | error | `noUselessThisAlias` | inspired; options differ |
| `@typescript-eslint/no-unnecessary-type-constraint` | error | `noUselessTypeConstraint` | source mapping; verify options |
| `@typescript-eslint/no-unsafe-declaration-merging` | error | `noUnsafeDeclarationMerging` | source mapping; verify options |
| `@typescript-eslint/no-unsafe-function-type` | error | `noBannedTypes` | inspired; options differ |
| `no-unused-expressions` | error | `noUnusedExpressions` | source mapping; verify options |
| `@typescript-eslint/no-unused-vars` | error | `noUnusedVariables` | source mapping; verify options |
| `@typescript-eslint/no-wrapper-object-types` | error | `noBannedTypes` | inspired; options differ |
| `no-throw-literal` | error | `useThrowOnlyError` | inspired; options differ |
| `@typescript-eslint/only-throw-error` | error | `useThrowOnlyError` | inspired; options differ |
| `@typescript-eslint/prefer-as-const` | error | `useAsConstAssertion` | source mapping; verify options |
| `@typescript-eslint/prefer-namespace-keyword` | error | `useNamespaceKeyword` | source mapping; verify options |
| `prefer-promise-reject-errors` | error | `usePromiseRejectErrors` (nursery) | source mapping; verify options |
| `@typescript-eslint/prefer-promise-reject-errors` | error | `usePromiseRejectErrors` (nursery) | source mapping; verify options |
| `@typescript-eslint/require-await` | error | `useAwait` | source mapping; verify options |
| `@typescript-eslint/restrict-plus-operands` | error | `noUnsafePlusOperands` (nursery) | source mapping; verify options |
| `@typescript-eslint/adjacent-overload-signatures` | error | `useAdjacentOverloadSignatures` | source mapping; verify options |
| `@typescript-eslint/array-type` | error | `useConsistentArrayType` | source mapping; verify options |
| `@typescript-eslint/consistent-type-definitions` | error | `useConsistentTypeDefinitions` | source mapping; verify options |
| `dot-notation` | error | `useLiteralKeys` | source mapping; verify options |
| `@typescript-eslint/dot-notation` | error | `useLiteralKeys` | source mapping; verify options |
| `no-empty-function` | error | `noEmptyBlockStatements` | source mapping; verify options |
| `@typescript-eslint/no-empty-function` | error | `noEmptyBlockStatements` | source mapping; verify options |
| `@typescript-eslint/no-inferrable-types` | error | `noInferrableTypes` | source mapping; verify options |
| `@typescript-eslint/prefer-find` | error | `useArrayFind` | source mapping; verify options |
| `@typescript-eslint/prefer-for-of` | error | `useForOf` | source mapping; verify options |
| `@typescript-eslint/prefer-function-type` | error | `useShorthandFunctionType` | source mapping; verify options |
| `@typescript-eslint/prefer-includes` | error | `useIncludes` (nursery) | inspired; options differ |
| `@typescript-eslint/prefer-nullish-coalescing` | error | `useNullishCoalescing` (nursery) | inspired; options differ |
| `@typescript-eslint/prefer-optional-chain` | error | `useOptionalChain` | source mapping; verify options |
| `@typescript-eslint/prefer-regexp-exec` | error | `useRegexpExec` (nursery) | source mapping; verify options |
| `@typescript-eslint/prefer-string-starts-ends-with` | error | `useStringStartsEndsWith` (nursery) | inspired; options differ |
| `react/jsx-key` | error | `useJsxKeyInIterable` | source mapping; verify options |
| `react/jsx-no-comment-textnodes` | error | `noCommentText` | source mapping; verify options |
| `react/jsx-no-duplicate-props` | error | `noDuplicateJsxProps` | source mapping; verify options |
| `react/jsx-no-target-blank` | error | `noBlankTarget` | inspired; options differ |
| `react/no-children-prop` | error | `noChildrenProp` | source mapping; verify options |
| `react/no-danger-with-children` | error | `noDangerouslySetInnerHtmlWithChildren` | source mapping; verify options |
| `react/no-string-refs` | error | `noReactStringRefs` (nursery) | source mapping; verify options |
| `react/no-unknown-property` | error | `noUnknownAttribute` | source mapping; verify options |
| `react-hooks/rules-of-hooks` | error | `useHookAtTopLevel` | source mapping; verify options |
| `react-hooks/exhaustive-deps` | error | `useExhaustiveDependencies` | source mapping; verify options |
| `jsx-a11y/alt-text` | error | `useAltText` | source mapping; verify options |
| `jsx-a11y/anchor-has-content` | error | `useAnchorContent` | source mapping; verify options |
| `jsx-a11y/anchor-is-valid` | error | `useValidAnchor` | source mapping; verify options |
| `jsx-a11y/aria-activedescendant-has-tabindex` | error | `useAriaActivedescendantWithTabindex` | source mapping; verify options |
| `jsx-a11y/aria-props` | error | `useValidAriaProps` | source mapping; verify options |
| `jsx-a11y/aria-proptypes` | error | `useValidAriaValues` | source mapping; verify options |
| `jsx-a11y/aria-role` | error | `useValidAriaRole` | source mapping; verify options |
| `jsx-a11y/aria-unsupported-elements` | error | `noAriaUnsupportedElements` | source mapping; verify options |
| `jsx-a11y/autocomplete-valid` | error | `useValidAutocomplete` | source mapping; verify options |
| `jsx-a11y/click-events-have-key-events` | error | `useKeyWithClickEvents` | source mapping; verify options |
| `jsx-a11y/control-has-associated-label` | error | `useControlLabel` (nursery) | inspired; options differ |
| `jsx-a11y/heading-has-content` | error | `useHeadingContent` | source mapping; verify options |
| `jsx-a11y/html-has-lang` | error | `useHtmlLang` | source mapping; verify options |
| `jsx-a11y/iframe-has-title` | error | `useIframeTitle` | source mapping; verify options |
| `jsx-a11y/img-redundant-alt` | error | `noRedundantAlt` | source mapping; verify options |
| `jsx-a11y/interactive-supports-focus` | error | `useFocusableInteractive` | source mapping; verify options |
| `jsx-a11y/label-has-associated-control` | error | `noLabelWithoutControl` | source mapping; verify options |
| `jsx-a11y/media-has-caption` | error | `useMediaCaption` | source mapping; verify options |
| `jsx-a11y/mouse-events-have-key-events` | error | `useKeyWithMouseEvents` | source mapping; verify options |
| `jsx-a11y/no-access-key` | error | `noAccessKey` | source mapping; verify options |
| `jsx-a11y/no-autofocus` | error | `noAutofocus` | source mapping; verify options |
| `jsx-a11y/no-distracting-elements` | error | `noDistractingElements` | source mapping; verify options |
| `jsx-a11y/no-interactive-element-to-noninteractive-role` | error | `noInteractiveElementToNoninteractiveRole` | source mapping; verify options |
| `jsx-a11y/no-noninteractive-element-interactions` | error | `noNoninteractiveElementInteractions` | source mapping; verify options |
| `jsx-a11y/no-noninteractive-element-to-interactive-role` | error | `noNoninteractiveElementToInteractiveRole` | source mapping; verify options |
| `jsx-a11y/no-noninteractive-tabindex` | error | `noNoninteractiveTabindex` | source mapping; verify options |
| `jsx-a11y/no-redundant-roles` | error | `noRedundantRoles` | source mapping; verify options |
| `jsx-a11y/no-static-element-interactions` | error | `noStaticElementInteractions` | source mapping; verify options |
| `jsx-a11y/role-has-required-aria-props` | error | `useAriaPropsForRole` | source mapping; verify options |
| `jsx-a11y/role-supports-aria-props` | error | `useAriaPropsSupportedByRole` | source mapping; verify options |
| `jsx-a11y/scope` | error | `noHeaderScope` | source mapping; verify options |
| `jsx-a11y/tabindex-no-positive` | error | `noPositiveTabindex` | source mapping; verify options |
| `@typescript-eslint/no-shadow` | error | `noShadow` | source mapping; verify options |
| `@typescript-eslint/no-use-before-define` | error | `noInvalidUseBeforeDeclaration` | source mapping; verify options |
| `@typescript-eslint/no-useless-constructor` | error | `noUselessConstructor` | source mapping; verify options |
| `import/no-default-export` | error | `noDefaultExport` | source mapping; verify options |
| `no-plusplus` | error | `noIncrementDecrement` | source mapping; verify options |
| `import/no-extraneous-dependencies` | error | `noUndeclaredDependencies` | source mapping; verify options |
| `no-void` | error | `noVoid` | source mapping; verify options |
| `array-callback-return` | error | `useIterableCallbackReturn` | source mapping; verify options |
| `arrow-body-style` | error | `useConsistentArrowReturn` | source mapping; verify options |
| `class-methods-use-this` | error | `useThisInClassMethods` (nursery) | source mapping; verify options |
| `default-case` | error | `useDefaultSwitchClause` | source mapping; verify options |
| `default-case-last` | error | `useDefaultSwitchClauseLast` | source mapping; verify options |
| `default-param-last` | error | `useDefaultParameterLast` | source mapping; verify options |
| `eqeqeq` | error | `noDoubleEquals` | source mapping; verify options |
| `grouped-accessor-pairs` | error | `useGroupedAccessorPairs` | source mapping; verify options |
| `guard-for-in` | error | `useGuardForIn` | source mapping; verify options |
| `import/first` | error | `useImportsFirst` (nursery) | source mapping; verify options |
| `import/no-cycle` | error | `noImportCycles` | source mapping; verify options |
| `import/no-self-import` | error | `noSelfImport` (nursery) | source mapping; verify options |
| `max-classes-per-file` | error | `noExcessiveClassesPerFile` | source mapping; verify options |
| `no-alert` | warning | `noAlert` | source mapping; verify options |
| `no-await-in-loop` | error | `noAwaitInLoops` | source mapping; verify options |
| `no-bitwise` | error | `noBitwiseOperators` | source mapping; verify options |
| `no-console` | warning | `noConsole` | source mapping; verify options |
| `no-constructor-return` | error | `noConstructorReturn` | source mapping; verify options |
| `no-continue` | error | `noContinue` | source mapping; verify options |
| `no-else-return` | error | `noUselessElse` | inspired; options differ |
| `no-eval` | error | `noGlobalEval` | source mapping; verify options |
| `no-extend-native` | error | `noExtendNative` (nursery) | source mapping; verify options |
| `no-extra-label` | error | `noUselessLabel` | source mapping; verify options |
| `no-inner-declarations` | error | `noInnerDeclarations` | source mapping; verify options |
| `no-label-var` | error | `noLabelVar` | source mapping; verify options |
| `no-labels` | error | `noConfusingLabels` | inspired; options differ |
| `no-lone-blocks` | error | `noUselessLoneBlockStatements` | source mapping; verify options |
| `no-lonely-if` | error | `useCollapsedElseIf` | source mapping; verify options |
| `no-loop-func` | error | `noLoopFunc` (nursery) | source mapping; verify options |
| `no-multi-assign` | error | `noMultiAssign` | inspired; options differ |
| `no-multi-str` | error | `noMultilineString` | source mapping; verify options |
| `no-nested-ternary` | error | `noNestedTernary` | source mapping; verify options |
| `no-new` | error | `noUnusedInstantiation` | source mapping; verify options |
| `no-new-func` | error | `noImpliedEval` (nursery) | inspired; options differ |
| `no-new-wrappers` | error | `useConsistentBuiltinInstantiation` | source mapping; verify options |
| `no-octal-escape` | error | `noOctalEscape` | source mapping; verify options |
| `no-param-reassign` | error | `noParameterAssign` | source mapping; verify options |
| `no-proto` | error | `noProto` | source mapping; verify options |
| `no-restricted-globals` | error | `noRestrictedGlobals` | source mapping; verify options |
| `no-restricted-properties` | error | `noJsRestrictedProperties` (nursery) | source mapping; verify options |
| `no-return-assign` | error | `noReturnAssign` | source mapping; verify options |
| `no-script-url` | error | `noScriptUrl` | source mapping; verify options |
| `no-self-compare` | error | `noSelfCompare` | source mapping; verify options |
| `no-sequences` | error | `noCommaOperator` | source mapping; verify options |
| `no-template-curly-in-string` | error | `noTemplateCurlyInString` | source mapping; verify options |
| `no-undef-init` | error | `noUselessUndefinedInitialization` | source mapping; verify options |
| `no-unneeded-ternary` | error | `noUselessTernary` | source mapping; verify options |
| `no-useless-computed-key` | error | `useLiteralKeys` | source mapping; verify options |
| `no-useless-concat` | error | `noUselessStringConcat` | source mapping; verify options |
| `no-useless-rename` | error | `noUselessRename` | source mapping; verify options |
| `no-useless-return` | error | `noUselessReturn` | inspired; options differ |
| `object-shorthand` | error | `useConsistentObjectDefinitions` | inspired; options differ |
| `one-var` | error | `useSingleVarDeclarator` | source mapping; verify options |
| `operator-assignment` | error | `useShorthandAssign` | source mapping; verify options |
| `prefer-arrow-callback` | error | `useArrowFunction` | inspired; options differ |
| `prefer-destructuring` | error | `useDestructuring` | inspired; options differ |
| `prefer-exponentiation-operator` | error | `useExponentiationOperator` | source mapping; verify options |
| `prefer-numeric-literals` | error | `useNumericLiterals` | source mapping; verify options |
| `prefer-object-spread` | error | `useObjectSpread` | source mapping; verify options |
| `prefer-regex-literals` | error | `useRegexLiterals` | source mapping; verify options |
| `prefer-template` | error | `useTemplate` | source mapping; verify options |
| `radix` | error | `useParseIntRadix` | source mapping; verify options |
| `symbol-description` | error | `useSymbolDescription` | source mapping; verify options |
| `vars-on-top` | error | `useVarsOnTop` (nursery) | source mapping; verify options |
| `yoda` | error | `noYodaExpression` | source mapping; verify options |
| `react-refresh/only-export-components` | warning | `useComponentExportOnlyModules` | inspired; options differ |
| `jsx-a11y/lang` | error | `useValidLang` | source mapping; verify options |
| `react/button-has-type` | error | `useButtonType` | source mapping; verify options |
| `react/jsx-boolean-value` | error | `noImplicitBoolean` | inspired; options differ |
| `react/jsx-curly-brace-presence` | error | `useConsistentCurlyBraces` | inspired; options differ |
| `react/jsx-fragments` | error | `useFragmentSyntax` | source mapping; verify options |
| `react/jsx-no-bind` | error | `noJsxPropsBind` | inspired; options differ |
| `react/jsx-no-script-url` | error | `noScriptUrl` | source mapping; verify options |
| `react/jsx-no-useless-fragment` | error | `noUselessFragments` | source mapping; verify options |
| `react/no-array-index-key` | error | `noArrayIndexKey` | source mapping; verify options |
| `react/no-danger` | warning | `noDangerouslySetInnerHtml` | source mapping; verify options |
| `react/void-dom-elements-no-children` | error | `noVoidElementsWithChildren` | source mapping; verify options |
