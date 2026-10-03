---
name: unslop
description: >-
  Edit assistant explanations and engineering prose for concrete, readable
  language. Use for technical answers, README files, documentation, runbooks,
  PR descriptions, commit messages, and engineering summaries. Humanizer owns
  scripts, narration, resumes, cover letters, and other voice-focused writing;
  engineering narration uses only this skill's supporting clarity reference.
  For agent instructions, preserve routing, requirements, and completion
  criteria. Writing-for-agents owns their instruction structure.
license: MIT
metadata:
  source: https://github.com/cursor/plugins/tree/main/pstack/skills/unslop
  adaptation: Adam's technical prose, voice routing, and agent-instruction safeguards
---

# Unslop

Edit technical prose to remove empty or formulaic language.

## Scope and routing

Apply this editorial pass to assistant explanations and engineering prose.
For your own technical answers, deliver the answer without announcing each
editing rule or adding a rewrite report. For an existing file, preserve its
structure and make only the edits the user requested.

[Writing-for-agents](../writing-for-agents/SKILL.md) owns the structure and
operational requirements of agent instructions. Apply this prose pass once
those requirements are defined. Editing their wording does not require
restarting the authoring workflow.

When editing agent instructions, preserve their triggers, command text,
paths, identifiers, contract headings, obligations, exceptions, and observable
completion criteria. Do not remove a necessary repeated warning, definition,
or point-of-action reminder merely to reduce repetition. Keep technical terms
that have an established meaning in the procedure. Change formatting or
sequence only within the requested editing scope. If clearer prose would
require changing the workflow, identify that as a separate proposed change.

[Humanizer](../humanizer/SKILL.md) remains the primary editor for scripts,
narration, resumes, cover letters, application answers, and other writing
where a person's voice matters. For engineering-video narration, use only
[the narration clarity reference](references/engineering-narration-clarity.md)
within humanizer's workflow. Do not run this whole catalog over narration.
Explicit requests to use either skill take precedence over this default.

Treat patterns as editing signals, not evidence of authorship. Follow
explicit user preferences, including the punctuation rules below. Preserve
useful technical terms, actual uncertainty, and authentic voice. Project
instructions and voice profiles govern the remaining style choices. Reduce
repetition without stripping the mechanism,
conditions, or technical detail needed to understand the point. Do not
invent facts, measurements, causes, examples, or stronger conclusions to
make a sentence more concrete. When evidence is thin, say less or state
the uncertainty.


## Process

1. Scan for the patterns below.
2. Rewrite. Preserve meaning, match intended tone.

## Patterns to detect and fix

Rule numbers are stable ids that other skills cite. A removed rule leaves a gap.

### Content

3. **Superficial -ing phrases.** "highlighting...", "ensuring...", "reflecting...", "showcasing...", "fostering...". Delete or expand with real sources.
5. **Vague attributions.** "Experts believe", "Industry reports suggest", "Some critics argue". Name the source or delete.

### Language

7. **AI vocabulary.** Additionally, crucial, delve, enduring, enhance, fostering, garner, interplay, intricate, landscape (abstract), pivotal, showcase, tapestry (abstract), testament, underscore, vibrant. Prefer a plain word when it preserves the intended meaning; keep a precise term that earns its place.
8. **Fancy ways to say "is".** "serves as", "stands as", "boasts", "features". Just say "is" or "has".
9. **"Not just X, but Y."** State the point directly instead.
10. **Rule of three.** Forcing ideas into groups of three. Use the natural number.
11. **Synonym cycling.** Protagonist, main character, central figure, hero all in one paragraph. Pick one, repeat it.
12. **False ranges.** "from X to Y" where X and Y aren't on a meaningful scale. List topics directly.

### Style

13. **Punctuation.** Do not use em dashes in authored prose. Parentheses may define an acronym in any register, such as "application programming interface (API)". Otherwise, use parentheses sparingly and only in casual text. In more formal writing, integrate an aside into the sentence or give it a separate sentence. Prefer periods to semicolons when separating independent clauses. Preserve punctuation required by code, commands, formulas, or verbatim quotations.
14. **Colon overuse.** Colons are fine before a list or example. Not as mid-sentence connectors. "If you're coming from traditional automation: instead of registering event handlers, you describe conditions" adds nothing with the colon. Rewrite to let the point stand on its own without comparison framing. "Describing when the scheduler should fire works best as plain English." Same meaning, no crutch punctuation.
15. **Boldface overuse.** Don't bold every proper noun or acronym.
16. **Inline-header lists.** The tell is a bold label and colon that restates the line: "**Performance:** Performance improved...". Convert those to prose. A bold lead-in that ends in a period, names the item, and is followed by genuinely new detail ("**Schema in TypeScript.** Tables live in one file.") is fine, not a tell.
17. **Title case headings.** Use sentence case.
18. **Decorative emojis.** Remove from headings and bullets.
19. **Quotation consistency.** Match the document convention. Preserve meaningful typography and do not alter quoted source text or code merely to normalize punctuation.

