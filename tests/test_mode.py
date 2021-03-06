"""Test illud.mode."""
from typing import Any, Optional
from unittest.mock import patch

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import CONTROL_C, CONTROL_D, CONTROL_F, CONTROL_J, CONTROL_K, CONTROL_W
from illud.exceptions.quit_exception import QuitException
from illud.file import File
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.status_bar import StatusBar
from illud.window import Window


def test_name() -> None:
    """Test illud.mode.Mode.name."""
    assert Mode.name == ''


# yapf: disable
@pytest.mark.parametrize('mode, other, expected_equality', [
    (Mode(), 'foo', False),
    (Mode(), 1, False),
    (Mode(), Mode(), True),
])
# yapf: enable
def test_eq(mode: Mode, other: Any, expected_equality: bool) -> None:
    """Test illud.mode.__eq__."""
    equality: bool = mode == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('mode, expected_representation', [
    (Mode(), 'Mode()'),
])
# yapf: enable
def test_repr(mode: Mode, expected_representation: str) -> None:
    """Test illud.mode.Mode.__repr__."""
    representation: str = repr(mode)

    assert representation == expected_representation


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state_before, character, expected_state_after, expect_writes, expect_exits', [
    (IlludState(), Character('i'), IlludState(), False, False),
    (IlludState(), Character(CONTROL_C), None, False, True),
    (IlludState(window=Window(size=IntegerSize2D(4, 3))), Character(CONTROL_D), IlludState(window=Window(size=IntegerSize2D(4, 3))), False, False),
    (IlludState(window=Window(size=IntegerSize2D(4, 3))), Character(CONTROL_F), IlludState(window=Window(size=IntegerSize2D(4, 3), offset=IntegerPosition2D(-1, 0))), False, False),
    (IlludState(window=Window(size=IntegerSize2D(4, 3))), Character(CONTROL_J), IlludState(window=Window(size=IntegerSize2D(4, 3), offset=IntegerPosition2D(0, -1))), False, False),
    (IlludState(window=Window(size=IntegerSize2D(4, 3))), Character(CONTROL_K), IlludState(window=Window(size=IntegerSize2D(4, 3))), False, False),
    (IlludState(), Character(CONTROL_W), IlludState(), False, False),
    (IlludState(file=File('foo')), Character(CONTROL_W), IlludState(file=File('foo')), True, False),
])
# yapf: enable # pylint: enable=line-too-long
def test_evaluate(state_before: IlludState, character: Character,
                  expected_state_after: Optional[IlludState], expect_writes: bool,
                  expect_exits: bool) -> None:
    """Test illud.mode.evaluate."""
    mode: Mode = Mode()

    if expect_exits:
        with pytest.raises(QuitException):
            mode.evaluate(state_before, character)
        return

    with patch('illud.file.File.write') as file_write_mock:
        mode.evaluate(state_before, character)

        if expect_writes:
            file_write_mock.assert_called_once_with(state_before.buffer)
        else:
            file_write_mock.assert_not_called()

    assert state_before == expected_state_after


class Foo(Mode):  # pylint: disable=too-few-public-methods
    """A mock mode."""
    name: str = 'Foo'


# yapf: disable
@pytest.mark.parametrize('state, mode, expected_state_after', [
    (IlludState(), Foo(), IlludState(mode=Foo(), status_bar=StatusBar(buffer_=Buffer('Foo')))),
])
# yapf: enable
def test_change_mode(state: IlludState, mode: Mode, expected_state_after: IlludState) -> None:
    """Test illud.mode.Mode._change_mode"""
    Mode._change_mode(state, mode)  # pylint: disable=protected-access

    assert state == expected_state_after
