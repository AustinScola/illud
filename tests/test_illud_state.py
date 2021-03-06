"""Test illud.illud_state."""
from typing import Any, Dict, List, Optional
from unittest.mock import mock_open, patch

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.cursor import Cursor
from illud.file import File
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.normal import Normal
from illud.selection import Selection
from illud.state import State
from illud.status_bar import StatusBar
from illud.window import Window


def test_inheritance() -> None:
    """Test illud.illud_state.IlludState inheritance."""
    assert issubclass(IlludState, State)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, keyword_arguments, expected_terminal_size, expected_buffer, expected_cursor, expected_selection, expected_clipboard, expected_mode, expected_window, expected_status_bar, expected_canvas, expected_file', [
    ([], {}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas(), None),
    ([IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas()], {}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas(), None),
    ([], {'terminal_size': IntegerSize2D(0, 0)}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas(), None),
    ([], {'buffer_': Buffer()}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas(), None),
    ([], {'cursor': Cursor()}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas(), None),
    ([], {'selection': Selection()}, IntegerSize2D(0, 0), Buffer(), Cursor(), Selection(), None, Normal(), Window(), StatusBar(), Canvas(), None),
    ([], {'clipboard': Buffer()}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, Buffer(), Normal(), Window(), StatusBar(), Canvas(), None),
    ([], {'mode': Normal()}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas(), None),
    ([], {'window': Window()}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas(), None),
    ([], {'status_bar': StatusBar()}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas(), None),
    ([], {'canvas': Canvas()}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas(), None),
    ([], {'file': File('foo')}, IntegerSize2D(0, 0), Buffer(), Cursor(), None, None, Normal(), Window(), StatusBar(), Canvas(), File('foo')),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
              expected_terminal_size: IntegerSize2D, expected_buffer: Buffer,
              expected_cursor: Cursor, expected_selection: Selection,
              expected_clipboard: Optional[Buffer], expected_mode: Mode, expected_window: Window,
              expected_status_bar: StatusBar, expected_canvas: Canvas,
              expected_file: Optional[File]) -> None:
    """Test illud.illud_state.IlludState.__init__."""
    illud_state: IlludState = IlludState(*arguments, **keyword_arguments)

    assert illud_state.terminal_size == expected_terminal_size
    assert illud_state.buffer == expected_buffer
    assert illud_state.cursor == expected_cursor
    assert illud_state.selection == expected_selection
    assert illud_state.clipboard == expected_clipboard
    assert illud_state.mode == expected_mode
    assert illud_state.window == expected_window
    assert illud_state.status_bar == expected_status_bar
    assert illud_state.canvas == expected_canvas
    assert illud_state.file == expected_file


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('path, file_contents, file_exists, terminal_size, expected_illud_state', [
    ('foo.txt', None, False, IntegerSize2D(0, 0), IlludState(file=File('foo.txt'), status_bar=StatusBar(buffer_=Buffer('Normal')))),
    ('foo.txt', '', True, IntegerSize2D(0, 0), IlludState(file=File('foo.txt'), status_bar=StatusBar(buffer_=Buffer('Normal')))),
    ('foo.txt', 'Lorem ipsum dolor sit amet', True, IntegerSize2D(120, 80), IlludState(terminal_size=IntegerSize2D(120, 80), buffer_=Buffer('Lorem ipsum dolor sit amet'), cursor=Cursor(Buffer('Lorem ipsum dolor sit amet')), window=Window(size=IntegerSize2D(120, 79), buffer_=Buffer('Lorem ipsum dolor sit amet')), status_bar=StatusBar(position=IntegerPosition2D(0, 79), size=IntegerSize2D(120, 1), buffer_=Buffer('Normal')), canvas=Canvas(IntegerSize2D(120, 80)).fill(' '), file=File('foo.txt'))),
])
# yapf: enable # pylint: enable=line-too-long
def test_from_file(path: str, file_contents: Optional[str], file_exists: bool,
                   terminal_size: IntegerSize2D, expected_illud_state: IlludState) -> None:
    """Test illud.illud_state.IlludState.from_file."""
    illud_state: IlludState
    with patch('illud.illud.Terminal.get_size', return_value=terminal_size):
        if file_exists:
            with patch('builtins.open', mock_open(read_data=file_contents)):
                illud_state = IlludState.from_file(path)
        else:
            with patch('builtins.open', side_effect=FileNotFoundError()):
                illud_state = IlludState.from_file(path)

    assert illud_state == expected_illud_state
    assert illud_state.cursor.buffer is illud_state.buffer
    assert illud_state.window.buffer is illud_state.buffer


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('illud_state, other, expected_equality', [
    (IlludState(), 'foo', False),
    (IlludState(), IlludState(), True),
    (IlludState(buffer_=Buffer('foo')), IlludState(), False),
    (IlludState(buffer_=Buffer('foo')), IlludState(buffer_=Buffer('bar')), False),
    (IlludState(buffer_=Buffer('foo')), IlludState(buffer_=Buffer('foo')), True),
    (IlludState(cursor=Cursor(Buffer(), 1)), IlludState(), False),
    (IlludState(cursor=Cursor(Buffer(), 1)), IlludState(cursor=Cursor(Buffer(), 1)), True),
    (IlludState(mode=Normal()), IlludState(mode=Insert()), False),
    (IlludState(mode=Normal()), IlludState(mode=Normal()), True),
    (IlludState(terminal_size=IntegerSize2D(3, 4)), IlludState(), False),
    (IlludState(terminal_size=IntegerSize2D(3, 4)), IlludState(terminal_size=IntegerSize2D(3, 4)), True),
    (IlludState(buffer_=Buffer('foo'), mode=Normal()), IlludState(buffer_=Buffer('bar'), mode=Normal()), False),
    (IlludState(buffer_=Buffer('foo'), mode=Normal()), IlludState(buffer_=Buffer('foo'), mode=Normal()), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(illud_state: IlludState, other: Any, expected_equality: bool) -> None:
    """Test illud.illud_state.IlludState.__eq__."""
    equality: bool = illud_state == other

    assert equality == expected_equality


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('illud_state, expected_representation', [
    (IlludState(), 'IlludState(terminal_size=IntegerSize2D(0, 0), buffer_=Buffer(), cursor=Cursor(buffer_=Buffer()), mode=Normal(), window=Window(position=IntegerPosition2D(), size=IntegerSize2D(0, 0), buffer_=Buffer(), offset=IntegerPosition2D()), status_bar=StatusBar(position=IntegerPosition2D(), size=IntegerSize2D(0, 0), buffer_=Buffer(), offset=IntegerPosition2D()), canvas=Canvas(size=IntegerSize2D(0, 0), text=[], inversions=[]))'),
])
# yapf: enable # pylint: enable=line-too-long
def test_repr(illud_state: IlludState, expected_representation: str) -> None:
    """Test illud.illud_state.IlludState.__repr__."""
    representation: str = repr(illud_state)

    assert representation == expected_representation
