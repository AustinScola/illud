"""ANSI escape codes for the cursor position."""
from illud.ansi.escape_codes.control import CONTROL_SEQUENCE_INTRODUCER

DEVICE_STATUS_REPORT = CONTROL_SEQUENCE_INTRODUCER + '6n'
