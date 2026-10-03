# Architecture

## Goal

Convert STM32 C/PDL APIs into a canonical machine-readable representation and generate bindings consumed by a Python/pytest validation layer.

## Pipeline

1. Input: STM32 HAL/LL/PDL headers and configuration headers.
2. Extraction: Clang AST resolves functions, typedefs, enums, structures, pointers, arrays and eventually callbacks.
3. IR: schema/api.schema.json defines the stable API contract.
4. Generation: deterministic C .h/.c wrappers and Python facade.
5. Execution: pytest-based validation tests.
6. Transport: board communication stays separate from generated API code.
7. Results: structured logs, SQLite results and HTML reports will be added.

## Design rule

Generated code must never contain hand-written test logic. Regeneration must be safe and deterministic.
