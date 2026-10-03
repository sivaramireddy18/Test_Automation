"""Canonical intermediate representation for extracted C APIs."""
from dataclasses import asdict, dataclass, field
from typing import Any

@dataclass
class Parameter:
    name: str
    type: str
    direction: str = "unknown"
    pointer_depth: int = 0
    array: str | None = None

@dataclass
class Function:
    name: str
    return_type: str
    parameters: list[Parameter] = field(default_factory=list)
    source: str | None = None

@dataclass
class Enum:
    name: str
    values: dict[str, int | str] = field(default_factory=dict)

@dataclass
class Field:
    name: str
    type: str

@dataclass
class Struct:
    name: str
    fields: list[Field] = field(default_factory=list)

@dataclass
class ApiIR:
    schema_version: str = "0.1"
    library: str = "STM32"
    functions: list[Function] = field(default_factory=list)
    enums: list[Enum] = field(default_factory=list)
    structs: list[Struct] = field(default_factory=list)
    typedefs: dict[str, str] = field(default_factory=dict)
    constants: dict[str, int | str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
