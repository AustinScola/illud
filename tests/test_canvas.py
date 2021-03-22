"""Test illud.canvas."""
import itertools
from typing import Any, List, Optional
from unittest.mock import MagicMock

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.canvas import Canvas, Text
from illud.outputs.standard_output import StandardOutput
from illud.terminal_cursor import TerminalCursor


def test_text() -> None:
    """Test illud.canvas.Text."""
    assert issubclass(Text, List)
    assert Text.__args__ == (List[str], )  # type: ignore[attr-defined]


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('size, text, inversions, expected_size, expected_text, expected_inversions', [
    (None, None, None, IntegerSize2D(0, 0), [], []),
    (IntegerSize2D(0, 0), None, None, IntegerSize2D(0, 0), [], []),
    (IntegerSize2D(1, 1), None, None, IntegerSize2D(1, 1), [['']], []),
    (IntegerSize2D(3, 2), None, None, IntegerSize2D(3, 2), [['', '', ''], ['', '', '']], []),
    (IntegerSize2D(0, 0), [], None, IntegerSize2D(0, 0), [], []),
    (IntegerSize2D(1, 1), [['']], [], IntegerSize2D(1, 1), [['']], []),
    (IntegerSize2D(1, 1), [['']], [IntegerPosition2D()], IntegerSize2D(1, 1), [['']], [IntegerPosition2D()]),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_init(size: Optional[IntegerSize2D], text: Optional[Text],
              inversions: Optional[List[IntegerPosition2D]], expected_size: IntegerSize2D,
              expected_text: Text, expected_inversions: List[IntegerPosition2D]) -> None:
    """Test illud.canvas.Canvas.__init__."""
    canvas: Canvas = Canvas(size, text, inversions)

    assert canvas.size == expected_size
    assert canvas.text == expected_text
    assert canvas._inversions == expected_inversions  # pylint: disable=protected-access
    assert canvas._standard_output == StandardOutput()  # pylint: disable=protected-access
    assert canvas._terminal_cursor == TerminalCursor(StandardOutput())  # pylint: disable=protected-access


# yapf: disable
@pytest.mark.parametrize('canvas, other, expected_equality', [
    (Canvas(), '', False),
    (Canvas(IntegerSize2D(1, 1)), Canvas(), False),
    (Canvas(IntegerSize2D(1, 1), [['a']]), Canvas(IntegerSize2D(1, 1), [['b']]), False),
    (Canvas(), Canvas(), True),
    (Canvas(IntegerSize2D(1, 1), [['a']]), Canvas(IntegerSize2D(1, 1), [['a']]), True),
])
# yapf: enable
def test_eq(canvas: Canvas, other: Any, expected_equality: bool) -> None:
    """Test illud.canvas.Canvas.__eq__."""
    equality: bool = canvas == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('canvas, expected_representation', [
    (Canvas(), 'Canvas(size=IntegerSize2D(0, 0), text=[], inversions=[])'),
])
# yapf: enable
def test_repr(canvas: Canvas, expected_representation: str) -> None:
    """Test illud.canvas.Canvas.__repr__."""
    representation: str = repr(canvas)

    assert representation == expected_representation


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('canvas, size, expected_canvas_after', [
    (Canvas(), IntegerSize2D(0, 0), Canvas()),
    (Canvas(), IntegerSize2D(1, 1), Canvas(IntegerSize2D(1, 1), [[' ']])),
    (Canvas(), IntegerSize2D(3, 2), Canvas(IntegerSize2D(3, 2), [[' ', ' ', ' '], [' ', ' ', ' ']])),
    (Canvas(), IntegerSize2D(3, 2), Canvas(IntegerSize2D(3, 2), [[' ', ' ', ' '], [' ', ' ', ' ']])),
    (Canvas(IntegerSize2D(1, 1), [['a']]), IntegerSize2D(3, 2), Canvas(IntegerSize2D(3, 2), [['a', ' ', ' '], [' ', ' ', ' ']])),
    (Canvas(IntegerSize2D(3, 2), [['f', 'o', 'o'], ['b', 'a', 'r']]), IntegerSize2D(1, 1), Canvas(IntegerSize2D(1, 1), [['f']])),
])
# yapf: enable # pylint: enable=line-too-long
def test_resize(canvas: Canvas, size: IntegerSize2D, expected_canvas_after: Canvas) -> None:
    """Test illud.canvas.Canvas.resize."""
    canvas.resize(size)

    assert canvas == expected_canvas_after


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('canvas, index, expected_line', [
    (Canvas(IntegerSize2D(1, 1), [[' ']]), 0, [' ']),
    (Canvas(IntegerSize2D(3, 3), [['f', 'o', 'o'], ['b', 'a', 'r'], ['b', 'a', 'z']]), 1, ['b', 'a', 'r']),
])
# yapf: enable # pylint: enable=line-too-long
def test_getitem(canvas: Canvas, index: int, expected_line: List[str]) -> None:
    """Test illud.canvas.Canvas.__getitem__."""
    line: List[str] = canvas[index]

    assert line == expected_line


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('canvas, position, expected_canvas_after', [
    (Canvas(IntegerSize2D(1, 1)), IntegerPosition2D(), Canvas(IntegerSize2D(1, 1), inversions=[IntegerPosition2D()])),
    (Canvas(IntegerSize2D(1, 1), inversions=[IntegerPosition2D()]), IntegerPosition2D(), Canvas(IntegerSize2D(1, 1), inversions=[IntegerPosition2D()])),
])
# yapf: enable # pylint: enable=line-too-long
def test_invert(canvas: Canvas, position: IntegerPosition2D, expected_canvas_after: Canvas) -> None:
    """Test illud.canvas.Canvas.invert."""
    canvas.invert(position)

    assert canvas == expected_canvas_after


# yapf: disable
@pytest.mark.parametrize('canvas, expected_canvas_after', [
    (Canvas(), Canvas()),
    (Canvas(inversions=[IntegerPosition2D()]), Canvas()),
    (Canvas(inversions=[IntegerPosition2D(), IntegerPosition2D(1, 1)]), Canvas()),
])
# yapf: enable
def test_remove_inversions(canvas: Canvas, expected_canvas_after: Canvas) -> None:
    """Test illud.canvas.Canvas.remove_inversions."""
    canvas.remove_inversions()

    assert canvas == expected_canvas_after


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('canvas, expected_output', [
    (Canvas(), ''),
    (Canvas(IntegerSize2D(1, 1), [[' ']]), '\x1b[;H '),
    (Canvas(IntegerSize2D(1, 1), [['a']]), '\x1b[;Ha'),
    (Canvas(IntegerSize2D(2, 1), [[' '], [' ']]), '\x1b[;H \x1b[2;H '),
    (Canvas(IntegerSize2D(2, 2), [[' ', ' '], [' ', ' ']]), '\x1b[;H  \x1b[2;H  '),
    (Canvas(IntegerSize2D(1, 1), [[' ']], [IntegerPosition2D()]), '\x1b[;H \x1b[;H\x1b[7m \x1b[;2H\x1b[m'),
])
# yapf: enable # pylint: enable=line-too-long
def test_render(canvas: Canvas, expected_output: str) -> None:
    """Test illud.canvas.Canvas.render."""
    standard_output_mock = MagicMock(StandardOutput)
    canvas._standard_output = standard_output_mock  # pylint: disable=protected-access
    canvas._terminal_cursor._standard_output = standard_output_mock  # pylint: disable=protected-access

    canvas.render()

    calls_args = itertools.chain.from_iterable(
        call_args for call_args, _ in standard_output_mock.write.call_args_list)
    output: str = ''.join(calls_args)

    assert list(output) == list(expected_output)
