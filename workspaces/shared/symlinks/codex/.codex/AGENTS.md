# Adam's working preferences

Continue authorized work through completion. Resolve routine implementation
choices from the task and available evidence. Ask when missing information
materially changes the outcome, rather than repeating an approval already given.

Use the installed `unslop` skill for assistant explanations and engineering
prose. Use `writing-for-agents` when creating or reviewing instructions an agent
must execute. It owns instruction structure, followed by unslop's wording pass
and a check that the requirements were preserved.

Use `humanizer` for narration, scripts, resumes, cover letters, and application
answers. Engineering narration uses its existing light clarity reference.
Preserve project voice profiles and explicitly requested formats.

For development work, read and use the [tdd skill](skills/tdd/SKILL.md).
Default to small red-green-refactor cycles through public interfaces.
Match verification to behavior and risk. Use appropriate direct checks for
documentation and other reversible edits that do not change behavior.

When diagnosing bugs or performance regressions, read and use the
[diagnosing-bugs skill](skills/diagnosing-bugs/SKILL.md). Scale the reproduction,
investigation, and verification to the difficulty of the failure.

When designing or changing domain concepts, terminology, relationships, or
invariants, read and use the [domain-modeling skill](skills/domain-modeling/SKILL.md).
Follow existing project glossary and architecture conventions.

Whenever working with TypeScript, read and use the
[typescript-quality skill](skills/typescript-quality/SKILL.md). This includes
writing, reviewing, debugging, or designing TypeScript code and configuring
its compiler or quality tools.

The punctuation preferences live in unslop. Preserve literal code, commands,
paths, and quotations when editing prose.

During code review, consider whether added tests duplicate existing coverage.
If Cypress is present, inspect fixed `cy.wait(...)` delays and prefer waits for
an observable condition when appropriate. Preserve meaningful verification.

Keep project-specific rules, setup commands, and domain knowledge in the
project's own instructions and configuration. Apply each skill only to its
stated purpose.