### Communication artifacts

20. **Chatbot phrases.** "I hope this helps!", "Let me know if...", "Of course!", "Certainly!", "Found the smoking gun!" Remove.
22. **Sycophantic tone.** "Great question! You're absolutely right!" Respond directly.

### Filler

23. **Filler phrases.** "In order to" becomes "To". "Due to the fact that" becomes "Because". "It is important to note that" gets deleted.
24. **Excessive hedging.** "could potentially possibly be argued that it might" becomes "may".
25. **Generic conclusions.** "The future looks bright." State specific plans or facts.

### Jargon

26. **Abstract metaphor nouns.** Substrate, wedge, vector, locus, vantage, nexus, primitive (as noun), harness (as metaphor), surface (as in "API surface"), bedrock, scaffolding (as metaphor), modality, paradigm, gold-plating, ratchet (as metaphor), evacuate (for moving code), endgame, north star, flywheel. These read as technical but usually have a plainer concrete word. "Substrate" becomes "base". "Wedge in" becomes "add". "Vector" becomes "way" or "method". "Gold-plating" becomes "more than the job needs". "Ratchet" becomes the mechanism's real name or "a limit that only tightens". "Evacuate" becomes "move out". "Endgame" becomes "the last phase". Prefer the concrete word when the metaphor obscures the mechanism. Keep established technical terms when they are accurate and useful.

### Plain speech

27. **Say what it does, not how it feels.** "the database stays close at hand", "SQL you can read", "types that follow your schema" name a feeling. The fix names the mechanism or a number: "`.toSQL()` returns the exact string sent to the database", "a column rename fails the build". Ask what the sentence tells the reader to do or know, then write that. If the sentence makes an unsupported claim, remove or qualify it. Ask whether a generic sentence contributes necessary context before cutting it. Use only evidence available from the source or task.
28. **Shorten or split dense sentences.** If the reader has to backtrack to parse a sentence, break it in two or drop clauses. Keep related reasoning together when it reads clearly. Vary sentence lengths rather than imposing uniformly short sentences.
29. **Active voice.** Prefer it. Catch "is/are/was/were + past participle" and name the actor: "queries are validated" becomes "the compiler validates queries", "the file is parsed by the loader" becomes "the loader parses the file". Passive is fine only when the actor is unknown or genuinely doesn't matter.
30. **Cut adverbs, or use a stronger verb.** "runs quickly" becomes "is fast" or the number. "significantly improves" becomes the measured delta. An adverb propping up a weak verb means the verb is wrong.
31. **Prefer the plain word.** "utilize" becomes "use", "leverage" becomes "use", "facilitate" becomes "help", "numerous" becomes "many", "in the event that" becomes "if". Retain a formal register or specific domain term when the project voice or meaning calls for it.
32. **Mannered prose.** Metaphor or flourish where a literal phrase exists: aphorisms ("wire it or delete it"), rhetorical fragments for effect, personified code ("the plan holds it"), figurative verbs ("rides along", "stands on"), stock framing phrases. "A dial worth turning" becomes "a parameter worth varying". Say what you mean. Rule 26 covers the metaphor nouns.
33. **Over-compression.** Dropped articles, verbless fragments, symbol-speak, and abbreviations that make the reader decode instead of read. "Parser rejects bad date → exit 2, no write" becomes "The parser rejects a bad date, exits with code 2, and writes nothing." Write complete prose when fragments make the reader decode the point. Keep useful diagrams, established abbreviations, code, and compact reference notation.

## Final check

Read the result as the intended audience. Revert edits that change meaning,
erase important detail, overstate certainty, or produce a monotonous rhythm.
Keep API names, commands, quoted text, and factual claims accurate.

For agent instructions, compare the edited text with the original requirements
and any explicitly approved changes. Confirm that the same work is required
under the same conditions, with the same limits and evidence.
