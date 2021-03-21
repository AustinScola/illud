"""Test illud.main"""
import argparse
from typing import Any, Dict, List, Optional, Union
from unittest.mock import MagicMock, patch

import pytest
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.cursor import Cursor
from illud.file import File
from illud.illud import Illud
from illud.illud_state import IlludState
from illud.main import _parse_arguments, _run_illud, _set_up_argument_parser, main
from illud.window import Window


def test_set_up_argument_parser() -> None:
    """Test illud.main._set_up_argument_parser"""
    argument_parser: argparse.ArgumentParser = _set_up_argument_parser()

    _assert_argument_parser_is_set_up(argument_parser)
    _assert_argument_parser_has_expected_arguments(argument_parser)


def _assert_argument_parser_is_set_up(argument_parser: argparse.ArgumentParser) -> None:
    """Assert that the argument parser is set up."""
    assert argument_parser.description == 'A text buffer editor and terminal viewer.'
    assert argument_parser.prog == 'python3 -m illud'


def _assert_argument_parser_has_expected_arguments(
        argument_parser: argparse.ArgumentParser) -> None:
    """Assert that the argument parser has the expected arguments."""
    _, file_argument = argument_parser._actions  # pylint: disable=protected-access

    assert file_argument.dest == 'file'
    assert file_argument.nargs == '?'
    assert file_argument.help == 'a file to open'


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
# yapf: enable # pylint: enable=line-too-long
def test_parse_arguments(argument_parser: argparse.ArgumentParser, arguments: List[str],
                         expected_parsed_arguments: argparse.Namespace) -> None:
    """Test illud.main._parse_arguments."""
    parsed_arguments: argparse.Namespace = _parse_arguments(argument_parser, arguments)

    assert parsed_arguments == expected_parsed_arguments


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('parsed_arguments, illud_state_from_file, terminal_size, expected_init_arguments', [
    (argparse.Namespace(file=None), None, IntegerSize2D(120, 80), [IlludState(Buffer(), Cursor(), window=Window(size=IntegerSize2D(120, 80)), canvas=Canvas(IntegerSize2D(120, 80), [[' ' for _ in range(120)] for _ in range(80)]), terminal_size=IntegerSize2D(120, 80))]),
    (argparse.Namespace(file='foo.py'), IlludState(Buffer('Lorem ipsum'), canvas=Canvas(IntegerSize2D(120, 80), [[' ' for _ in range(120)] for _ in range(80)]), terminal_size=IntegerSize2D(120, 80), file=File('foo.py')), IntegerSize2D(120, 80), [IlludState(Buffer('Lorem ipsum'), canvas=Canvas(IntegerSize2D(120, 80), [[' ' for _ in range(120)] for _ in range(80)]), terminal_size=IntegerSize2D(120, 80), file=File('foo.py'))]),
])
# yapf: enable # pylint: enable=line-too-long
def test_run_illud(parsed_arguments: argparse.Namespace, illud_state_from_file: Optional[str],
                   terminal_size: IntegerSize2D, expected_init_arguments: List[Any]) -> None:
    """Test illud.main._run_illud."""
    illud_mock = MagicMock(Illud, autospec=True)
    illud_init_mock = MagicMock(Illud.__init__, autospec=True, return_value=illud_mock)
    with patch('illud.main.Illud', illud_init_mock), \
        patch('illud.illud_state.IlludState.from_file', return_value=illud_state_from_file), \
        patch('illud.main.Terminal.get_size', return_value=terminal_size):

        _run_illud(parsed_arguments)

        illud_mock.assert_called_once()

    illud_init_mock.assert_called_once_with(*expected_init_arguments)

    if illud_state_from_file is None:
        illud_init_arguments, _ = illud_init_mock.call_args
        illud_state: IlludState = illud_init_arguments[0]

        assert illud_state.cursor.buffer is illud_state.buffer
        assert illud_state.window.buffer is illud_state.buffer


# yapf: disable
@pytest.mark.parametrize('arguments, expected_return_value', [
    ([], 0),
])
# yapf: enable
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
