import pytest

from src.converterkawtar import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32

def test_fahrenheit_to_celsius_at_freezing_point():
    assert fahrenheit_to_celsius(32) == 0

def test_celsius_to_fahrenheit_rejects_text():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("ww")