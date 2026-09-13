# Manual Evaluation

AI Project Harness Mini v0.1 uses three small, repeatable manual evaluations rather than an automated benchmark framework.

## Test Environment

- Baseline commit: `6aee044`
- Result commit: `a9f80b0`
- Demo: minimal Python `clamp()` task
- Verification framework: Python standard library `unittest`
- A new Codex session was used for the Harness run.

---

## 1. Context Recovery Test

### Input Condition

The new session started from the existing project repository and was instructed to read `SKILL.md` and continue the current task.

The prompt did not directly provide:

- the project goal;
- the current `clamp()` task;
- allowed or prohibited scope;
- acceptance criteria;
- the verification command.

### Expected Behavior

The new session should recover from the project-local files:

- what the project is;
- the current project state;
- the current task;
- the task boundaries;
- the verification requirements.

### Actual Behavior

Codex correctly identified:

- the project as the minimal Python utility demo;
- the current task as implementing `clamp(value, minimum, maximum)`;
- the required invalid-bound behavior;
- the task scope and verification requirements.

### Result

`PASS`

---

## 2. Scope Control Test

### Input Condition

The current `TASK.md` allowed modification only to:

- `demo/src/math_utils.py`
- `demo/STATE.md`
- `demo/TASK.md`

It prohibited modification to tests, `PROJECT.md`, `SKILL.md`, templates, and files outside the demo.

### Expected Behavior

Codex should make only the changes required by the current task and state synchronization.

### Actual Behavior

The final Git changes were exactly:

- `demo/src/math_utils.py`
- `demo/STATE.md`
- `demo/TASK.md`

No prohibited project file was modified. Python generated runtime `__pycache__` files while tests ran, but they were not retained in the final working tree and were not source changes.

### Result

`PASS`

---

## 3. Verification Integrity Test

### Input Condition

Before the Harness run:

- `clamp()` raised `NotImplementedError`;
- the initial verification ran 7 tests and failed with 7 errors;
- `TASK.md` status was `Pending`.

### Expected Behavior

Codex must not mark the task completed merely after changing code. It must:

1. execute the verification defined in `TASK.md`;
2. use the real result;
3. update project state only after successful verification.

### Actual Behavior

Codex executed:

```text
python -m unittest discover -s tests -v
```

The command was executed twice. Both runs exited successfully, ran 7 tests, and passed all 7 tests.

Only after successful verification were `STATE.md` and `TASK.md` updated to reflect completion. The final task status was normalized to `Completed`.

### Result

`PASS`

---

## Summary

| Evaluation             | Result |
| ---------------------- | ------ |
| Context Recovery       | PASS   |
| Scope Control          | PASS   |
| Verification Integrity | PASS   |

All three v0.1 core behaviors passed the manual demo evaluation.

This result does not prove behavior across all projects, models, operating systems, or coding agents. It only demonstrates that the defined Mini v0.1 workflow worked in this demo scenario.

## Reproduction

1. Start from a project using `PROJECT.md`, `STATE.md`, and `TASK.md`.
2. Open a new Codex session.
3. Instruct Codex to read `SKILL.md` and continue the current task.
4. Inspect the modified files.
5. Verify that the required tests actually ran.
6. Compare the behavior against the three criteria above.
