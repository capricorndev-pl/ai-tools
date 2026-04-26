# Nygard template

Michael Nygard's original 2011 format. Use when the target repo is already Nygard-style, or when the user explicitly asks. Minimal by design — it doesn't enumerate options with pros/cons; that analysis lives in the Context section as prose.

```markdown
# {NNNN}. {Short imperative title}

Date: {YYYY-MM-DD}

## Status

{Proposed | Accepted | Deprecated | Superseded by ADR-NNNN}

## Context

{The forces at play — technological, political, social, project-local. Describe the problem and the considered options as flowing prose, not a bulleted list. End with the question to be answered.}

## Decision

{The change being made. Stated in full sentences, active voice. "We will …"}

## Consequences

{What becomes easier or harder because of this change. Include both good and bad follow-on effects. New ADRs that this decision will likely trigger belong here.}
```

Nygard ADRs are usually **shorter** than MADR ADRs because the analysis is compressed into the Context section. Don't pad them to look like MADR.
