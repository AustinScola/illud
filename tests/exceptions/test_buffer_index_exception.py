"""Test illud.exceptions.buffer_index_exception."""
import pytest

from illud.exception import IlludException
from illud.exceptions.buffer_index_exception import BufferIndexException


def test_inheritance() -> None:
    """Test illud.exceptions.buffer_index_exception.BufferIndexException inheritance."""
    assert issubclass(BufferIndexException, IlludException)


# yapf: disable
@pytest.mark.parametrize('index, length, expected_message', [
    (0, 0, 'The buffer is empty.'),
    (1, 0, 'The buffer is empty.'),
    (1, 1, 'The index 1 is not in the range 0-0.'),
    (2, 2, 'The index 2 is not in the range 0-1.'),
    (-1, 2, 'The index -1 is not in the range 0-1.'),
    (-1, 5, 'The index -1 is not in the range 0-4.'),
])
# yapf: enable
def test_init(index: int, length: int, expected_message: str) -> None:
    """Test illud.exceptions.buffer_index_exception.BufferIndexException.__init__."""
    buffer_index_exception: BufferIndexException = BufferIndexException(index, length)

    assert str(buffer_index_exception) == expected_message
