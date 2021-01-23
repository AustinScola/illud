"""Test illud.exceptions.no_columns_exception."""
from illud.exception import IlludException
from illud.exceptions.no_columns_exception import NoColumnsException


def test_inheritance() -> None:
    """Test illud.exceptions.no_columns_exception.NoColumnsException inheritance."""
    assert issubclass(NoColumnsException, IlludException)
