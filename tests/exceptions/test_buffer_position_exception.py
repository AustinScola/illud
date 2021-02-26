"""Test illud.exceptions.buffer_position_exception."""
import pytest

from illud.exception import IlludException
from illud.exceptions.buffer_position_exception import BufferPositionException


def test_inheritance() -> None:
    """Test illud.exceptions.buffer_position_exception.BufferPositionException inheritance."""
    assert issubclass(BufferPositionException, IlludException)


# yapf: disable
@pytest.mark.parametrize('position, length, expected_message', [
    (0, 0, 'The buffer is empty.'),
    (1, 0, 'The buffer is empty.'),
    (1, 1, 'The position 1 is not in the range 0-0.'),
    (2, 2, 'The position 2 is not in the range 0-1.'),
    (-1, 2, 'The position -1 is not in the range 0-1.'),
    (-1, 5, 'The position -1 is not in the range 0-4.'),
])
# yapf: enable
def test_init(position: int, length: int, expected_message: str) -> None:
    """Test illud.exceptions.buffer_position_exception.BufferPositionException.__init__."""
    buffer_position_exception: BufferPositionException = BufferPositionException(position, length)

    assert str(buffer_position_exception) == expected_message
