"""Test illud.cursor."""
import pytest

from illud.buffer import Buffer
from illud.cursor import Cursor


# yapf: disable
@pytest.mark.parametrize('buffer_,  position', [
    (Buffer(), 0),
    (Buffer('foo'), 1),
])
# yapf: enable
def test_init(buffer_: Buffer, position: int) -> None:
    """Test illud.cursor.Cursor.__init__."""
    cursor: Cursor = Cursor(buffer_, position)

    assert cursor.position == position
    assert cursor.buffer is buffer_
