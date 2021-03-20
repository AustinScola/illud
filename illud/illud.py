"""A text buffer editor and terminal viewer."""
import sys
from typing import Any, Optional

from illud.canvas import Canvas
from illud.character import Character
from illud.cursor import Cursor
from illud.exceptions.quit_exception import QuitException
from illud.illud_input import IlludInput
from illud.illud_state import IlludState
from illud.inputs.signal_listener import SignalListener
from illud.mode import Mode
from illud.repl import REPL
from illud.signal_ import Signal
from illud.signal_handler import SignalHandler
from illud.terminal import Terminal
from illud.window import Window


class Illud(REPL):
    """A text buffer editor and terminal viewer."""
    def __init__(self, initial_state: Optional[IlludState] = None) -> None:
        self._terminal: Terminal = Terminal()
        self._signal_listener: SignalListener = SignalListener()
        self._signal_handler: SignalHandler = SignalHandler()

        self._state: IlludState
        if initial_state is None:
            self._state = IlludState(terminal_size=self._terminal.get_size())
        else:
            self._state = initial_state

    def startup(self) -> None:
        self._terminal.enable_alternative_screen()
        self.print(None)
        self._signal_listener.start()

    def read(self) -> IlludInput:
        input_: IlludInput
        if self._signal_listener:
            signal: Signal = next(self._signal_listener)
            input_ = signal
        else:
            character: Character = self._terminal.get_character()
            input_ = character
        return input_

    def evaluate(self, input_: IlludInput) -> None:
        if isinstance(input_, Character):
            character: Character = input_
            mode: Mode = self._state.mode
            mode.evaluate(self._state, character)
        else:
            signal: Signal = input_
            self._signal_handler.handle(self._state, signal)

    def print(self, result: Any) -> None:
        canvas: Canvas = self._state.canvas
        canvas.remove_inversions()

        window: Window = self._state.window

        self._terminal.draw_window(window, canvas)

        cursor: Cursor = self._state.cursor
        self._terminal.draw_cursor(cursor, window.offset, canvas)

        canvas.render()

        self._terminal.update()

    def catch(self, exception: Exception) -> None:
        self._terminal.disable_alternative_screen()

        if isinstance(exception, QuitException):
            sys.exit()

        raise exception
