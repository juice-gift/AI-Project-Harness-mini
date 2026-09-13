---
name: ai-project-harness-mini
description: A lightweight project-local workflow skill for maintaining project context, task scope, and verification state across AI-assisted software development sessions.
---

# AI Project Harness Mini

Use this workflow to recover project context, enforce the current task boundary, and keep verification state truthful.

## Startup

Before working on a project task, read these files in order:

1. `PROJECT.md` — understand the project goals, technology stack, architecture, and stable constraints.
2. `STATE.md` — understand the current phase, completed work, known issues, latest verification results, and next step.
3. `TASK.md` — understand the current objective, allowed and prohibited modification scope, acceptance criteria, and task status.

Use all three files to establish the project context, current state, and task boundary. If information required for the current work is missing or conflicts across the files, do not guess; report the problem explicitly.

## Scope Control

- Complete only the current task defined in `TASK.md`.
- Modify only the files and areas that the task allows.
- Do not expand scope for incidental cleanup, aesthetics, speculative future needs, or unrelated improvements.
- If completion requires a change outside the allowed scope, stop that part of the work and report why it is required.
- Never expand the task boundary silently.

Treat an explicit user request to change the current scope as a task scope change. Follow the user's instruction, but clearly identify the change instead of silently bypassing `TASK.md`.

## Verification Integrity

An implementation is not complete merely because the code was changed.

After implementation:

1. Run real tests or verification based on the acceptance criteria in `TASK.md`.
2. Record the verification method actually executed and its actual result.
3. Mark the task complete only when verification succeeds.
4. If verification fails, cannot run, or remains uncertain, do not claim completion.
5. Record failed, blocked, or unverified status truthfully in the state files.

Never infer that tests passed because the code looks correct.

## State Update

At the end of the task, update `STATE.md` and `TASK.md` from facts that actually occurred and results that were actually verified. Ensure a new Codex session can determine:

- what the project is;
- how far it has progressed;
- what the current task is;
- whether the current task has been verified;
- what should happen next.

Do not use chat history as the only source of project state.

## Completion Rule

Declare the current task complete only when all four conditions are true:

```text
implementation complete
+ acceptance criteria satisfied
+ actual verification successful
+ STATE.md and TASK.md synchronized
```

Otherwise, report the current status accurately.

## Task Scope Changes

The user may explicitly change the current task or its scope.

When that happens:

- treat it as an explicit task scope change;
- clearly identify the change;
- update the relevant project state before relying on the new scope;
- never expand the task silently.
