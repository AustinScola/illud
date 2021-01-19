"""Test illud.buffer."""
from typing import Any, List, Optional, Type, Union

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


# yapf: disable
@pytest.mark.parametrize('buffer_, index_or_slice, expected_item, expected_exception', [
    (Buffer(''), 0, None, IndexError),
    (Buffer('f'), 0, 'f', None),
    (Buffer('foo'), 1, 'o', None),
    (Buffer('foo'), -1, 'o', None),
    (Buffer('foo'), slice(0), '', None),
    (Buffer('foo'), slice(1), 'f', None),
    (Buffer('foo'), slice(2), 'fo', None),
    (Buffer('foo'), slice(3), 'foo', None),
    (Buffer('foobar'), slice(0, 3), 'foo', None),
    (Buffer('foobar'), slice(0, 5, 2), 'foa', None),
])
# yapf: enable
def test_getitem(buffer_: Buffer, index_or_slice: Union[int, slice],
                 expected_item: Optional[Union[str, List[str]]],
                 expected_exception: Optional[Type[Exception]]) -> None:
    """Test illud.buffer.Buffer.__getitem__."""
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            buffer_.__getitem__(index_or_slice)
    else:
        item: Union[str, List[str]] = buffer_.__getitem__(index_or_slice)

        assert item == expected_item
