"""Test illud.cursor."""
from typing import Any

import pytest

from illud.buffer import Buffer
from illud.cursor import Cursor


# yapf: disable
@pytest.mark.parametrize('buffer_,  position', [
    (Buffer(), 0),
    (Buffer('foo'), 1),
])
# yapf: enable
def test_init(buffer_: Buffer, position: int) -> None:
    """Test illud.cursor.Cursor.__init__."""
    cursor: Cursor = Cursor(buffer_, position)

    assert cursor.position == position
    assert cursor.buffer is buffer_


# yapf: disable
@pytest.mark.parametrize('cursor, other, expected_equality', [
    (Cursor(Buffer(), 0), 'foo', False),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('foo'), 1), False),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('bar'), 1), False),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('foo'), 0), True),
])
# yapf: enable
def test_eq(cursor: Cursor, other: Any, expected_equality: bool) -> None:
    """Test illud.cursor.Cursor.__eq__."""
    equality: bool = cursor == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('cursor, expected_representation', [
    (Cursor(Buffer(), 0), 'Cursor(Buffer(), 0)'),
    (Cursor(Buffer('foo'), 0), "Cursor(Buffer('foo'), 0)"),
])
# yapf: enable
def test_repr(cursor: Cursor, expected_representation: str) -> None:
    """Test illud.cursor.Cursor.__repr__."""
    representation: str = repr(cursor)

    assert representation == expected_representation


# yapf: disable
@pytest.mark.parametrize('cursor, string, expected_cursor_after', [
    (Cursor(Buffer(), 0), '', Cursor(Buffer(), 0)),
    (Cursor(Buffer(), 0), 'f', Cursor(Buffer('f'), 1)),
    (Cursor(Buffer(), 0), 'foo', Cursor(Buffer('foo'), 3)),
    (Cursor(Buffer('bar'), 0), 'foo', Cursor(Buffer('foobar'), 3)),
    (Cursor(Buffer('foo'), 1), '', Cursor(Buffer('foo'), 1)),
    (Cursor(Buffer('fo'), 1), 'o', Cursor(Buffer('foo'), 2)),
    (Cursor(Buffer('foo'), 3), 'bar', Cursor(Buffer('foobar'), 6)),
])
# yapf: enable
def test_insert(cursor: Cursor, string: str, expected_cursor_after: Cursor) -> None:
    """Test illud.cursor.Cursor.insert."""
    cursor.insert(string)

    assert cursor == expected_cursor_after
