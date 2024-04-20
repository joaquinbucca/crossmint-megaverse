from typing import Type

from factories.megaverse_factory import MegaverseFactory, MegaverseObjectNotSupported
from models.astral_objetcs import POLYanet, SOLoon, ComETH
from models.megaverse_object import Space, MegaverseObject


def test_parsing_space():
    space = MegaverseFactory.create_megaverse_object("SPACE", 0, 1)
    _assert_megaverse_object(space, Space, 0, 1)


def test_parsing_polyanets():
    polyanet = MegaverseFactory.create_megaverse_object("POLYANET", 0, 1)
    _assert_megaverse_object(polyanet, POLYanet, 0, 1)


def test_parsing_soloons():
    blue_soloon = MegaverseFactory.create_megaverse_object("BLUE_SOLOON", 0, 1)
    _assert_soloon(blue_soloon, row=0, column=1, color="blue")

    red_soloon = MegaverseFactory.create_megaverse_object("RED_SOLOON", 0, 1)
    _assert_soloon(red_soloon, row=0, column=1, color="red")

    purple_soloon = MegaverseFactory.create_megaverse_object("PURPLE_SOLOON", 0, 1)
    _assert_soloon(purple_soloon, row=0, column=1, color="purple")

    white_soloon = MegaverseFactory.create_megaverse_object("WHITE_SOLOON", 0, 1)
    _assert_soloon(white_soloon, row=0, column=1, color="white")


def test_parsing_comeths():
    up_cometh = MegaverseFactory.create_megaverse_object("UP_COMETH", 0, 1)
    _assert_cometh(up_cometh, 0, 1, "up")

    down_cometh = MegaverseFactory.create_megaverse_object("DOWN_COMETH", 0, 1)
    _assert_cometh(down_cometh, 0, 1, "down")

    left_cometh = MegaverseFactory.create_megaverse_object("LEFT_COMETH", 0, 1)
    _assert_cometh(left_cometh, 0, 1, "left")

    right_cometh = MegaverseFactory.create_megaverse_object("RIGHT_COMETH", 0, 1)
    _assert_cometh(right_cometh, 0, 1, "right")


def test_parsing_unsupported_object():
    try:
        MegaverseFactory.create_megaverse_object("RANDOM_OBJ", 0, 1)
        assert False, "This object is unsupported and the test should've failed!"
    except MegaverseObjectNotSupported as ex:
        assert ex.object_name == "RANDOM_OBJ"


def _assert_megaverse_object(megaverse_object: MegaverseObject, obj_class: Type[MegaverseObject], row: int, column: int):
    assert isinstance(megaverse_object, obj_class)
    assert megaverse_object.row == row
    assert megaverse_object.column == column


def _assert_soloon(soloon: MegaverseObject, row: int, column: int, color: str):
    _assert_megaverse_object(soloon, SOLoon, row, column)
    assert soloon.color == color


def _assert_cometh(cometh: MegaverseObject, row: int, column: int, direction: str):
    _assert_megaverse_object(cometh, ComETH, row, column)
    assert cometh.direction == direction
