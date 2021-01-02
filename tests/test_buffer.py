"""Test illud.buffer."""
from typing import Any

import pytest

from illud.buffer import Buffer


# yapf: disable
@pytest.mark.parametrize('string', [
    (''),
    ('foo'),
])
# yapf: enable
def test_init(string: str) -> None:
    """Test illud.buffer.Buffer.__init__."""
    buffer_: Buffer = Buffer(string)

    assert buffer_.string == string


# yapf: disable
@pytest.mark.parametrize('buffer_, other, expected_equality', [
    (Buffer(''), 'foo', False),
    (Buffer(''), Buffer('foo'), False),
    (Buffer(''), Buffer(''), True),
    (Buffer('foo'), Buffer('foo'), True),
])
# yapf: enable
def test_eq(buffer_: Buffer, other: Any, expected_equality: bool) -> None:
    """Test illud.buffer.Buffer.__eq__."""
    equality: bool = buffer_ == other

    assert equality == expected_equality
