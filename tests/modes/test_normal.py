"""Test illud.modes.normal."""
from typing import Optional

import pytest

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import CONTROL_C
from illud.command import Command
from illud.exceptions.quit_exception import QuitException
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.normal import Normal


def test_inheritance() -> None:
    """Test illud.modes.normal.Normal inheritance."""
    assert issubclass(Normal, Mode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state_before, command, expected_state_after, expect_exits', [
    (IlludState(), Command(Character('i')), IlludState(mode=Insert()), False),
    (IlludState(), Command(Character('j')), IlludState(), False),
    (IlludState(Buffer('foo')), Command(Character('j')), IlludState(Buffer('foo')), False),
    (IlludState(Buffer('foo\nbar')), Command(Character('j')), IlludState(Buffer('foo\nbar'), cursor_position=4), False),
    (IlludState(), Command(Character('k')), IlludState(), False),
    (IlludState(), Command(Character('f')), IlludState(), False),
    (IlludState(), Command(Character('d')), IlludState(), False),
    (IlludState(), Command(Character(CONTROL_C)), None, True),
])
# yapf: enable # pylint: enable=line-too-long
def test_evaluate(state_before: IlludState, command: Command,
                  expected_state_after: Optional[IlludState], expect_exits: bool) -> None:
    """Test illud.modes.normal.Normal.evaluate."""
    normal: Normal = Normal()

    if expect_exits:
        with pytest.raises(QuitException):
            normal.evaluate(state_before, command)
    else:
        normal.evaluate(state_before, command)

        assert state_before == expected_state_after
