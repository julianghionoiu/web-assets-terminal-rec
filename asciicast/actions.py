from typing import List

from asciicast.action import AsciicastAction
from asciicast.frame import AsciicastFrame
from asciicast.text import newline


class Wait(AsciicastAction):
    ticks: int

    def __init__(self, ticks: int) -> None:
        self.ticks = ticks

    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        return [AsciicastFrame(self.ticks, "")]


class Appear(AsciicastAction):
    content: str

    def __init__(self, content: str) -> None:
        self.content = content

    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        return [AsciicastFrame(1, self.content)]


class TypeChars(AsciicastAction):
    text: str

    def __init__(self, text: str) -> None:
        self.text = text

    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        return [AsciicastFrame(1, char) for char in self.text]


class Delete(AsciicastAction):
    num_chars: int

    def __init__(self, num_chars: int) -> None:
        self.num_chars = num_chars

    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        return [AsciicastFrame(1, "\b \b") for _ in range(0, self.num_chars)]


class PressEnter(AsciicastAction):

    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        return [AsciicastFrame(1, newline())]
