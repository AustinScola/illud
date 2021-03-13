"""Test illud.exceptions.no_signals_exception."""
from illud.exception import IlludException
from illud.exceptions.no_signals_exception import NoSignalsException


def test_inheritance() -> None:
    """Test illud.exceptions.no_signals_exception.NoSignalsException inheritance."""
    assert issubclass(NoSignalsException, IlludException)
    assert issubclass(NoSignalsException, StopIteration)
