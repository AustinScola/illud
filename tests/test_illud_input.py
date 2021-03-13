"""Test illud.illud_input."""
from typing import Union

from illud.character import Character
from illud.illud_input import IlludInput
from illud.signal_ import Signal


def test_illud_input() -> None:
    """Test illud.illud_input.IlludInput"""
    assert isinstance(IlludInput, type(Union))
    assert IlludInput.__args__ == (Character, Signal)  # type: ignore[attr-defined]
