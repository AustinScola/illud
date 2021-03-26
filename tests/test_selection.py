"""Test illud.selection."""
from typing import Any, Dict, List

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.cursor import Cursor
from illud.selection import Selection


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, keyword_arguments, expected_buffer, expected_start, expected_end', [
    ([], {}, Buffer(), 0, 0),
    ([], {'buffer_': Buffer('foo'), 'start': 1, 'end': 3}, Buffer('foo'), 1, 3),
    ([Buffer('foo')], {}, Buffer('foo'), 0, 0),
    ([Buffer('foo')], {'start': 1}, Buffer('foo'), 1, 1),
    ([Buffer('foo')], {'start': 1, 'end': 3}, Buffer('foo'), 1, 3),
    ([Buffer('foo'), 1], {}, Buffer('foo'), 1, 1),
    ([Buffer('foo'), 1], {'end': 3}, Buffer('foo'), 1, 3),
    ([Buffer('foo'), 1, 3], {}, Buffer('foo'), 1, 3),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any], expected_buffer: Buffer,
              expected_start: int, expected_end: int) -> None:
    """Test illud.selection.Selection.__init__."""
    selection: Selection = Selection(*arguments, **keyword_arguments)

    assert selection.buffer == expected_buffer
    assert selection.start == expected_start
    assert selection.end == expected_end


# yapf: disable
@pytest.mark.parametrize('cursor, expected_selection', [
    (Cursor(), Selection()),
    (Cursor(Buffer('foo')), Selection(Buffer('foo'))),
    (Cursor(Buffer('foo'), 1), Selection(Buffer('foo'), 1)),
    (Cursor(Buffer('foo'), 3), Selection(Buffer('foo'), 3)),
])
# yapf: enable
def test_from_cursor(cursor: Cursor, expected_selection: Selection) -> None:
    """Test illud.selection.Selection.from_cursor."""
    selection: Selection = Selection.from_cursor(cursor)

    assert selection == expected_selection


# yapf: disable
@pytest.mark.parametrize('selection, other, expected_equality', [
    (Selection(), 'foo', False),
    (Selection(Buffer('foo')), Selection(), False),
    (Selection(start=1), Selection(), False),
    (Selection(start=1, end=3), Selection(start=1), False),
    (Selection(), Selection(), True),
    (Selection(Buffer('foo'), 1, 3), Selection(Buffer('foo'), 1, 3), True),
])
# yapf: enable
def test_eq(selection: Selection, other: Any, expected_equality: bool) -> None:
    """Test illud.selection.Selection.__eq__."""
    equality: bool = selection == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('selection, expected_representation', [
    (Selection(), 'Selection(buffer_=Buffer(), end=0)'),
])
# yapf: enable
def test_repr(selection: Selection, expected_representation: str) -> None:
    """Test illud.selection.Selection.__repr__."""
    representation: str = repr(selection)

    assert representation == expected_representation


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('selection, canvas, offset, expected_canvas_after', [
    (Selection(), Canvas(), IntegerPosition2D(), Canvas()),
    (Selection(), Canvas(IntegerSize2D(1, 1)), IntegerPosition2D(0, 1), Canvas(IntegerSize2D(1, 1))),
    (Selection(Buffer('foo'), 3), Canvas(), IntegerPosition2D(), Canvas()),
    (Selection(), Canvas(IntegerSize2D(1, 1)), IntegerPosition2D(), Canvas(IntegerSize2D(1, 1), inversions=[IntegerPosition2D()])),
    (Selection(Buffer('foo'), 1, 2), Canvas(IntegerSize2D(3, 1)), IntegerPosition2D(), Canvas(IntegerSize2D(3, 1), inversions=[IntegerPosition2D(1, 0), IntegerPosition2D(2, 0)])),
    (Selection(Buffer('foo'), 1), Canvas(IntegerSize2D(2, 1)), IntegerPosition2D(1, 0), Canvas(IntegerSize2D(2, 1), inversions=[IntegerPosition2D()])),
    (Selection(Buffer('foo'), 1), Canvas(IntegerSize2D(3, 1)), IntegerPosition2D(0, 1), Canvas(IntegerSize2D(3, 1), inversions=[])),
    (Selection(Buffer('foo\nbar'), 4), Canvas(IntegerSize2D(2, 1)), IntegerPosition2D(0, 1), Canvas(IntegerSize2D(2, 1), inversions=[IntegerPosition2D()])),
])
# yapf: enable # pylint: enable=line-too-long
def test_draw(selection: Selection, canvas: Canvas, offset: IntegerPosition2D,
              expected_canvas_after: Canvas) -> None:
    """Test illud.selection.Selection.draw."""
    selection.draw(canvas, offset)

    assert canvas == expected_canvas_after
