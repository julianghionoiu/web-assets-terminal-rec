
from stream import AsciicastStream


class VimEditor(object):
    _asciicast_stream: AsciicastStream
    _editor_contents: str

    def __init__(self, asciicast_stream: AsciicastStream, ) -> None:
        self._asciicast_stream = asciicast_stream
        self._editor_contents = ""
        self._cursor_row = 0
        self._cursor_column = 0
        self._viewport_row = 0
        self._viewport_column = 0

    def display_content(self, block_of_text):
        self._editor_contents = block_of_text

