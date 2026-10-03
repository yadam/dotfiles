---
name: tdd
description: >-
  Default to test-first development for features, bug fixes, and refactoring.
  Use public interfaces and small red-green-refactor cycles. Also use for explicit
  TDD or behavior-focused integration-test requests. Scale verification to behavior
  and risk.
license: MIT
metadata:
  source: https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/tdd
  adaptation: Adam's Codex workflow, scoped execution, and self-contained references
---

# Test-driven development

Build behavior in small red-green-refactor cycles. Read existing rules, specifications, GLOSSARY.md, and relevant architecture decisions so the test vocabulary and expected results match the domain.

## Choose the public interface

Test at a public boundary where the behavior is observable: a domain function, module API, service endpoint, command, or user interaction. Use interfaces already established by the request, specification, or existing tests. State the chosen boundary when it matters. Existing authorization is enough to proceed.

Clarify only when different plausible interfaces or expected behaviors would materially change the work and the available sources cannot resolve them. Do not request confirmation before every test. If the interface is still unsettled, inspect the existing design and resolve the relevant decision before adding a large suite. No additional design or review skill is required.

## What a useful test proves

Tests exercise behavior callers care about and survive internal refactoring. Expected results come from an independent source: the specification, a worked example, a known correct literal, or an independently validated reference. Do not recompute the expected value with the same algorithm being tested.

Read [tests.md](tests.md) for examples and [mocking.md](mocking.md) when choosing test dependencies. Prefer real local implementations. Control time, randomness, storage, and external services where needed to make the test reliable. Observe durable side effects through a public read interface when one exists. Direct storage inspection can be appropriate when storage behavior itself is the contract.

## Run the loop

1. Choose one meaningful behavior within the task.
2. Write a test that fails on that behavior. Run it and confirm the expected failure, rather than a broken test setup.
3. Make the smallest implementation change that satisfies it.
4. Run the relevant test and confirm it passes.
5. Refactor when it improves the changed code without adding speculative features. Keep the relevant tests green.
6. Repeat for the next behavior, then run the project's required checks before handoff.

For a bug, establish a failing reproduction before the fix and rerun the original scenario afterward. Each cycle should teach something about the real behavior. Avoid writing a large batch of speculative tests followed by a large implementation batch.

## Avoid false confidence

- Do not test private methods or internal call sequences when observable behavior answers the question.
- Do not mock internal collaborators merely to make the test easy to write.
- Do not derive expected results from the implementation itself.
- Do not add tests that simply mirror a reversible, low-impact edit or assert generated wording.
- Do not claim a test was red or green without having run it.

Use the project's existing runner and conventions. Match test effort to the risk and behavior under change. Explain material unverified behavior or infrastructure limits in the handoff.
