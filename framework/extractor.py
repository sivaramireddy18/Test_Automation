"""Initial extractor interface.

Production extraction will use Clang AST. This boundary is intentionally
separate from generation so the same IR can support other parsers later.
"""
import json
from pathlib import Path
from .ir import ApiIR

def write_ir(ir: ApiIR, path: str | Path) -> None:
    Path(path).write_text(json.dumps(ir.to_dict(), indent=2) + "\n", encoding="utf-8")

def read_ir(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))
