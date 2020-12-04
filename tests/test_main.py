"""Test illud.main"""
import argparse
from typing import List
from unittest.mock import patch

import pytest

from illud.main import _set_up_argument_parser, main


def test_set_up_argument_parser() -> None:
    """Test illud.main._set_up_argument_parser"""
    argument_parser: argparse.ArgumentParser = _set_up_argument_parser()

    _assert_argument_parser_is_set_up(argument_parser)


def _assert_argument_parser_is_set_up(argument_parser: argparse.ArgumentParser) -> None:
    """Assert that the argument parser is set up."""
    assert argument_parser.description == 'A text buffer editor and terminal viewer.'
    assert argument_parser.prog == 'python3 -m illud'


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, expected_return_value', [
    ([], 0),
])
# yapf: enable # pylint: enable=line-too-long
def test_main(arguments: List[str], expected_return_value: int) -> None:
    """Test illud.main.main."""
    with patch('illud.main._set_up_argument_parser') as set_up_argument_parser_mock:
        return_value: int = main(arguments)

        set_up_argument_parser_mock.assert_called_once()

    assert return_value == expected_return_value
