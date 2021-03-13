"""Raised when there are no signals."""
from illud.exception import IlludException


class NoSignalsException(IlludException, StopIteration):
    """Raised when there are no signals."""
