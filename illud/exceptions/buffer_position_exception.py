"""Raised when a buffer position is out of range."""
from illud.exception import IlludException


class BufferPositionException(IlludException):
    """Raised when a buffer position is out of range."""
    def __init__(self, position: int, length: int):
        message: str
        if not length:
            message = 'The buffer is empty.'
        else:
            message = f'The position {position} is not in the range 0-{length-1}.'

        super().__init__(message)
