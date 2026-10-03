# STM32 Validation Test Automation Framework

API-driven automation framework for STM32 PDL/HAL libraries.

## Initial architecture

```text
STM32 PDL/HAL headers -> C AST/API extractor -> canonical JSON IR
                                      |
                         +------------+------------+
                         |                         |
                    C wrapper generator      Python generator
                         |                         |
                       .c/.h                      .py
                         |                         |
                         +------------+------------+
                                      |
                              pytest validation
```

## Planned components

- STM32 C header/API extraction using Clang AST
- Canonical JSON representation of functions, typedefs, enums and structures
- Generated C wrappers (`.c`/`.h`)
- Generated Python API
- pytest-based validation execution
- Structured logging and result reporting
- Hardware/transport abstraction for board automation

## Project status

Early architecture / bootstrap stage. The first milestone is a working STM32 API extractor and deterministic C/Python code generator.
