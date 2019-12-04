from typing import List

from asciicast.action import AsciicastAction
from asciicast.frame import AsciicastFrame
from asciicast.text import newline


class Wait(AsciicastAction):
    _ticks: int

    def __init__(self, ticks: int) -> None:
        self._ticks = ticks

    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        return [AsciicastFrame(self._ticks, "")]


class Appear(AsciicastAction):
    _content: str

    def __init__(self, content: str) -> None:
        self._content = content

    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        return [AsciicastFrame(1, self._content)]


class TypeChars(AsciicastAction):
    _text: str

    def __init__(self, text: str) -> None:
        self._text = text

    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        return [AsciicastFrame(1, char) for char in self._text]


class Delete(AsciicastAction):
    _num_chars: int

    def __init__(self, num_chars: int) -> None:
        self._num_chars = num_chars

    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        return [AsciicastFrame(1, "\b \b") for _ in range(0, self._num_chars)]


class PressEnter(AsciicastAction):

    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        return [AsciicastFrame(1, newline())]
