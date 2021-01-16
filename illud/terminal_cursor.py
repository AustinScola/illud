"""The cursor of a terminal."""
from illud.ansi.escape_codes.cursor import DEVICE_STATUS_REPORT
from illud.inputs.standard_input import StandardInput
from illud.integer_position_2d import IntegerPosition2D
from illud.outputs.standard_output import StandardOutput


class TerminalCursor():  # pylint: disable=too-few-public-methods
    """The cursor of a terminal."""
    def __init__(self, standard_input: StandardInput, standard_output: StandardOutput):
        self._standard_input: StandardInput = standard_input
        self._standard_output: StandardOutput = standard_output

        self._position: IntegerPosition2D = self._get_position_from_terminal()

    def _get_position_from_terminal(self) -> IntegerPosition2D:
        """Return the position of the cursor as reported by the terminal."""
        self._standard_output.write(DEVICE_STATUS_REPORT)

        y: int = self._standard_input.maybe_read_integer(default=0)  # pylint: disable=invalid-name
        self._standard_input.expect(';')
        x: int = self._standard_input.maybe_read_integer(default=0)  # pylint: disable=invalid-name
        self._standard_input.expect('R')

        return IntegerPosition2D(x, y)
