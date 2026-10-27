
import pytest
from src.converterhibateallah import convert_length


def test_kilometers_to_miles():
    assert convert_length(1, "km", "miles") == pytest.approx(0.621371)


def test_miles_to_kilometers():
    assert convert_length(1, "miles", "km") == pytest.approx(1.609344)


def test_centimeters_to_meters():
    assert convert_length(100, "cm", "m") == 1


def test_zero_length():
    assert convert_length(0, "km", "miles") == 0


def test_invalid_unit():
    with pytest.raises(ValueError):
        convert_length(5, "yards", "miles")


def test_negative_value():
    with pytest.raises(ValueError):
        convert_length(-5, "km", "miles")
