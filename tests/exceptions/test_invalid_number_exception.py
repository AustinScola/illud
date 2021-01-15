"""Test illud.exceptions.invalid_number_exception."""
from illud.exception import IlludException
from illud.exceptions.invalid_number_exception import InvalidNumberException


def test_inheritance() -> None:
    """Test illud.exceptions.invalid_number_exception.InvalidNumberException inheritance."""
    assert issubclass(InvalidNumberException, IlludException)
