from dataclasses import dataclass
from typing import Dict, Any, Optional

from models.megaverse_object import MegaverseObject


@dataclass
class AstralObject(MegaverseObject):

    path_resource: str

    def is_astral_object(self) -> bool:
        return True

@dataclass
class POLYanet(AstralObject):

    name: str = "POLYANET"
    path_resource: str = "polyanets"


@dataclass
class ComETH(AstralObject):

    name: str = "COMETH"
    path_resource: str = "comeths"
    direction: Optional[str] = None

    def to_body(self) -> Dict[str, Any]:
        body = super().to_body()
        body["direction"] = self.direction
        return body


@dataclass
class SOLoon(AstralObject):

    name: str = "SOLOON"
    path_resource: str = "soloons"
    color: Optional[str] = None

    def to_body(self) -> Dict[str, Any]:
        body = super().to_body()
        body["color"] = self.color
        return body
