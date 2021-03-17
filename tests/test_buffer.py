"""Test illud.buffer."""
from typing import Any, Dict, List, Optional, Type, Union

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D

from illud.buffer import Buffer
from illud.exceptions.buffer_has_no_end_exception import BufferHasNoEndException
from illud.exceptions.buffer_index_exception import BufferIndexException


# yapf: disable
@pytest.mark.parametrize('string, pass_string, expected_string', [
    ('', False, ''),
    ('', True, ''),
    ('foo', True, 'foo'),
])
# yapf: enable
def test_init(string: str, pass_string: bool, expected_string: str) -> None:
    """Test illud.buffer.Buffer.__init__."""
    arguments: List[Any] = []
    if pass_string:
        arguments.append(string)

    buffer_: Buffer = Buffer(*arguments)

    assert buffer_.string == expected_string


# yapf: disable
@pytest.mark.parametrize('buffer_, expected_end, expected_exception', [
    (Buffer(), None, BufferHasNoEndException()),
    (Buffer('a'), 0, None),
    (Buffer('ab'), 1, None),
    (Buffer('abc'), 2, None),
])
# yapf: enable
def test_end(buffer_: Buffer, expected_end: Optional[int],
             expected_exception: Optional[Exception]) -> None:
    """Test illud.buffer.Buffer.__init__."""
    if expected_exception is not None:
        with pytest.raises(type(expected_exception)):
            buffer_.end  # pylint: disable=pointless-statement
    else:
        end: int = buffer_.end

        assert end == expected_end


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
@pytest.mark.parametrize('buffer_, expected_representation', [
    (Buffer(), 'Buffer()'),
    (Buffer('foo'), "Buffer(string='foo')"),
    (Buffer("'"), 'Buffer(string="\'")'),
    (Buffer('"'), 'Buffer(string=\'"\')'),
])
# yapf: enable
def test_repr(buffer_: Buffer, expected_representation: str) -> None:
    """Test illud.buffer.Buffer.__repr__."""
    representation: str = repr(buffer_)

    assert representation == expected_representation


