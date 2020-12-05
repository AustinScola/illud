"""Test illud.exceptions.break_exception."""
from illud.exception import IlludException
from illud.exceptions.break_exception import BreakException


def test_inheritance() -> None:
    """Test illud.exceptions.break_exception.BreakException inheritance."""
    assert issubclass(BreakException, IlludException)
