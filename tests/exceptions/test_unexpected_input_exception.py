"""Test illud.exceptions.unexpected_input_exception."""
from illud.exception import IlludException
from illud.exceptions.unexpected_input_exception import UnexpectedInputException


def test_inheritance() -> None:
    """Test illud.exceptions.unexpected_input_exception.UnexpectedInputException inheritance."""
    assert issubclass(UnexpectedInputException, IlludException)
