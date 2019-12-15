from asciicast.stream import AsciicastStream
from asciicast.text import newline, trim, replace_escapes


class Shell(object):

    def __init__(self, asciicast_stream: AsciicastStream) -> None:
        self._stream = asciicast_stream

    def appear(self, content: str) -> None:
        self._stream.write_section_comment("appear(content={})".format(replace_escapes(trim(content, 20))))
        self._stream.write_frame(content=content, ticks_after=1)

    def type_chars(self, text: str) -> None:
        self._stream.write_section_comment("type_chars(text={})".format(text))
        for _char in text:
            self._stream.write_frame(content=_char, ticks_after=1)

    def delete(self, num_chars: int) -> None:
        self._stream.write_section_comment("delete(num_chars={})".format(num_chars))
        for _ in range(0, num_chars):
            self._stream.write_frame(content="\b \b", ticks_after=1)

    def press_enter(self):
        self._stream.write_frame(content=newline(), ticks_before=4, ticks_after=1)
