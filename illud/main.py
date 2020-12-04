"""Main entry point."""
import argparse
from typing import List


def _set_up_argument_parser() -> argparse.ArgumentParser:
    """Set up an argument parser."""
    argument_parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog='python3 -m illud', description='A text buffer editor and terminal viewer.')
    return argument_parser


def main(arguments: List[str]) -> int:  # pylint: disable=unused-argument
    """Main entry point."""
    argument_parser: argparse.ArgumentParser = _set_up_argument_parser()  # pylint: disable=unused-variable
    return 0
