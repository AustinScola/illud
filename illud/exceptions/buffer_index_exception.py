"""Raised when an index to a buffer is out of range."""
from illud.exception import IlludException


class BufferIndexException(IlludException):
    """Raised when an index to a buffer is out of range."""
    def __init__(self, index: int, length: int):
        message: str
        if not length:
            message = 'The buffer is empty.'
        else:
            message = f'The index {index} is not in the range 0-{length-1}.'

        super().__init__(message)
