"""Test illud.illud_state."""
from typing import Any

import pytest

from illud.illud_state import IlludState
from illud.state import State


def test_inheritance() -> None:
    """Test illud.illud_state.IlludState inheritance."""
    assert issubclass(IlludState, State)


# yapf: disable
@pytest.mark.parametrize('illud_state, other, expected_equality', [
    (IlludState(), 'foo', False),
    (IlludState(), IlludState(), True),
])
# yapf: enable
def test_eq(illud_state: IlludState, other: Any, expected_equality: bool) -> None:
    """Test illud.illud_state.IlludState.__eq__."""
    equality: bool = illud_state == other

    assert equality == expected_equality
