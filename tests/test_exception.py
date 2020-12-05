"""Test illud.exception."""
from illud.exception import IlludException


def test_inheritance() -> None:
    """Test illud.exception.IlludException inheritance."""
    assert issubclass(IlludException, Exception)
