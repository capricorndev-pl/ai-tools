---
name: git-commit
description: Analyze staged git changes, summarize the staged diff, draft a concise conventional commit message, and perform the commit only after explicit user approval. Use when Codex is asked to review staged changes, write a commit message, or create a git commit for the current repository without including unstaged work.
---

# Git Commit

## Overview

Review only the staged index, derive a short conventional commit message from the actual diff, and gate `git commit` behind explicit approval. Ignore unstaged changes except to note that they exist and are excluded from the commit.

## Workflow

1. Verify there is staged content before doing message work.
2. Inspect the staged diff, not the full worktree.
3. Propose one concise conventional commit message.
4. Ask for approval before running `git commit`.
5. If approval is granted, commit exactly the staged changes with the approved message.

## Inspect The Right Scope

Use git commands that read the staged index:

- `git status --short`
- `git diff --cached --stat`
- `git diff --cached`

Do not base the commit message on unstaged changes or untracked files. If unstaged work exists, mention that the proposed commit covers staged files only.

If nothing is staged, stop and tell the user there is nothing to commit.

## Write The Message

Use conventional commit format:

- `<type>: <subject>`
- Optional scope only when it materially improves clarity: `<type>(<scope>): <subject>`

Default to a single-line message unless the diff clearly warrants a body and the user asked for more detail. Keep the subject specific and short. Avoid restating filenames unless they are the clearest way to express the change.

Choose the type from the change intent:

- `feat` for user-facing behavior or capability additions
- `fix` for bug fixes or behavioral corrections
- `refactor` for internal restructuring without behavior change
- `docs` for documentation-only changes
- `test` for test-only changes
- `build` for build, tooling, or dependency changes
- `ci` for pipeline or automation changes
- `chore` for maintenance work that does not fit better elsewhere
- `perf` for measurable performance improvements

Subject rules:

- Use imperative mood.
- Prefer lowercase, unless names require casing.
- Keep it concise; aim for about 50 characters and stay well under 72.
- Avoid trailing punctuation.
- Avoid filler such as `update`, `changes`, `misc`, or `stuff` unless the diff truly leaves no better choice.

When the staged diff spans unrelated intents, say so and recommend splitting the commit instead of forcing a vague message.

## Approval Gate

Never run `git commit` without explicit approval in the current conversation. Approval must come after presenting the proposed message.

Before committing:

1. Show a brief summary of what the staged diff does.
2. Present the proposed conventional commit message in backticks.
3. Ask whether to proceed with the commit.

After approval:

1. Run `git commit -m "<approved message>"`.
2. Report the resulting commit hash and subject.
3. If the commit fails, show the reason and stop.

Do not amend, sign, push, or stage additional files unless the user explicitly asks.

## Output Pattern

Use this structure when the user asks for a commit:

```text
Staged summary: <1-3 sentences based on git diff --cached>
Proposed commit: `<type>(optional-scope): <subject>`
Proceed with `git commit` using this message?
```

If the user asks only for a message and not the commit itself, stop after proposing the message.
