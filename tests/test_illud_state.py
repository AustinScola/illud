"""Test illud.illud_state."""
from typing import Any, Dict, Optional

import pytest

from illud.buffer import Buffer
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.normal import Normal
from illud.state import State


def test_inheritance() -> None:
    """Test illud.illud_state.IlludState inheritance."""
    assert issubclass(IlludState, State)


# yapf: disable
@pytest.mark.parametrize('buffer_, mode, pass_buffer, pass_mode, expected_buffer, expected_mode', [
    (None, None, False, False, Buffer(''), Normal()),
    (None, Normal(), False, True, Buffer(''), Normal()),
    (Buffer(''), None, True, False, Buffer(''), Normal()),
    (Buffer(''), Normal(), True, True, Buffer(''), Normal()),
    (None, None, True, False, Buffer(''), Normal()),
    (None, Normal(), True, True, Buffer(''), Normal()),
    (Buffer('foo'), None, True, False, Buffer('foo'), Normal()),
    (Buffer('foo'), Normal(), True, True, Buffer('foo'), Normal()),
])
# yapf: enable
# pylint: disable=too-many-arguments
def test_init(buffer_: Optional[Buffer], mode: Optional[Mode], pass_buffer: bool, pass_mode: bool,
              expected_buffer: Buffer, expected_mode: Mode) -> None:
    """Test illud.illud_state.IlludState.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_buffer:
        keyword_arguments['buffer_'] = buffer_
    if pass_mode:
        keyword_arguments['mode'] = mode

    illud_state: IlludState = IlludState(**keyword_arguments)

    assert illud_state.buffer == expected_buffer
    assert illud_state.mode == expected_mode


# yapf: disable
@pytest.mark.parametrize('illud_state, other, expected_equality', [
    (IlludState(), 'foo', False),
    (IlludState(), IlludState(), True),
    (IlludState(Buffer('foo')), IlludState(), False),
    (IlludState(Buffer('foo')), IlludState(Buffer('bar')), False),
    (IlludState(Buffer('foo')), IlludState(Buffer('foo')), True),
    (IlludState(mode=Normal()), IlludState(mode=Insert()), False),
    (IlludState(mode=Normal()), IlludState(mode=Normal()), True),
    (IlludState(Buffer('foo'), mode=Normal()), IlludState(Buffer('bar'), Normal()), False),
    (IlludState(Buffer('foo'), mode=Normal()), IlludState(Buffer('foo'), Normal()), True),
])
# yapf: enable
def test_eq(illud_state: IlludState, other: Any, expected_equality: bool) -> None:
    """Test illud.illud_state.IlludState.__eq__."""
    equality: bool = illud_state == other

    assert equality == expected_equality
