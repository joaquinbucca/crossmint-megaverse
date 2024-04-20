from typing import List, NoReturn

from models.megaverse_object import MegaverseObject


class InvalidCoordinateException(Exception):

    def __init__(self, row: int, column: int) -> None:
        super().__init__(f"This coordinate ({row}, {column}) is invalid in this board")


class MegaverseGoalBoard:

    board: List[MegaverseObject]

    def __init__(self, board: List[MegaverseObject]):
        self.board = board

    def __iter__(self):
        for megaverse_obj in self.board:
            yield megaverse_obj
