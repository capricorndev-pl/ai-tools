# Tyree & Akerman template

From the 2005 IEEE paper "Architecture Decisions: Demystifying Architecture" (Capital One). Heavier than MADR or Nygard. Use only when the context demands it: regulated industries, formal governance, enterprise review boards, or when the user explicitly asks.

```markdown
# {Title}

## Issue
{The architectural question being addressed. No ambiguity about why this is being addressed now.}

## Decision
{The chosen position.}

## Status
{Pending | Decided | Approved}

## Group
{Optional grouping: integration | presentation | data | security | …}

## Assumptions
{Environmental assumptions — cost, schedule, technology standards, constraints accepted as given.}

## Constraints
{Additional constraints that the chosen option imposes.}

## Positions
{All viable options considered, each with enough detail that a reviewer won't ask "did you consider …?". Include rejected ones fully.}

## Argument
{Why the chosen Decision is best given Assumptions, Constraints, and Positions.}

## Implications
{Downstream effects: new decisions triggered, requirements modified, scope or schedule impact, training needed, operational changes.}

## Related decisions
{Links to other ADRs, upstream or downstream.}

## Related requirements
{Business requirements, NFRs, or ASRs this decision addresses. Decisions should be business-driven.}

## Related artifacts
{Design docs, diagrams, models, prototypes.}

## Related principles
{Architectural principles, standards, or policies invoked.}

## Notes
{Meeting notes, dissenting opinions worth preserving, review history.}
```

This template is **deliberately heavyweight**. If a section has nothing to say, cut it rather than writing filler — empty sections signal that a lighter template would have been a better fit.
