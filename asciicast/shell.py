from asciicast.frame import AsciicastFrame
from asciicast.stream import AsciicastStream
from asciicast.text import newline


class Shell(object):

    def __init__(self, asciicast_stream: AsciicastStream) -> None:
        self._asciicast_stream = asciicast_stream

    def wait(self, ticks: int) -> None:
        self._asciicast_stream.write_frame(AsciicastFrame(ticks, ""))

    def appear(self, content: str) -> None:
        self._asciicast_stream.write_frame(AsciicastFrame(1, content))

    def type_chars(self, text: str) -> None:
        for _char in text:
            self._asciicast_stream.write_frame(AsciicastFrame(1, _char))

    def delete(self, num_chars: int) -> None:
        for _ in range(0, num_chars):
            self._asciicast_stream.write_frame(AsciicastFrame(1, "\b \b"))

    def press_enter(self):
        self._asciicast_stream.write_frame(AsciicastFrame(1, newline()))
