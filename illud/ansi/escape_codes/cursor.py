"""ANSI escape codes for the cursor position."""
from illud.ansi.escape_codes.control import CONTROL_SEQUENCE_INTRODUCER
from illud.integer_position_2d import IntegerPosition2D

DEVICE_STATUS_REPORT = CONTROL_SEQUENCE_INTRODUCER + '6n'


def get_move_cursor(position: IntegerPosition2D) -> str:
    """Return an escape code to move the cursor to the given position."""
    one_based_position = position + IntegerPosition2D(1, 1)

    move_cursor_command: str = CONTROL_SEQUENCE_INTRODUCER
    if one_based_position.y != 1:
        move_cursor_command += str(one_based_position.y)
    move_cursor_command += ';'
    if one_based_position.x != 1:
        move_cursor_command += str(one_based_position.x)
    move_cursor_command += 'H'

    return move_cursor_command
