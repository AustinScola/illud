"""Test illud.outputs.standard_output."""
import sys
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from illud.output import Output
from illud.outputs.standard_output import StandardOutput


def test_inheritance() -> None:
    """Test illud.outputs.standard_output.StandardOutput inheritance."""
    assert issubclass(StandardOutput, Output)


def test_init() -> None:
    """Test illud.outputs.standard_output.StandardOutput.__init__."""
    standard_output: StandardOutput = StandardOutput()

    assert standard_output._stdout == sys.stdout  # pylint: disable=protected-access


# yapf: disable
@pytest.mark.parametrize('standard_output, other, expected_equality', [
    (StandardOutput(), 'foo', False),
    (StandardOutput(), StandardOutput(), True),
])
# yapf: enable
def test_eq(standard_output: StandardOutput, other: Any, expected_equality: bool) -> None:
    """Test illud.outputs.standard_output.StandardOutput.__eq__."""
    equality: bool = standard_output == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('string', [
    (''),
    ('foo'),
])
# yapf: enable
def test_write(string: str) -> None:
    """Test illud.outputs.standard_output.StandardOutput.write."""
    stdout_mock = MagicMock(sys.stdout)
    with patch('sys.stdout', stdout_mock):
        standard_output: StandardOutput = StandardOutput()

    standard_output.write(string)

    stdout_mock.write.assert_called_once_with(string)


def test_flush() -> None:
    """Test illud.outputs.standard_output.StandardOutput.flush."""
    stdout_mock = MagicMock(sys.stdout)
    with patch('sys.stdout', stdout_mock):
        standard_output: StandardOutput = StandardOutput()

    standard_output.flush()

    stdout_mock.flush.assert_called_once_with()
