"""Test illud.exceptions.buffer_has_no_end_exception."""
from illud.exception import IlludException
from illud.exceptions.buffer_has_no_end_exception import BufferHasNoEndException


def test_inheritance() -> None:
    """Test illud.exceptions.buffer_has_no_end_exception.BufferHasNoEndException inheritance."""
    assert issubclass(BufferHasNoEndException, IlludException)


def test_init() -> None:
    """Test illud.exceptions.buffer_has_no_end_exception.BufferHasNoEndException.__init__."""
    buffer_has_no_end_exception = BufferHasNoEndException()

    assert str(buffer_has_no_end_exception) == \
        'The buffer does not have an ending index because it is empty.'
