"""Test illud.exceptions.no_rows_exception."""
from illud.exception import IlludException
from illud.exceptions.no_rows_exception import NoRowsException


def test_inheritance() -> None:
    """Test illud.exceptions.no_rows_exception.NoRowsException inheritance."""
    assert issubclass(NoRowsException, IlludException)
