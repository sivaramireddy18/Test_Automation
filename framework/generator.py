"""Deterministic C/Python wrapper generation from the canonical IR."""
from pathlib import Path
from .ir import ApiIR

def generate_c(ir: ApiIR, out_dir: str | Path) -> None:
    out = Path(out_dir)
    inc = out / "include"
    src = out / "src"
    inc.mkdir(parents=True, exist_ok=True)
    src.mkdir(parents=True, exist_ok=True)
    header = ["#pragma once", "#include <stdint.h>", "", "/* Generated file. Do not edit. */", ""]
    source = ['#include "stm32_generated.h"', "", "/* Generated file. Do not edit. */", ""]
    for fn in ir.functions:
        params = ", ".join(f"{p.type} {p.name}" for p in fn.parameters) or "void"
        header += [f"{fn.return_type} stm32_{fn.name}({params});", ""]
        args = ", ".join(p.name for p in fn.parameters)
        call = f"    {fn.name}({args});" if fn.return_type == "void" else f"    return {fn.name}({args});"
        source += [f"{fn.return_type} stm32_{fn.name}({params})", "{", call, "}", ""]
    (inc / "stm32_generated.h").write_text("\n".join(header), encoding="utf-8")
    (src / "stm32_generated.c").write_text("\n".join(source), encoding="utf-8")

def generate_python(ir: ApiIR, out_dir: str | Path) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    lines = ['"""Generated STM32 API facade."""', "", "# Generated file. Do not edit.", ""]
    for fn in ir.functions:
        params = ", ".join(p.name for p in fn.parameters)
        lines += [f"def {fn.name}({params}):", '    """Call the corresponding generated C binding."""',
                  f"    raise NotImplementedError({fn.name!r})", ""]
    (out / "stm32_api.py").write_text("\n".join(lines), encoding="utf-8")
