from typing import Type, Dict

from models.astral_objetcs import POLYanet, SOLoon, ComETH
from models.megaverse_object import MegaverseObject, Space


class MegaverseObjectNotSupported(Exception):

    def __init__(self, object_name: str):
        super().__init__(f"Metaverse object {object_name} is currently not supported.")


class MegaverseFactory:

    @staticmethod
    def create_megaverse_object(object_name: str, row: int, column: int) -> MegaverseObject:

        if object_name == Space.name:
            return Space(row, column)

        if object_name == POLYanet.name:
            return POLYanet(row, column)

        if SOLoon.name in object_name:
            color = parse_object_attribute(object_name)
            return SOLoon(row, column, color=color)

        if ComETH.name in object_name:
            direction = parse_object_attribute(object_name)
            return ComETH(row, column, direction=direction)

        raise MegaverseObjectNotSupported(object_name)


def parse_object_attribute(full_name: str) -> str:
    split_name = full_name.split("_")

    if len(split_name) <=1:
        raise MegaverseObjectNotSupported(full_name)

    return split_name[0].lower()
