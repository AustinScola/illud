"""Test illud.modes.normal."""
from typing import Optional
from unittest.mock import patch

import pytest

from illud.character import Character
from illud.characters import CONTROL_C
from illud.command import Command
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.normal import Normal


def test_inheritance() -> None:
    """Test illud.modes.normal.Normal inheritance."""
    assert issubclass(Normal, Mode)


# yapf: disable
@pytest.mark.parametrize('state_before, command, expected_state_after, expect_exits', [
    (IlludState(), Command(Character('i')), IlludState(mode=Insert()), False),
    (IlludState(), Command(Character(CONTROL_C)), None, True),
])
# yapf: enable
def test_evaluate(state_before: IlludState, command: Command,
                  expected_state_after: Optional[IlludState], expect_exits: bool) -> None:
    """Test illud.modes.normal.Normal.evaluate."""
    normal: Normal = Normal()

    if expect_exits:
        with patch('sys.exit') as exit_mock:
            normal.evaluate(state_before, command)

            exit_mock.assert_called_once_with()
    else:
        normal.evaluate(state_before, command)

        assert state_before == expected_state_after
