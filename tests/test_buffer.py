"""Test illud.buffer."""
from typing import Any, List, Optional

import pytest

from illud.buffer import Buffer


# yapf: disable
@pytest.mark.parametrize('string, expected_string', [
    (None, ''),
    ('', ''),
    ('foo', 'foo'),
])
# yapf: enable
def test_init(string: Optional[str], expected_string: str) -> None:
    """Test illud.buffer.Buffer.__init__."""
    arguments: List[Any] = []
    if string is not None:
        arguments.append(string)

    buffer_: Buffer = Buffer(*arguments)

    assert buffer_.string == expected_string


# yapf: disable
@pytest.mark.parametrize('buffer_, other, expected_equality', [
    (Buffer(), 'foo', False),
    (Buffer(), Buffer('foo'), False),
    (Buffer(), Buffer(), True),
    (Buffer('foo'), Buffer('foo'), True),
])
# yapf: enable
def test_eq(buffer_: Buffer, other: Any, expected_equality: bool) -> None:
    """Test illud.buffer.Buffer.__eq__."""
    equality: bool = buffer_ == other

    assert equality == expected_equality
