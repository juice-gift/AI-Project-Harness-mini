# AI Project Harness Mini

A lightweight project-local workflow skill for preserving critical project context, task scope, and verification state across AI-assisted software development sessions, including session restarts and context compaction.

## Why

Long-running AI-assisted coding work can lose continuity across sessions. A new coding-agent session may not know what the project is, what has already been completed, what the current task is, which files it may modify, or whether previous work was actually verified.

AI Project Harness Mini keeps these facts in project-local Markdown files instead of relying only on chat history.

## Core Workflow

```text
Codex enters project
        ↓
reads SKILL.md
        ↓
reads PROJECT.md
        ↓
reads STATE.md
        ↓
reads TASK.md
        ↓
performs current task
        ↓
runs real verification
        ↓
updates STATE.md / TASK.md
        ↓
next session can continue
```

## Project Files

### `PROJECT.md`

Stable project information: purpose, goal, tech stack, architecture, and long-term constraints.

Answers: **What is this project?**

### `STATE.md`

Current project state: phase, completed work, current task reference, known issues, latest verification, and next step.

Answers: **Where is the project now?**

### `TASK.md`

Current work boundary: objective, allowed scope, prohibited scope, acceptance criteria, required verification, and status.

Answers: **What am I allowed to do now, and what counts as done?**

## Three v0.1 Behaviors

### Context Recovery

A new session can recover project and task state from project-local files.

### Scope Control

The current task defines what may and may not be modified.

### Verification Integrity

Changing code is not enough. A task may be marked `Completed` only after the required verification actually succeeds and project state is synchronized.

## Repository Structure

```text
AI-Project-Harness-Mini/
├── README.md
├── SKILL.md
├── EVALUATION.md
├── templates/
│   ├── PROJECT.template.md
│   ├── STATE.template.md
│   └── TASK.template.md
└── demo/
    ├── PROJECT.md
    ├── STATE.md
    ├── TASK.md
    ├── src/
    │   ├── __init__.py
    │   └── math_utils.py
    └── tests/
        └── test_math_utils.py
```

## Usage

1. Copy the three templates into a software project as `PROJECT.md`, `STATE.md`, and `TASK.md`.
2. Fill them with the project's actual information.
3. Make `SKILL.md` available in the project.
4. Start a new Codex session in that repository.
5. Give Codex a short instruction such as:

   ```text
   Read the project-local SKILL.md and follow its workflow.
   Recover the current project state from the project files, then continue the current task.
   ```

6. After the run, inspect the modified files, verification commands actually executed, `STATE.md`, and `TASK.md`.

This v0.1 does not claim that Codex automatically discovers `SKILL.md`. It demonstrates that Codex can follow the project-local workflow when instructed to read the file.

## Demo

The included demo began from an intentional incomplete baseline:

- `clamp()` raised `NotImplementedError`;
- all 7 tests failed;
- `TASK.md` was `Pending`.

A new Codex session then recovered the task from the Harness files, implemented `clamp()`, modified only the permitted implementation and state files, ran the required `unittest` command, passed all 7 tests, synchronized project state, and set the task to `Completed`.

The following commits provide a simple before-and-after demonstration:

```text
6aee044 Initialize AI Project Harness Mini v0.1 baseline
a9f80b0 Complete demo task with harness workflow
```

## Manual Evaluation

| Evaluation             | Result |
| ---------------------- | ------ |
| Context Recovery       | PASS   |
| Scope Control          | PASS   |
| Verification Integrity | PASS   |

See [EVALUATION.md](EVALUATION.md) for the detailed manual evidence. These results demonstrate this demo scenario only; they do not generalize to every model, agent, repository, or operating system.

## Non-Goals for v0.1

AI Project Harness Mini v0.1 intentionally does not include:

- an automated benchmark framework;
- an evaluation runner;
- an LLM judge;
- trajectory analysis;
- a complex verifier;
- `skill-eval-harness` integration;
- large baseline-vs-harness experiments;
- multi-agent platform support;
- cross-platform runtime compatibility research;
- a sandbox system;
- a database;
- a backend service;
- a Web UI.

## Status

AI Project Harness Mini v0.1 has completed its core demo, and all three defined manual evaluations passed. This does not mean the project is universally validated or production proven.
