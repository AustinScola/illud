"""Test illud.mode."""
from typing import Any, Optional
from unittest.mock import patch

import pytest

from illud.character import Character
from illud.characters import CONTROL_C
from illud.command import Command
from illud.illud_state import IlludState
from illud.mode import Mode


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
@pytest.mark.parametrize('state_before, command, expected_state_after, expect_exits', [
    (IlludState(), Command(Character('i')), IlludState(), False),
    (IlludState(), Command(Character(CONTROL_C)), None, True),
])
# yapf: enable
def test_evaluate(state_before: IlludState, command: Command,
                  expected_state_after: Optional[IlludState], expect_exits: bool) -> None:
    """Test illud.mode.evaluate."""
    mode: Mode = Mode()

    if expect_exits:
        with patch('sys.exit') as exit_mock:
            mode.evaluate(state_before, command)

            exit_mock.assert_called_once_with()
    else:
        mode.evaluate(state_before, command)

        assert state_before == expected_state_after
