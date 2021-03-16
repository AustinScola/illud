"""Characters."""
from typing import Set

SPACE: str = ' '
TAB: str = '\t'
VERTICAL_TAB: str = '\x0b'
FORM_FEED: str = '\x0c'
BACKSPACE: str = ''
NEWLINE: str = '\n'
CARRIAGE_RETURN: str = '\r'
ESCAPE: str = ''
CONTROL_C: str = ''
CONTROL_D: str = ''
CONTROL_F: str = ''
CONTROL_J: str = '\x0a'
CONTROL_K: str = '\x0b'
CONTROL_W: str = ''

WHITESPACE: Set[str] = {SPACE, TAB, VERTICAL_TAB, CARRIAGE_RETURN, NEWLINE, FORM_FEED}
