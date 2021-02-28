"""Test illud.excpetions.quit_exception."""
from illud.exception import IlludException
from illud.exceptions.quit_exception import QuitException


def test_inheritance() -> None:
    """Test illud.exceptions.quit_exception.QuitException inheritance."""
    assert issubclass(QuitException, IlludException)
