"""Test illud.modes.delete."""
from typing import Optional

import pytest

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import CONTROL_C, ESCAPE
from illud.cursor import Cursor
from illud.exceptions.quit_exception import QuitException
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.delete import Delete
from illud.modes.normal import Normal
from illud.status_bar import StatusBar


def test_name() -> None:
    """Test illud.modes.delete.Delete.name."""
    assert Delete.name == 'Delete'


def test_inheritance() -> None:
    """Test illud.modes.delete.Delete inheritance."""
    assert issubclass(Delete, Mode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state, character, expected_state_after, expect_exits', [
    (IlludState(mode=Delete()), Character(CONTROL_C), None, True),
    (IlludState(mode=Delete()), Character(ESCAPE), IlludState(mode=Normal(), status_bar=StatusBar(buffer_=Buffer('Normal'))), False),
    (IlludState(mode=Delete(), cursor=Cursor(Buffer('foo\nbar\nbaz'), 5)), Character('l'), IlludState(mode=Normal(), status_bar=StatusBar(buffer_=Buffer('Normal')), cursor=Cursor(Buffer('foo\nbaz'), 5), clipboard=Buffer('bar\n')), False),
])
# yapf: enable # pylint: enable=line-too-long
def test_evaluate(state: IlludState, character: Character,
                  expected_state_after: Optional[IlludState], expect_exits: bool) -> None:
    """Test illud.modes.delete.Delete.evaluate."""
    if expect_exits:
        with pytest.raises(QuitException):
            Delete.evaluate(state, character)
    else:
        Delete.evaluate(state, character)

        assert state == expected_state_after
