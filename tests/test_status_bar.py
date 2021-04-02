"""Test illud.status_bar."""
import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.status_bar import StatusBar
from illud.window import Window


def test_inheritance() -> None:
    """Test illud.status_bar.StatusBar inheritance."""
    assert issubclass(StatusBar, Window)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('status_bar, canvas, expected_canvas_after', [
    (StatusBar(size=IntegerSize2D(3, 1), buffer_=Buffer('foo')), Canvas(IntegerSize2D(3, 1)).fill('x'), Canvas(IntegerSize2D(3, 1), [['f', 'o', 'o']], inversions=[IntegerPosition2D(x, 0) for x in range(3)])),
])
# yapf: enable # pylint: enable=line-too-long
def test_draw(status_bar: StatusBar, canvas: Canvas, expected_canvas_after: Canvas) -> None:
    """Test illud.status_bar.StatusBar.draw."""
    status_bar.draw(canvas)

    assert canvas == expected_canvas_after
