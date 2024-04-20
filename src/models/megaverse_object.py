from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class MegaverseObject:

    row: int
    column: int
    name: str

    def is_astral_object(self) -> bool:
        return False

    def to_body(self) -> Dict[str, Any]:
        return {
            "row": self.row,
            "column": self.column
        }

@dataclass
class Space(MegaverseObject):

    name: str = "SPACE"
