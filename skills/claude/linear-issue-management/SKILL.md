---
name: linear-issue-management
description: >
  Create well-structured Linear issues or triage items from repo, product,
  bug, audit, or planning context. Use when Claude needs to file new Linear
  work, decide between an implementation issue vs a triage item, choose
  project/category/priority, write consistent Linear descriptions, or
  update issue metadata for Linear audit trails.
metadata:
  author: piotr.swiecik@gmail.com
  version: "1.0"
---

# Linear Issue Management

## Overview

Create Linear items with the right project, status, label, and description shape. Prefer precise inference from current context; ask only when project or item type cannot be determined safely.

## Required Workflow

1. Read enough context to understand the requested work: user message, current repo, relevant `CLAUDE.md` / `AGENTS.md`, active OpenSpec change, recent commits, logs, screenshots, SQL evidence, or linked issue.
2. Inspect Linear before writing:
   - List projects when project is not already certain.
   - List teams/statuses/labels as needed to use exact workspace names.
   - Search existing issues by key phrases when there is duplicate risk.
3. Decide item type:
   - Create an **issue** for scoped, implementable work or a confirmed bug/feature/improvement.
   - Create a **triage item** for unclear product intent, policy decisions, research, audit/debug-retention discussions, or future design exploration.
   - Ask the user only when the evidence genuinely supports both.
4. Create the Linear item in an inferred project. Never create items in the generic workspace without a project unless the user explicitly asks.
5. Report the Linear identifier and URL.

## Project Inference

Infer the project from the strongest available signal:

- Explicit user instruction wins.
- Repository instructions in `CLAUDE.md`, `AGENTS.md`, or local workflow docs are next.
- Repo/app naming conventions are next; compare repository names, package/project names, application names, and domain terms against Linear project names.
- If no project can be inferred, ask the user for the project before creating anything.

## Issue vs Triage

Use an **issue** when:

- The behavior is confirmed and actionable.
- The expected fix can be described in acceptance criteria.
- The user asks to implement, fix, add, document, or configure something.
- The item should enter normal backlog planning.

Use **triage** when:

- The user asks for a discussion item, future decision, research, audit policy, or product clarification.
- Requirements are intentionally unresolved.
- The next step is deciding scope, not implementing.

Do not put "triage" in the title to simulate triage. Set the Linear state/status to the workspace's real `Triage` status.

## Metadata Rules

- **Status**:
  - For implementation issues, let the item land in the workspace default backlog state unless a status is explicitly requested or the default is known to be wrong.
  - For triage items, explicitly set state/status to `Triage`.
- **Project**: Always set one.
- **Assignee/owner**: Do not assign an owner. Omit `assignee`; do not use `me`.
- **Priority**: Set only when clearly deduced from current context. Otherwise omit it.
- **Due dates, milestones, cycles**: Do not set. These are user responsibilities.
- **Labels/category**: Use existing labels when the category is clear:
  - `Bug`: broken behavior, regression, error, incorrect state, data loss, security or reliability defect.
  - `Feature`: new user-facing capability.
  - `Improvement`: configuration, UX refinement, documentation/process improvement, non-bug enhancement.
  - For triage, labels are optional; set only for clear-cut cases.

## Priority Guidance

Only set priority when evidence makes it defensible:

- Urgent: production-down, data loss/corruption, security exposure, or blocked critical workflow.
- High: confirmed user-blocking bug, audit/compliance risk, or repeated manual test failure in core flow.
- Normal/Low: use only when the user states it or the context has an explicit planning convention.

When uncertain, leave priority blank.

## Issue Description Template

Use this exact section order. Omit `Severity` only when it is not clearly supported.
When style calibration is useful, inspect a few existing high-quality issues in the same Linear project before drafting.

```markdown
## Severity

<Optional: Urgent/High/Normal/Low plus one sentence of evidence.>

## Summary

<One short paragraph describing the issue in plain English.>

## Evidence

<Concrete observations: reproduction steps, logs, SQL facts, screenshots, commits, file paths, API responses, or user report. Avoid speculation.>

## Impact

<Who is affected and why it matters. Include examples and user stories when useful, e.g. "As a workflow author, I need...">

## Suggested Fix

<A practical direction or acceptance criteria. If the exact fix is unknown, describe the investigation boundary and expected outcome.>
```

## Triage Description Template

Use this exact section order.
When style calibration is useful, inspect an existing high-quality triage item in the same Linear project before drafting.

```markdown
## Context

<What prompted the discussion and what is known today.>

## Open Questions

<Questions that must be answered before implementation.>

## Out of Scope

<Decisions or implementation work that should not happen in this triage item.>

## Next Steps

<Concrete follow-up: decide, draft ADR/spec, split implementation issue, gather evidence, or close as not needed.>
```

## Title Rules

- Write a short descriptive English title.
- Do not prefix with Linear key, project name, "Triage:", or "Bug:".
- Prefer outcome/problem language: `Configure scratch artifact root path`, `Run UI remains queued after backend run completes`.

## Quality Bar

- Do not create vague catch-all items.
- Do not overstate severity, priority, or certainty.
- Prefer one item per decision or implementation slice.
- Link related issues when known instead of duplicating context in multiple places.
- If filing from a resolved/implemented finding, mention the fixing commit or current status in Evidence.