# yapf: disable
@pytest.mark.parametrize('buffer_, index_or_slice, expected_item, expected_exception', [
    (Buffer(), 0, None, IndexError),
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


# yapf: disable
@pytest.mark.parametrize('buffer_, expected_length', [
    (Buffer(), 0),
    (Buffer('a'), 1),
    (Buffer('foo'), 3),
    (Buffer('foo\nbar'), 7),
])
# yapf: enable
def test_len(buffer_: Buffer, expected_length: int) -> None:
    """Test illud.buffer.Buffer.__len__."""
    length: int = len(buffer_)

    assert length == expected_length


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('buffer_, substring, start, pass_start, end, pass_end, expected_index, expected_exception', [
    (Buffer(), '', None, False, None, False, 0, None),
    (Buffer(), '', None, False, None, True, 0, None),
    (Buffer(), '', None, True, None, False, 0, None),
    (Buffer(), '', None, True, None, True, 0, None),
    (Buffer(), 'foo', None, False, None, False, None, ValueError),
    (Buffer(), 'foo', None, False, None, True, None, ValueError),
    (Buffer(), 'foo', None, True, None, False, None, ValueError),
    (Buffer(), 'foo', None, True, None, True, None, ValueError),
    (Buffer('foo'), 'foo', None, False, None, False, 0, None),
    (Buffer('foo'), 'foo', None, False, None, True, 0, None),
    (Buffer('foo'), 'foo', None, True, None, False, 0, None),
    (Buffer('foo'), 'foo', None, True, None, True, 0, None),
    (Buffer('foobar'), 'bar', None, False, None, False, 3, None),
    (Buffer('foobar'), 'foo', 3, True, None, False, None, ValueError),
    (Buffer('foobar'), 'foo', None, False, 1, True, None, ValueError),
    (Buffer('foobar'), 'foo', 0, True, 1, True, None, ValueError),
    (Buffer('foobar'), 'baz', None, False, None, False, None, ValueError),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_index(buffer_: Buffer, substring: str, start: Optional[int], pass_start: bool,
               end: Optional[int], pass_end: bool, expected_index: Optional[int],
               expected_exception: Optional[Type[Exception]]) -> None:
    """Test illud.buffer.Buffer.index."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_start:
        keyword_arguments['start'] = start
    if pass_end:
        keyword_arguments['end'] = end

    if expected_exception is not None:
        with pytest.raises(expected_exception):
            buffer_.index(substring, **keyword_arguments)
    else:
        index = buffer_.index(substring, **keyword_arguments)

        assert index == expected_index


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('buffer_, substring, start, pass_start, end, pass_end, expected_index, expected_exception', [
    (Buffer(), '', None, False, None, False, 0, None),
    (Buffer(), '', None, False, None, True, 0, None),
    (Buffer(), '', None, True, None, False, 0, None),
    (Buffer(), '', None, True, None, True, 0, None),
    (Buffer('foo'), 'foo', None, False, None, False, 0, None),
    (Buffer('foo'), 'foo', None, False, None, True, 0, None),
    (Buffer('foo'), 'foo', None, True, None, False, 0, None),
    (Buffer('foo'), 'foo', None, True, None, True, 0, None),
    (Buffer('aba'), 'a', None, False, None, False, 2, None),
    (Buffer('aba'), 'a', None, False, None, True, 2, None),
    (Buffer('aba'), 'a', None, True, None, False, 2, None),
    (Buffer('aba'), 'a', None, True, None, True, 2, None),
    (Buffer('foobar'), 'bar', None, False, None, False, 3, None),
    (Buffer('foobar'), 'foo', 3, True, None, False, None, ValueError),
    (Buffer('foobar'), 'foo', None, False, 1, True, None, ValueError),
    (Buffer('foobar'), 'foo', 0, True, 1, True, None, ValueError),
    (Buffer('foobar'), 'baz', None, False, None, False, None, ValueError),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_reverse_index(buffer_: Buffer, substring: str, start: Optional[int], pass_start: bool,
                       end: Optional[int], pass_end: bool, expected_index: Optional[int],
                       expected_exception: Optional[Type[Exception]]) -> None:
    """Test illud.buffer.Buffer.reverse_index."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_start:
        keyword_arguments['start'] = start
    if pass_end:
        keyword_arguments['end'] = end

    if expected_exception is not None:
        with pytest.raises(expected_exception):
            buffer_.reverse_index(substring, **keyword_arguments)
    else:
        index = buffer_.reverse_index(substring, **keyword_arguments)

        assert index == expected_index


# yapf: disable
@pytest.mark.parametrize('buffer_, index, expected_exception, expected_position', [
    (Buffer(), 0, BufferIndexException(0, 0), None),
    (Buffer(), 1, BufferIndexException(1, 0), None),
    (Buffer('foo'), 0, None, IntegerPosition2D()),
    (Buffer('foo'), 1, None, IntegerPosition2D(1, 0)),
    (Buffer('foo\nbar'), 0, None, IntegerPosition2D()),
    (Buffer('foo\nbar'), 4, None, IntegerPosition2D(0, 1)),
    (Buffer('foo\nbar'), 6, None, IntegerPosition2D(2, 1)),
])
# yapf: enable
def test_get_position(buffer_: Buffer, index: int,
                      expected_exception: Optional[BufferIndexException],
                      expected_position: IntegerPosition2D) -> None:
    """Test illud.buffer.Buffer.get_position."""
    if expected_exception is not None:
        with pytest.raises(type(expected_exception)):
            buffer_.get_position(index)
    else:
        position: IntegerPosition2D = buffer_.get_position(index)

        assert position == expected_position


# yapf: disable
@pytest.mark.parametrize('buffer_, index, expected_exception, expected_row', [
    (Buffer(), 1, BufferIndexException(1, 0), None),
    (Buffer(), 0, None, 0),
    (Buffer(), 0, None, 0),
    (Buffer('foo'), 0, None, 0),
    (Buffer('foo'), 1, None, 0),
    (Buffer('foo'), 2, None, 0),
    (Buffer('foo\nbar'), 3, None, 0),
    (Buffer('foo\nbar'), 4, None, 1),
    (Buffer('foo\nbar'), 5, None, 1),
    (Buffer('foo\nbar'), 6, None, 1),
    (Buffer('foo\nbar\nbaz'), 7, None, 1),
    (Buffer('foo\nbar\nbaz'), 8, None, 2),
    (Buffer('foo\nbar\nbaz'), 9, None, 2),
    (Buffer('foo\nbar\nbaz'), 10, None, 2),
])
# yapf: enable
def test_get_row(buffer_: Buffer, index: int, expected_exception: Optional[BufferIndexException],
                 expected_row: int) -> None:
    """Test illud.buffer.Buffer.get_row."""
    if expected_exception is not None:
        with pytest.raises(type(expected_exception)):
            buffer_.get_row(index)
    else:
        row: int = buffer_.get_row(index)

        assert row == expected_row


# yapf: disable
@pytest.mark.parametrize('buffer_, index, expected_exception, expected_column', [
    (Buffer(), 0, BufferIndexException(0, 0), None),
    (Buffer(' '), 0, None, 0),
    (Buffer('\n'), 0, None, 0),
    (Buffer('foo'), 0, None, 0),
    (Buffer('foo'), 1, None, 1),
    (Buffer('foo'), 2, None, 2),
    (Buffer('foo\nbar'), 3, None, 3),
    (Buffer('foo\nbar'), 4, None, 0),
    (Buffer('foo\nbar'), 5, None, 1),
    (Buffer('foo\nbar'), 6, None, 2),
])
# yapf: enable
def test_get_column(buffer_: Buffer, index: int, expected_exception: Optional[BufferIndexException],
                    expected_column: int) -> None:
    """Test illud.buffer.Buffer.get_column."""
    if expected_exception is not None:
        with pytest.raises(type(expected_exception)):
            buffer_.get_column(index)
    else:
        column: int = buffer_.get_column(index)

        assert column == expected_column


# pylint: enable=too-many-arguments


# yapf: disable
@pytest.mark.parametrize('buffer_, string, index, expected_buffer_after', [
    (Buffer(), '', 0, Buffer()),
    (Buffer(), 'f', 0, Buffer('f')),
    (Buffer(), 'foo', 0, Buffer('foo')),
    (Buffer('bar'), 'foo', 0, Buffer('foobar')),
    (Buffer('foo'), '', 1, Buffer('foo')),
    (Buffer('fo'), 'o', 1, Buffer('foo')),
    (Buffer('foo'), 'bar', 3, Buffer('foobar')),
])
# yapf: enable
def test_insert(buffer_: Buffer, string: str, index: int, expected_buffer_after: Buffer) -> None:
    """Test illud.buffer.Buffer.insert."""
    buffer_.insert(string, index)

    assert buffer_ == expected_buffer_after


# yapf: disable
@pytest.mark.parametrize('buffer_, index, expected_exception, expected_buffer_after', [
    (Buffer(), -1, BufferIndexException(-1, 0), None),
    (Buffer(), 0, BufferIndexException(0, 0), None),
    (Buffer(), 1, BufferIndexException(1, 0), None),
    (Buffer('spam'), -1, BufferIndexException(-1, 4), None),
    (Buffer('spam'), 0, None, Buffer('pam')),
    (Buffer('spam'), 1, None, Buffer('sam')),
    (Buffer('spam'), 2, None, Buffer('spm')),
    (Buffer('spam'), 3, None, Buffer('spa')),
    (Buffer('spam'), 4, BufferIndexException(4, 4), None),
])
# yapf: enable
def test_delete(buffer_: Buffer, index: int, expected_exception: Optional[BufferIndexException],
                expected_buffer_after: Optional[Buffer]) -> None:
    """Test illud.buffer.Buffer.delete."""
    if expected_exception is not None:
        with pytest.raises(type(expected_exception), match=str(expected_exception)):
            buffer_.delete(index)
    else:
        buffer_.delete(index)

        assert buffer_ == expected_buffer_after
