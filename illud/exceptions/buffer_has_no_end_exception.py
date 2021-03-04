"""Raised when a buffer buffer does not have an ending index because it is empty."""
from illud.exception import IlludException


class BufferHasNoEndException(IlludException):
    """Raised when a buffer buffer does not have an ending index because it is empty."""
    def __init__(self) -> None:
        message: str = 'The buffer does not have an ending index because it is empty.'
        super().__init__(message)
