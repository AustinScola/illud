"""Test illud.buffer."""
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
