"""Test illud.window."""
import pytest

from illud.buffer import Buffer
from illud.integer_position_2d import IntegerPosition2D
from illud.window import Window


# yapf: disable
@pytest.mark.parametrize('position, width, height, buffer_', [
    (IntegerPosition2D(0, 0), 0, 0, Buffer()),
])
# yapf: enable
def test_init(position: IntegerPosition2D, width: int, height: int, buffer_: Buffer) -> None:
    """Test illud.window.Window.__init__"""
    window: Window = Window(position, width, height, buffer_)

    assert window.position == position
    assert window.width == width
    assert window.height == height
    assert window.buffer is buffer_
