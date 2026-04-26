---
name: openspec-cherry
description: Implement one selected task or a limited subset of tasks from an OpenSpec change tasks file. Use when the user wants a cherry-picked OpenSpec implementation instead of applying every pending task.
---

# OpenSpec Cherry

Implement only the selected task or explicitly bounded task subset from an OpenSpec change.

## Input

Accept a change name plus one of:

- a task number, such as `2` or `2.1`
- a small task range, such as `2-4`
- a short task description that clearly matches one pending task
- an explicit instruction such as "next task only"

If the change or task scope is ambiguous, stop and ask for clarification before editing files.

## Workflow

1. **Select the change**

   If a change name is provided, use it. Otherwise infer it from conversation context only when clear.

   If no clear change can be inferred, run:

   ```bash
   openspec list --json
   ```

   Then ask the user which change to use.

2. **Read status**

   ```bash
   openspec status --change "<name>" --json
   ```

   Use the JSON to identify the schema and task artifact.

3. **Get apply instructions**

   ```bash
   openspec instructions apply --change "<name>" --json
   ```

   If the change is blocked or has no tasks, report that and stop.

4. **Read context files**

   Read the files listed in `contextFiles`. Do not assume specific file names; use the CLI output.

5. **Resolve the cherry scope**

   Identify exactly which pending task or tasks are in scope.

   Guardrails:

   - Prefer one task.
   - Accept a limited subset only when the user explicitly requested it.
   - Do not silently expand scope to adjacent tasks.
   - If a requested task is already complete, say so and ask before doing related work.
   - If the requested task depends on an incomplete prerequisite, pause and explain the dependency.

6. **Implement only the selected scope**

   For each selected task:

   - Announce the task being worked on.
   - Make minimal code or doc changes needed for that task.
   - Mark only that task complete in the tasks file after implementation is done.
   - Leave unrelated pending tasks untouched.

7. **Stop after the selected scope**

   Show what was completed, what remains, and any verification the user should run.

## Output Pattern

```text
Using change: <change-name>
Cherry scope: <task number or short description>

Completed:
- [x] <task>

Remaining tasks were left untouched.
```

## Guardrails

- Do not loop through all remaining tasks.
- Do not mark unchecked tasks complete unless they were explicitly selected and implemented.
- Do not broaden scope because nearby work is convenient.
- Ask before changing OpenSpec artifacts when implementation reveals a spec issue.
- Follow repository command restrictions for validation commands.
