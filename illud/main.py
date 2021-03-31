"""Main entry point."""
import argparse
from typing import List

from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.cursor import Cursor
from illud.illud import Illud
from illud.illud_state import IlludState
from illud.terminal import Terminal
from illud.window import Window


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


def _run_illud(parsed_arguments: argparse.Namespace) -> None:
    """Run Illud."""

    illud_state: IlludState
    if parsed_arguments.file is not None:
        illud_state = IlludState.from_file(parsed_arguments.file)
    else:
        buffer_: Buffer = Buffer()
        cursor: Cursor = Cursor(buffer_)
        terminal_size: IntegerSize2D = Terminal.get_size()
        window: Window = Window(size=terminal_size, buffer_=buffer_)
        canvas: Canvas = Canvas(terminal_size).fill(' ')
        illud_state = IlludState(terminal_size,
                                 buffer_=buffer_,
                                 cursor=cursor,
                                 selection=None,
                                 clipboard=None,
                                 window=window,
                                 canvas=canvas)

    illud: Illud = Illud(illud_state)

    illud()


def main(arguments: List[str]) -> int:
    """Main entry point."""
    argument_parser: argparse.ArgumentParser = _set_up_argument_parser()
    parsed_arguments: argparse.Namespace = _parse_arguments(argument_parser, arguments)
    _run_illud(parsed_arguments)
    return 0
