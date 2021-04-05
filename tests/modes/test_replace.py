"""Test illud.modes.replace."""
from typing import Optional

import pytest

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import CARRIAGE_RETURN, CONTROL_C, ESCAPE
from illud.cursor import Cursor
from illud.exceptions.quit_exception import QuitException
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.normal import Normal
from illud.modes.replace import Replace
from illud.status_bar import StatusBar


def test_inheritance() -> None:
    """Test illud.modes.replace.Replace inheritance."""
    assert issubclass(Replace, Mode)


def test_name() -> None:
    """Test illud.modes.replace.Replace.name."""
    assert Replace.name == 'Replace'


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state, character, expected_state_after, expect_exits', [
    (IlludState(mode=Replace()), Character(CONTROL_C), None, True),
    (IlludState(mode=Replace()), Character(ESCAPE), IlludState(mode=Normal(), status_bar=StatusBar(buffer_=Buffer('Normal'))), False),
    (IlludState(mode=Replace(), cursor=Cursor(Buffer('bat'))), Character('c'), IlludState(mode=Normal(), cursor=Cursor(Buffer('cat')), status_bar=StatusBar(buffer_=Buffer('Normal'))), False),
    (IlludState(mode=Replace(), cursor=Cursor(Buffer('bat'), 1)), Character('o'), IlludState(mode=Normal(), cursor=Cursor(Buffer('bot'), 1), status_bar=StatusBar(buffer_=Buffer('Normal'))), False),
    (IlludState(mode=Replace(), cursor=Cursor(Buffer('bat'), 2)), Character('r'), IlludState(mode=Normal(), cursor=Cursor(Buffer('bar'), 2), status_bar=StatusBar(buffer_=Buffer('Normal'))), False),
    (IlludState(mode=Replace(), cursor=Cursor(Buffer('batsman'), 3)), Character(CARRIAGE_RETURN), IlludState(mode=Normal(), cursor=Cursor(Buffer('bat\nman'), 3), status_bar=StatusBar(buffer_=Buffer('Normal'))), False),
])
# yapf: enable # pylint: enable=line-too-long
def test_evaluate(state: IlludState, character: Character,
                  expected_state_after: Optional[IlludState], expect_exits: bool) -> None:
    """Test illud.modes.replace.Replace.evaluate."""
    if expect_exits:
        with pytest.raises(QuitException):
            Replace.evaluate(state, character)
    else:
        Replace.evaluate(state, character)

        assert state == expected_state_after
