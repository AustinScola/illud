"""Test illud.modes.normal."""
from illud.mode import Mode
from illud.modes.normal import Normal


def test_inheritance() -> None:
    """Test illud.modes.normal.Normal inheritance."""
    assert issubclass(Normal, Mode)
