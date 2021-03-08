"""Test illud.illud_state."""
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

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
@pytest.mark.parametrize('arguments, keyword_arguments, expected_buffer, expected_cursor, expected_mode, expected_window, expected_terminal_size', [
    ([], {}, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer()), IntegerSize2D(0, 0)),
    ([Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer()), IntegerSize2D(0, 0)], {}, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer()), IntegerSize2D(0, 0)),
    ([], {'buffer_': Buffer()}, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer()), IntegerSize2D(0, 0)),
    ([], {'cursor': Cursor(Buffer(), 0)}, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer()), IntegerSize2D(0, 0)),
    ([], {'mode': Normal()}, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer()), IntegerSize2D(0, 0)),
    ([], {'window': Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer())}, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer()), IntegerSize2D(0, 0)),
    ([], {'terminal_size': IntegerSize2D(0, 0)}, Buffer(), Cursor(Buffer(), 0), Normal(), Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer()), IntegerSize2D(0, 0)),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any], expected_buffer: Buffer,
              expected_cursor: Cursor, expected_mode: Mode, expected_window: Window,
              expected_terminal_size: IntegerSize2D) -> None:
    """Test illud.illud_state.IlludState.__init__."""
    illud_state: IlludState = IlludState(*arguments, **keyword_arguments)

    assert illud_state.buffer == expected_buffer
    assert illud_state.cursor == expected_cursor
    assert illud_state.mode == expected_mode
    assert illud_state.window == expected_window
    assert illud_state.terminal_size == expected_terminal_size


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('file, file_contents, terminal_size, expected_illud_state', [
    ('foo.txt', '', IntegerSize2D(0, 0), IlludState()),
    ('foo.txt', 'Lorem ipsum dolor sit amet', IntegerSize2D(120, 80), IlludState(Buffer('Lorem ipsum dolor sit amet'), terminal_size=IntegerSize2D(120, 80))),
])
# yapf: enable # pylint: enable=line-too-long
def test_from_file(file: str, file_contents: str, terminal_size: IntegerSize2D,
                   expected_illud_state: IlludState) -> None:
    """Test illud.illud_state.IlludState.from_file."""
    with patch('illud.illud.Terminal.get_size', return_value=terminal_size), \
        patch('builtins.open', mock_open(read_data=file_contents)):

        illud_state: IlludState = IlludState.from_file(file)

    assert illud_state == expected_illud_state


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('illud_state, other, expected_equality', [
    (IlludState(), 'foo', False),
    (IlludState(), IlludState(), True),
    (IlludState(Buffer('foo')), IlludState(), False),
    (IlludState(Buffer('foo')), IlludState(Buffer('bar')), False),
    (IlludState(Buffer('foo')), IlludState(Buffer('foo')), True),
    (IlludState(cursor=Cursor(Buffer(), 1)), IlludState(), False),
    (IlludState(cursor=Cursor(Buffer(), 1)), IlludState(cursor=Cursor(Buffer(), 1)), True),
    (IlludState(mode=Normal()), IlludState(mode=Insert()), False),
    (IlludState(mode=Normal()), IlludState(mode=Normal()), True),
    (IlludState(terminal_size=IntegerSize2D(3, 4)), IlludState(), False),
    (IlludState(terminal_size=IntegerSize2D(3, 4)), IlludState(terminal_size=IntegerSize2D(3, 4)), True),
    (IlludState(Buffer('foo'), mode=Normal()), IlludState(Buffer('bar'), mode=Normal()), False),
    (IlludState(Buffer('foo'), mode=Normal()), IlludState(Buffer('foo'), mode=Normal()), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(illud_state: IlludState, other: Any, expected_equality: bool) -> None:
    """Test illud.illud_state.IlludState.__eq__."""
    equality: bool = illud_state == other

    assert equality == expected_equality
