"""Test illud.illud_state."""
from typing import Any, Dict, Optional

import pytest

from illud.buffer import Buffer
from illud.illud_state import IlludState
from illud.state import State


def test_inheritance() -> None:
    """Test illud.illud_state.IlludState inheritance."""
    assert issubclass(IlludState, State)


# yapf: disable
@pytest.mark.parametrize('buffer_, pass_buffer, expected_buffer', [
    (None, False, Buffer('')),
    (Buffer(''), True, Buffer('')),
    (None, True, Buffer('')),
    (Buffer('foo'), True, Buffer('foo')),
])
# yapf: enable
def test_init(buffer_: Optional[Buffer], pass_buffer: bool, expected_buffer: Buffer) -> None:
    """Test illud.illud_state.IlludState.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_buffer:
        keyword_arguments['buffer_'] = buffer_

    illud_state: IlludState = IlludState(**keyword_arguments)

    assert illud_state.buffer == expected_buffer


# yapf: disable
@pytest.mark.parametrize('illud_state, other, expected_equality', [
    (IlludState(), 'foo', False),
    (IlludState(), IlludState(), True),
])
# yapf: enable
def test_eq(illud_state: IlludState, other: Any, expected_equality: bool) -> None:
    """Test illud.illud_state.IlludState.__eq__."""
    equality: bool = illud_state == other

    assert equality == expected_equality
