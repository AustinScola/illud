"""Test illud.file."""
from pathlib import Path
from typing import Any, Union
from unittest.mock import mock_open, patch

import pytest

from illud.buffer import Buffer
from illud.file import File


# yapf: disable
@pytest.mark.parametrize('path, expected_path', [
    ('foo', Path('foo')),
    ('foo.bar', Path('foo.bar')),
    ('/foo/bar', Path('/foo/bar')),
    ('/foo/bar.baz', Path('/foo/bar.baz')),
    ('foo/bar', Path('foo/bar')),
    ('foo/bar.baz', Path('foo/bar.baz')),
    ('../foo/bar', Path('../foo/bar')),
    ('../foo/bar.baz', Path('../foo/bar.baz')),
])
# yapf: enable
def test_init(path: Union[str, Path], expected_path: Path) -> None:
    """Test illud.file.__init__."""
    file: File = File(path)

    assert file.path == expected_path


# yapf: disable
@pytest.mark.parametrize('file, expected_normalized_path', [
    (File('foo'), Path('foo')),
    (File('foo/bar'), Path('foo/bar')),
    (File('foo/../bar'), Path('bar')),
])
# yapf: enable
def test_normalized_path(file: File, expected_normalized_path: Path) -> None:
    """Test illud.file.normalized_path."""
    normalized_path = file.normalized_path

    assert normalized_path == expected_normalized_path


# yapf: disable
@pytest.mark.parametrize('file, other, expected_equality', [
    (File('foo'), 'foo', False),
    (File('foo'), File('bar'), False),
    (File('foo'), File('foo'), True),
    (File('foo/../bar'), File('bar'), True),
])
# yapf: enable
def test_eq(file: File, other: Any, expected_equality: bool) -> None:
    """Test illud.file.__eq__."""
    equality = file == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('file, buffer_', [
    (File('foo'), Buffer()),
    (File('foo'), Buffer('bar')),
])
# yapf: enable
def test_write(file: File, buffer_: Buffer) -> None:
    """Test illud.file.write."""
    with patch('builtins.open', mock_open()) as open_mock:
        file.write(buffer_)

        open_mock().write.assert_called_once_with(buffer_.string)
