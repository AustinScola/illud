"""Main entry point."""
import argparse
from typing import List

from illud.illud import Illud


def _set_up_argument_parser() -> argparse.ArgumentParser:
    """Set up an argument parser."""
    argument_parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog='python3 -m illud', description='A text buffer editor and terminal viewer.')

    argument_parser.add_argument('file', nargs='?', help='a file to open')

    return argument_parser


def _parse_arguments(argument_parser: argparse.ArgumentParser,
                     arguments: List[str]) -> argparse.Namespace:
    """Return parsed arguments."""
    parsed_arguments: argparse.Namespace = argument_parser.parse_args(arguments)
    return parsed_arguments


def _run_illud(parsed_arguments: argparse.Namespace) -> None:  # pylint: disable=unused-argument
    """Run Illud."""
    illud: Illud = Illud()
    illud()


def main(arguments: List[str]) -> int:
    """Main entry point."""
    argument_parser: argparse.ArgumentParser = _set_up_argument_parser()
    parsed_arguments: argparse.Namespace = _parse_arguments(argument_parser, arguments)
    _run_illud(parsed_arguments)
    return 0
