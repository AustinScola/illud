"""Test illud.window."""
import pytest

from illud.buffer import Buffer
from illud.window import Window


# yapf: disable
@pytest.mark.parametrize('x, y, width, height, buffer_', [
    (0, 0, 0, 0, Buffer('')),
])
# yapf: enable
# pylint: disable=invalid-name
def test_init(x: int, y: int, width: int, height: int, buffer_: Buffer) -> None:
    """Test illud.window.Window.__init__"""
    window: Window = Window(x, y, width, height, buffer_)

    assert window.x == x
    assert window.y == y
    assert window.width == width
    assert window.height == height
    assert window.buffer is buffer_
