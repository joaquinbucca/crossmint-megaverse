from models.astral_objetcs import ComETH, SOLoon, POLYanet
from models.megaverse_object import Space


def test_initializing_each_object_does_not_fail():
    assert Space(0, 1).is_astral_object() is False
    astral_objects = [
        ComETH(0, 1),
        POLYanet(0, 1),
        SOLoon(0, 1)
    ]
    for astral_object in astral_objects:
        assert astral_object.is_astral_object() is True


def test_to_body_generates_coordinates():
    body = POLYanet(0, 1).to_body()

    assert body == {"row": 0, "column": 1}


def test_to_body_includes_direction_in_comeths():
    body = ComETH(0, 1, direction="down").to_body()

    assert body == {"row": 0, "column": 1, "direction": "down"}


def test_to_body_includes_color_in_soloons():
    body = SOLoon(0, 1, color="white").to_body()

    assert body == {"row": 0, "column": 1, "color": "white"}
