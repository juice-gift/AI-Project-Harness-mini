# Project State

## Current Phase

Initial implementation

## Completed

- Demo project structure created.
- Existing tests for `clamp()` created.

## Current Task

Implement `clamp()` so that the existing tests pass.

## Known Issues

- `clamp()` is not implemented.
- The current tests are therefore expected to fail.

## Latest Verification

`python -m unittest discover -s tests -v`

Result: FAIL — 7 tests ran with 7 errors because `clamp()` raised `NotImplementedError: clamp is not implemented yet`.

## Next Step

Read `TASK.md`, implement the current task, and run the specified tests.
