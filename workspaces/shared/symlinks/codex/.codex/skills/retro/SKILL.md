---
name: retro
description: Review a specified coding session for evidence-backed improvements to checks, navigation,
  instructions, and tooling. Recommend changes in order of severity.
license: MIT
metadata:
  source: https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/retro
  adaptation: Adam's Codex workflow and writing-for-agents integration
---

# Retrospective

Review the coding session the user specifies and recommend changes that improve future work. Default to the current conversation when no other session is named. This is an evidence-based review, not permission to rewrite global instructions or project configuration.

## Gather the evidence

Use available task records, commands, outcomes, diffs, and artifacts. Read task-scoped logs when relevant and available. Avoid searching unrelated private chats. Distinguish observed failures from suspected weaknesses. If the record is incomplete, state what the review can and cannot establish.

## Find improvements

- **Navigation.** Did finding the relevant files take unnecessary work? Recommend a precise link and a condition for following it.
- **Automated checks.** Inspect existing lint, typecheck, test, hook, and CI commands first. A check that exists but is broken or unwired is a repair opportunity. Identify the concrete mistake or invariant a proposed check would catch.
- **Coding standards.** Prefer a deterministic check for mechanical violations when the benefit justifies it. Keep guidance for choices that require judgment. Do not add a rule for every isolated mistake.
- **Instructions.** Identify duplication, stale commands, missing caveats, or guidance that repeatedly misroutes work. Keep project-wide context small and put conditional detail in discoverable references.
- **Tool use.** Look for expensive repeated searches or calls that existing scripts, batching, or targeted reads could replace.
- **Information access.** Identify missing read-only evidence, useful logs, or environment details. Recommend the smallest relevant improvement instead of broader access by default.

Do not assume the project has a separate implementation agent and review agent. Recommend ownership that matches its actual workflow. Reuse existing documents before creating new ones.

## Write useful proposals

Use [unslop](../unslop/SKILL.md) for the user-facing explanation. When proposing or editing agent instructions, read [writing-for-agents](../writing-for-agents/SKILL.md) for instruction structure, routing, and observable completion criteria. Follow its composition process for the final clarity pass and requirement check. Ordinary retrospective explanations need only unslop.

For skill packaging or validation, use the installed `skill-creator` skill. Keep the authoring principles in writing-for-agents as the authoritative reference rather than duplicating them here.

## Handoff

Rank a small set of candidates by severity or expected benefit. For each, identify the observed problem, supporting evidence, concrete change, and how its effect could be checked. Separate required repairs from optional improvements. A missing hook is not automatically a reason to add one when existing CI already covers the need.

Implement recommendations only when the user requests implementation or has already authorized that scope. Installation of this skill alone does not authorize changing external services, global configuration, or unrelated projects.
