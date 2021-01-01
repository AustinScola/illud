"""Test illud.illud_state."""
from illud.illud_state import IlludState
from illud.state import State


def test_inheritance() -> None:
    """Test illud.illud_state.IlludState inheritance."""
    assert issubclass(IlludState, State)
