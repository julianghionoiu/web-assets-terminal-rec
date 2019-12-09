from asciicast.stream import AsciicastStream
from asciicast.text import replace_escapes, trim, newline


class VimEditor(object):
    _stream: AsciicastStream
    _data_lines: list

    def __init__(self, asciicast_stream: AsciicastStream, ) -> None:
        self._stream = asciicast_stream
        self._viewport_height = asciicast_stream.height - 1
        self._viewport_cursor_row = 0
        self._viewport_cursor_max_row = self._viewport_height - 1
        self._data_lines = []
        self._data_line_max_row = self._viewport_height

    def display_content(self, block_of_text):
        self._data_lines = block_of_text.split()
        short_content: str = replace_escapes(trim(block_of_text, 20))
        self._stream.write_section_comment("display_content(block_of_text={})".format(short_content))
        self._stream.write_internal_comment("set duration")
        self._stream.write_frame(1, "")

        self._stream.write_internal_comment("clear screen")
        self._stream.write_frame(0, _ansi_hide_cursor())
        self._stream.write_frame(0, _ansi_set_window_scroll_height(self._stream.height))
        self._stream.write_frame(0, _ansi_cursor_to_home())
        self._stream.write_frame(0, _ansi_clear_screen())

        self._stream.write_internal_comment("draw screen")
        for index in range(0, self._data_line_max_row):
            self._stream.write_frame(0, self._data_lines[index] + newline())

        self._stream.write_internal_comment("set and show cursor")
        self._stream.write_frame(0, _ansi_cursor_to_home())
        self._stream.write_frame(0, _ansi_show_cursor())

    def cursor_down(self, num_lines):
        self._stream.write_section_comment("cursor_down(num_lines={})".format(num_lines))
        max_allowed_lines = self._viewport_cursor_max_row - self._viewport_cursor_row
        lines_with_cursor_only_move = min(max_allowed_lines, num_lines)
        self._stream.write_internal_comment(
            "lines_with_cursor_only_move={}".format(lines_with_cursor_only_move))
        content_beyond_current_scroll = max(num_lines - max_allowed_lines, 0)
        self._stream.write_internal_comment(
            "content_beyond_current_scroll={}".format(content_beyond_current_scroll))
        data_lines_not_yet_shown = len(self._data_lines) - self._data_line_max_row
        self._stream.write_internal_comment(
            "data_lines_not_yet_shown={}".format(data_lines_not_yet_shown))
        lines_with_content_regen_scroll = min(content_beyond_current_scroll, data_lines_not_yet_shown)
        self._stream.write_internal_comment(
            "lines_with_content_regen_scroll={}".format(lines_with_content_regen_scroll))

        self._stream.write_internal_comment("set duration")
        self._stream.write_frame(1, "")

        if lines_with_cursor_only_move:
            self._stream.write_frame(0, _ansi_cursor_down(lines_with_cursor_only_move))
            self._viewport_cursor_row += lines_with_cursor_only_move

        if lines_with_content_regen_scroll:
            self._stream.write_internal_comment("push content up")
            self._stream.write_frame(0, _ansi_hide_cursor())
            self._stream.write_frame(0, _ansi_set_window_scroll_height(self._viewport_height))
            self._stream.write_frame(0, _ansi_cursor_to_row(self._viewport_height))
            for _ in range(0, lines_with_content_regen_scroll):
                self._stream.write_frame(0, newline())

            self._stream.write_internal_comment("add new lines")
            for index in range(0, lines_with_content_regen_scroll):
                self._stream.write_frame(0, _ansi_cursor_to_row(self._viewport_height - lines_with_content_regen_scroll + 1 + index))
                self._stream.write_frame(0, self._data_lines[self._data_line_max_row + index])
            self._data_line_max_row += lines_with_content_regen_scroll

            self._stream.write_internal_comment("reset original viewport + footer")
            self._stream.write_frame(0, _ansi_set_window_scroll_height(self._stream.height))

            self._stream.write_internal_comment("show cursor at the end")
            self._stream.write_frame(0, _ansi_cursor_to_row(self._viewport_height))
            self._stream.write_frame(0, _ansi_show_cursor())



    def cursor_up(self, num_lines):
        pass


# ~~~~~~~~~~~

def _ansi_set_window_scroll_height(num_lines: int):
    return "\u001b[1;{}r".format(num_lines)


def _ansi_clear_screen():
    return "\u001b[2J"


def _ansi_hide_cursor():
    return "\u001b[?25l"


def _ansi_show_cursor():
    return "\u001b[?25h"


def _ansi_cursor_to_home():
    return "\u001b[H"


def _ansi_cursor_to_row(num_row):
    return "\u001b[{};1H".format(num_row)


def _ansi_cursor_down(num_lines: int):
    return "\u001b[{}B".format(num_lines)
