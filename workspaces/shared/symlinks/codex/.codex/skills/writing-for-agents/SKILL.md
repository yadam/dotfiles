---
name: writing-for-agents
description: >-
  Create or review instructions an agent must execute. Use for SKILL.md,
  AGENTS.md, CLAUDE.md, agent checklists, and agent-specific procedures.
  Own instruction structure, routing, and observable completion criteria.
  Use unslop for the final clarity pass. Ordinary explanations and
  human-facing documentation remain with unslop.
license: MIT
metadata:
  source: https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/writing-for-agents
  adaptation: Adam's agent-instruction scope and composition with unslop
---

# Writing for agents

Make instructions discoverable, executable, and clear about completion.

## Scope and ownership

Use this skill when creating or reviewing instructions an agent is expected
to execute. Merely reading a document does not make it an agent procedure.
In mixed documents, apply these principles to the agent-specific sections.

This skill owns instruction structure, routing, and operational requirements.
[Unslop](../unslop/SKILL.md) owns the wording and punctuation of the final
clarity pass. Use unslop alone for ordinary explanations, human-facing README
sections, engineering documentation, PR descriptions, and commit messages.
[Humanizer](../humanizer/SKILL.md) remains responsible for narration, scripts,
resumes, cover letters, and other writing where personal voice matters.
Engineering narration follows humanizer's existing light clarity reference.

For creating or changing a skill's packaging, frontmatter, invocation metadata,
or supporting resources, use
the installed `skill-creator` skill. Use the host's actual
mechanics rather than copying another platform's discovery or invocation rules.

## Route to the right material

A reference should name its target and state when to read it. For example,
"Read deployment.md when publishing a release" gives the agent both a resource
and a condition. Keep descriptions and always-loaded instructions concise,
with distinct use cases rather than lists of synonyms for the same case.

Before adding another pointer or document, check whether existing instructions
already cover the task. A required reference must be available and reachable.
If a pointer is unclear, clarify its wording before inlining a large reference.

## Organize steps and references

Put shared purpose, essential constraints, and needed actions where every
applicable reader will see them. Keep a concept's definition, requirements,
and caveats together. Place substantial conditional detail behind a reference
whose reading condition is explicit.

Split by a real difference in task, audience, or procedure when that improves
navigation. Do not introduce separate files, handoffs, or agent roles merely
to hide later steps or shorten the entry point. A simple instruction can remain
a single paragraph. A fixed checklist is useful only when the workflow needs it.

## Define observable completion

For consequential stages, state what action is required and what observed
result establishes completion. Name necessary inputs, preconditions, evidence,
and limits when they affect execution. Match coverage to the actual task.
Do not require every conceivable field or exhaustive checks for a routine edit.

Replace "verify the app" with the actual behavior to exercise and the result
to observe. Keep required checks distinct from optional recommendations.
State unverified or inconclusive outcomes explicitly when a procedure cannot
be completed. Do not invent commands, selectors, evidence, or success criteria
to make instructions appear complete.

## Maintain authoritative instructions

Keep each rule in one authoritative place. Link to it when other procedures
need the same requirement. Necessary repetition is appropriate at a point of
action, in a standalone excerpt, or when an important condition could otherwise
be missed.

Use configuration, task-runner scripts, and tool help as sources of truth for
cheap lookups. Preserve unwritten conventions, non-obvious constraints, and
reasons that those files cannot explain. An exact command belongs in a verified
recipe when reproducibility requires it. Keep that command grounded in the
current environment rather than copying stale examples.

Prune irrelevant, stale, or redundant guidance when supported by the task and
evidence. Do not discard an explicit user preference or an operational invariant
merely because the agent might already follow it by default.

## Use complete, precise language

Use established project vocabulary and define unfamiliar terms. Prefer complete
instructions over compressed keywords that hide requirements. Phrase ordinary
guidance as the desired action when that is clearer. Preserve explicit
prohibitions, authorization boundaries, and user preferences. Do not treat a
theory about negation activating unwanted behavior as an established fact.

Keep obligation strength accurate. "Must", "may", "only", and "never" can carry
requirements that a softer paraphrase would change. Preserve literal commands,
paths, identifiers, contract headings, and meaningful distinctions.

## Compose with unslop

1. Establish the trigger, actions, necessary inputs, constraints, evidence, and
   completion conditions appropriate to the task.
2. Apply unslop to the wording after those requirements are correct. Let it own
   style preferences instead of maintaining a second punctuation or vocabulary
   catalog here.
3. Check that the cleanup preserved the trigger, obligation strength, exceptions,
   links, exact commands, and completion conditions. Compare edits with the
   original requirements and any explicitly approved changes.

Change workflow behavior only within the requested scope. Identify a proposed
workflow change separately when it goes beyond a prose edit. The finished
instructions should be usable without an explanation of the editorial passes.
