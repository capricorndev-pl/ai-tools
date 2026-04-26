---
name: adr-author
description: Draft Architecture Decision Records (ADRs) as single Markdown files that capture one significant technical decision, its context, considered options, outcome, and consequences. Use when Codex needs to write, scaffold, or add an ADR, a decision record, a design decision doc, or a tech decision doc, or when documenting a choice between technical options such as databases, frameworks, libraries, deployment targets, protocols, or patterns. Also use when the user mentions MADR, Nygard ADR, Y-statement, or an `adr/`, `docs/adr/`, or `docs/decisions/` directory.
---

# ADR Author

Create one ADR per architecturally significant decision. An ADR records what was chosen, why it was chosen, what alternatives were considered, and what consequences follow from the decision.

## When This Skill Applies

Use this skill when the task is to:

- write, draft, or scaffold an ADR or decision record
- document a choice between technical options
- add a new decision file under `adr/`, `docs/adr/`, or `docs/decisions/`
- supersede or amend an existing ADR

Do not use this skill for general technical writeups, tutorials, runbooks, or RFCs that are not primarily recording a decision.

## ADR Quality Bar

- Capture exactly one decision. Split separate decisions into separate ADRs.
- State the accepted choice clearly, not as a speculative essay.
- Treat the rejected options seriously with concrete pros and cons.
- Record consequences honestly, including negative ones.
- Preserve history. Supersede accepted ADRs instead of rewriting them in place.
- Keep it short. Most ADRs should remain easy to read on one screen.

## Workflow

1. Gather the decision.

   Confirm you have:
   - the decision itself in one sentence
   - the driving forces behind the choice
   - at least two considered options, including the chosen one
   - concrete rejection reasons for the non-chosen options
   - positive and negative consequences

   If any of these are missing and cannot be inferred safely from the repo or conversation, ask before drafting. Do not invent trade-offs.

2. Pick a template.

   Default to MADR full. If the repository already contains ADRs, inspect one file and match the existing style.

   - MADR full: default for most decisions. See `references/template-madr-full.md`.
   - MADR minimal: use for quick or small decisions. See `references/template-madr-minimal.md`.
   - Nygard: use when the repo already uses it or the user asks for it. See `references/template-nygard.md`.
   - Y-statement: use for a short inline decision summary or when explicitly requested. See `references/template-y-statement.md`.
   - Tyree & Akerman: use only for heavier governance or explicit requests. See `references/template-tyree-akerman.md`.

3. Name the file.

   Use:

   ```text
   NNNN-present-tense-imperative-phrase.md
   ```

   Rules:
   - `NNNN` is a zero-padded four-digit sequence like `0001`
   - use lowercase kebab-case and ASCII only
   - write the slug as an imperative verb phrase such as `use-postgresql`
   - do not prefix the slug with `adr-`
   - do not put dates in the filename

   Run `scripts/next_id.py <adr-dir>` to compute the next ID from an ADR directory.

4. Draft the ADR.

   Fill the chosen template using these rules:
   - Title matches the filename phrase and uses Title Case.
   - Status is one of `Proposed`, `Accepted`, `Rejected`, `Deprecated`, or `Superseded by [NNNN](./nnnn-title.md)`.
   - Date uses ISO format `YYYY-MM-DD`.
   - Only include deciders or reviewers if the user or repo provides them.
   - Context explains the forces and constraints, not a long history.
   - Considered options include every real option the team weighed.
   - Decision outcome states the winner and the decisive reason.
   - Consequences include positive, negative, and unknown effects where relevant.
   - Links use relative paths for related ADRs in the same repository.

5. Verify before presenting.

   Check that:
   - the ADR records exactly one decision
   - the rejected options have concrete reasoning
   - the chosen option still includes trade-offs
   - at least one negative consequence is documented
   - the filename, status, date, and links are complete
   - the total length is proportionate, usually about 150 to 600 words

6. Write the file.

   If an ADR directory already exists, place the file there. Otherwise ask where it should live or default to `docs/adr/`.

   If the new ADR supersedes an earlier one:
   - update the older ADR status to point at the new file
   - add a reciprocal supersession link in the new ADR
   - do not delete the older ADR

## Common Mistakes

- Writing a proposal instead of a recorded decision
- Listing only the winning option's strengths
- Hiding the actual decision deep in the document
- Omitting negative consequences
- Letting a second decision creep into the same file
- Rewriting history instead of superseding prior ADRs

## References

- `references/template-madr-full.md`
- `references/template-madr-minimal.md`
- `references/template-nygard.md`
- `references/template-y-statement.md`
- `references/template-tyree-akerman.md`
- `references/examples.md`
- `scripts/next_id.py`
