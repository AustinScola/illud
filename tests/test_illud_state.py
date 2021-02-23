"""Test illud.illud_state."""
from typing import Any, Dict, Optional

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.cursor import Cursor
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.normal import Normal
from illud.state import State
from illud.window import Window


def test_inheritance() -> None:
    """Test illud.illud_state.IlludState inheritance."""
    assert issubclass(IlludState, State)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('buffer_, cursor_position, mode, terminal_size, pass_buffer, pass_cursor_position, pass_mode, pass_terminal_size, expected_buffer, expected_cursor, expected_mode, expected_window', [
    (None, None, None, None, False, False, False, False, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer())),
    (None, None, Normal(), None, False, False, True, False, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer())),
    (Buffer(), None, None, None, True, False, False, False, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer())),
    (Buffer(), None, Normal(), None, True, False, True, False, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer())),
    (None, None, None, None, True, False, False, False, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer())),
    (None, None, Normal(), None, True, False, True, False, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer())),
    (Buffer('foo'), None, None, None, True, False, False, False, Buffer('foo'), Cursor(Buffer('foo'), 0), Normal(), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer('foo'))),
    (Buffer('foo'), None, Normal(), None, True, False, True, False, Buffer('foo'), Cursor(Buffer('foo'), 0), Normal(), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer('foo'))),
    (Buffer('foo'), 1, Normal(), None, True, True, True, False, Buffer('foo'), Cursor(Buffer('foo'), 1), Normal(), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer('foo'))),
    (Buffer('foo'), 1, Normal(), IntegerSize2D(80, 24), True, True, True, True, Buffer('foo'), Cursor(Buffer('foo'), 1), Normal(), Window(IntegerPosition2D(0, 0), IntegerSize2D(80, 24), Buffer('foo'))),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_init(buffer_: Optional[Buffer], cursor_position: Optional[int], mode: Optional[Mode],
              terminal_size: Optional[IntegerSize2D], pass_buffer: bool, pass_cursor_position: bool,
              pass_mode: bool, pass_terminal_size: bool, expected_buffer: Buffer,
              expected_cursor: Cursor, expected_mode: Mode, expected_window: Window) -> None:
    """Test illud.illud_state.IlludState.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_buffer:
        keyword_arguments['buffer_'] = buffer_
    if pass_cursor_position:
        keyword_arguments['cursor_position'] = cursor_position
    if pass_mode:
        keyword_arguments['mode'] = mode
    if pass_terminal_size:
        keyword_arguments['terminal_size'] = terminal_size

    illud_state: IlludState = IlludState(**keyword_arguments)

    assert illud_state.buffer == expected_buffer
    assert illud_state.cursor == expected_cursor
    assert illud_state.cursor.buffer is illud_state.buffer
    assert illud_state.mode == expected_mode
    assert illud_state.window == expected_window
    assert illud_state.window.buffer is illud_state.buffer


# yapf: disable
@pytest.mark.parametrize('illud_state, other, expected_equality', [
    (IlludState(), 'foo', False),
    (IlludState(), IlludState(), True),
    (IlludState(Buffer('foo')), IlludState(), False),
    (IlludState(Buffer('foo')), IlludState(Buffer('bar')), False),
    (IlludState(Buffer('foo')), IlludState(Buffer('foo')), True),
    (IlludState(mode=Normal()), IlludState(mode=Insert()), False),
    (IlludState(mode=Normal()), IlludState(mode=Normal()), True),
    (IlludState(Buffer('foo'), mode=Normal()), IlludState(Buffer('bar'), mode=Normal()), False),
    (IlludState(Buffer('foo'), mode=Normal()), IlludState(Buffer('foo'), mode=Normal()), True),
])
# yapf: enable
def test_eq(illud_state: IlludState, other: Any, expected_equality: bool) -> None:
    """Test illud.illud_state.IlludState.__eq__."""
    equality: bool = illud_state == other

    assert equality == expected_equality
