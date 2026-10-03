---
name: show-me-your-work
description: Keep an evidence-backed decision log for long-running, unattended, or experimental
  work. Use when asked for a reviewable trail of decisions and outcomes.
license: MIT
metadata:
  source: https://github.com/cursor/plugins/tree/7022c81efb48d8b5eb15498ce6043a3bd74b694c/pstack/skills/show-me-your-work
  adaptation: Adam's Codex workflow, scoped execution, and self-contained references
---

# Show me your work

Keep a reviewable record of material decisions and the evidence for their outcomes. Record concise reasons that a teammate can assess. Do not record a private reasoning transcript or every tool call.

## One canonical log

Use the header in [decision-log-template.tsv](references/decision-log-template.tsv). Each row has six single-line cells:

- `ts`: UTC timestamp in ISO8601 format.
- `phase`: the phase or workstream.
- `decision`: the chosen action or decision.
- `why`: a concise reason.
- `evidence`: a resolving path, link, commit, trace, or screenshot.
- `result`: the observed outcome, or `open` or `INCONCLUSIVE` when unresolved.

Use `scripts/log.sh <logfile> <phase> <decision> <why> <evidence> <result>`. The helper creates the header, timestamps the row, flattens tabs and newlines, and prefixes formula-leading characters for spreadsheet readers. Use one writer per log when work is concurrent. Separate logs are preferable to interleaved writes.

Keep the log local by default, at `decisions.tsv` or `.audit/<task-name>.tsv` in the task's working directory. Check existing ignore rules so the artifact is not accidentally committed. Commit a trail only when requested or when it is part of the agreed review deliverable.

## What to record

Log significant choices, completed units and their verification, pivots, reversions, and blockers. For repeated experiments, one row per iteration is usually enough. Skip routine navigation and self-evident commands. Use [unslop](../unslop/SKILL.md) for clear, concrete log text.

Start a resumed or replacement run with a `start` row naming the task or run and the earlier rows it is taking over. Check the tail before appending after a gap. Identify the rows produced by this run so a later audit does not imply review of unrelated work.

The log is append-only. Correct a wrong claim by adding a row that identifies and supersedes it. Preserve the original entry. Evidence is a pointer to an artifact, not an unsupported summary. Avoid secrets and redact sensitive captured output before linking or quoting it.

## Audit before handoff

Check this run's entries against the available conversation, commands, outputs, diff, and artifacts. If a task-scoped transcript is available, use only that transcript. Do not search unrelated private conversations to manufacture a complete record.

- Confirm each entry describes a real decision or action.
- Follow evidence pointers and check that they support the claimed result.
- Add material pivots or abandoned approaches missing from the record.
- Supersede false or overstated claims with the observed result.
- Mark inaccessible evidence and unresolved claims as inconclusive.

When an independent review is requested and available, give the reviewer the relevant log and evidence. A different model family can be useful but is not required. This skill does not require delegation. Do not claim independent review when only self-review occurred. State the review's actual coverage and any evidence limits.

## Handoff

Link the log and flag the rows requiring attention. If review occurred, identify who or what performed it. Report unresolved verification honestly. Use a compact response appropriate to the task rather than a mandatory heading on every reply.

Other skills can reference this skill for a decision trail instead of inventing another format. Keep the column definitions here as the authoritative source.
