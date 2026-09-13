# Current Task

## Objective

Implement `clamp(value, minimum, maximum)` with the following behavior:

- Return `minimum` when `value < minimum`.
- Return `maximum` when `value > maximum`.
- Otherwise, return `value`.
- Raise `ValueError` when `minimum > maximum`.

## Allowed Scope

- `src/math_utils.py`
- `STATE.md`
- `TASK.md`

`STATE.md` and `TASK.md` may be modified so the Harness can synchronize project state after the task.

## Prohibited Scope

- `PROJECT.md`
- `tests/`
- `src/__init__.py`
- Any file outside the demo
- The Harness root `SKILL.md`
- The Harness templates

## Acceptance Criteria

- `clamp()` correctly handles a value below `minimum`.
- `clamp()` correctly handles a value above `maximum`.
- `clamp()` correctly handles a value within the range.
- `clamp()` behaves correctly when `minimum == maximum`.
- `clamp()` raises `ValueError` when `minimum > maximum`.
- All existing automated tests pass.
- No prohibited scope is modified.

## Verification

Run:

```text
python -m unittest discover -s tests -v
```

Determine task completion from the actual command result.

## Status

Completed
