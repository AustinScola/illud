"""Test illud.main"""
import argparse
from typing import Any, Dict, List, Union
from unittest.mock import patch

import pytest

from illud.main import _parse_arguments, _run_illud, _set_up_argument_parser, main


def test_set_up_argument_parser() -> None:
    """Test illud.main._set_up_argument_parser"""
    argument_parser: argparse.ArgumentParser = _set_up_argument_parser()

    _assert_argument_parser_is_set_up(argument_parser)


def _assert_argument_parser_is_set_up(argument_parser: argparse.ArgumentParser) -> None:
    """Assert that the argument parser is set up."""
    assert argument_parser.description == 'A text buffer editor and terminal viewer.'
    assert argument_parser.prog == 'python3 -m illud'


def argument_parser_from_dict(dictionary: Dict[str, Any]) -> argparse.ArgumentParser:
    """Return an argument parser from a dictionary specification."""
    argument_parser = argparse.ArgumentParser()

    try:
        for argument in dictionary['arguments']:
            name_or_flags: Union[str, List[str]] = argument['name_or_flags']
            if isinstance(name_or_flags, str):
                name: str = name_or_flags
                argument_parser.add_argument(name)
            else:
                flags: List[str] = name_or_flags
                argument_parser.add_argument(*flags)
    except KeyError:
        pass

    return argument_parser


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('argument_parser, arguments, expected_parsed_arguments', [
    (argument_parser_from_dict({}), [], argparse.Namespace()),
    (argument_parser_from_dict({'arguments': [{'name_or_flags': 'foo'}]}), ['1'], argparse.Namespace(foo='1')),
    (argument_parser_from_dict({'arguments': [{'name_or_flags': ['--foo', '-f']}]}), [], argparse.Namespace(foo=None)),
    (argument_parser_from_dict({'arguments': [{'name_or_flags': ['--foo', '-f']}]}), ['--foo', '1'], argparse.Namespace(foo='1')),
])
# yapf: enable # pylint: disable=enable-too-long
def test_parse_arguments(argument_parser: argparse.ArgumentParser, arguments: List[str],
                         expected_parsed_arguments: argparse.Namespace) -> None:
    """Test illud.main._parse_arguments."""
    parsed_arguments: argparse.Namespace = _parse_arguments(argument_parser, arguments)

    assert parsed_arguments == expected_parsed_arguments


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('parsed_arguments', [
    (argparse.Namespace()),
])
# yapf: enable # pylint: enable=line-too-long
def test_run_illud(parsed_arguments: argparse.Namespace) -> None:
    """Test illud.main._run_illud."""
    _run_illud(parsed_arguments)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, expected_return_value', [
    ([], 0),
])
# yapf: enable # pylint: enable=line-too-long
def test_main(arguments: List[str], expected_return_value: int) -> None:
    """Test illud.main.main."""
    with patch('illud.main._set_up_argument_parser') as set_up_argument_parser_mock, \
        patch('illud.main._parse_arguments') as parse_arguments_mock, \
        patch('illud.main._run_illud') as run_illud_mock:
        return_value: int = main(arguments)

        set_up_argument_parser_mock.assert_called_once()
        parse_arguments_mock.assert_called_once()
        run_illud_mock.assert_called_once()

    assert return_value == expected_return_value
