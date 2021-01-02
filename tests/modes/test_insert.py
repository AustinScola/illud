"""Test illud.modes.insert."""
from illud.mode import Mode
from illud.modes.insert import Insert


def test_inheritance() -> None:
    """Test illud.modes.insert.Insert inheritance."""
    assert issubclass(Insert, Mode)
