from asciicast.stream import AsciicastStream
from asciicast.text import newline


class VimEditor(object):
    _stream: AsciicastStream
    _data_lines: list

    def __init__(self, asciicast_stream: AsciicastStream, block_of_text: str) -> None:
        self._stream = asciicast_stream
        self._data_lines = block_of_text.split()
        self._viewport_height = asciicast_stream.height - 1
        self._data_line_row = 0
        self._cursor_row = 0

    def display_content(self):
        self._stream.write_section_comment("display_content()")
        self._stream.wait(5)
        self._render_data_lines(self._data_line_row, self._viewport_height, self._cursor_row)

    def cursor_down(self, num_lines):
        self._stream.write_section_comment("cursor_down(num_lines={})".format(num_lines))
        max_cursor_down = self._viewport_height - self._cursor_row - 1
        self._stream.write_internal_comment("max_cursor_down={}".format(max_cursor_down))
        actual_cursor_down = min(max_cursor_down, num_lines)
        self._stream.write_internal_comment("actual_cursor_down={}".format(actual_cursor_down))
        self._stream.wait(5)
        self._stream.write_frame(_ansi_cursor_down(actual_cursor_down))
        self._cursor_row += actual_cursor_down
        self._stream.write_internal_comment("self._cursor_row={}".format(self._cursor_row))

    def cursor_up(self, num_lines):
        self._stream.write_section_comment("cursor_up(num_lines={})".format(num_lines))
        max_cursor_up = self._cursor_row
        self._stream.write_internal_comment("max_cursor_up={}".format(max_cursor_up))
        actual_cursor_up = min(max_cursor_up, num_lines)
        self._stream.write_internal_comment("actual_cursor_up={}".format(actual_cursor_up))
        self._stream.wait(5)
        self._stream.write_frame(_ansi_cursor_up(actual_cursor_up))
        self._cursor_row -= actual_cursor_up
        self._stream.write_internal_comment("self._cursor_row={}".format(self._cursor_row))

    def content_scroll_down(self, num_lines):
        self._stream.write_section_comment("content_scroll_down(num_lines={})".format(num_lines))
        max_scroll_down = len(self._data_lines) - self._viewport_height - self._data_line_row
        self._stream.write_internal_comment("max_scroll_down={}".format(max_scroll_down))
        actual_scroll_down = min(max_scroll_down, num_lines)
        self._stream.write_internal_comment("actual_scroll_down={}".format(actual_scroll_down))
        self._stream.wait(5)
        self._render_data_lines(self._data_line_row + actual_scroll_down, self._viewport_height, self._cursor_row)
        self._data_line_row += actual_scroll_down

    def content_scroll_up(self, num_lines):
        self._stream.write_section_comment("content_scroll_up(num_lines={})".format(num_lines))
        max_scroll_up = self._data_line_row
        self._stream.write_internal_comment("max_scroll_up={}".format(max_scroll_up))
        actual_scroll_up = min(max_scroll_up, num_lines)
        self._stream.write_internal_comment("actual_scroll_up={}".format(actual_scroll_up))
        self._stream.wait(5)
        self._render_data_lines(self._data_line_row - actual_scroll_up, self._viewport_height, self._cursor_row)
        self._data_line_row -= actual_scroll_up

    # ~~~~ reusable render methods ~~~~

    def _render_data_lines(self, start_row: int, num_rows: int, cursor_row: int):
        self._stream.write_internal_comment("clear screen and hide cursor")
        self._stream.write_frame(_ansi_hide_cursor())
        self._stream.write_frame(_ansi_set_window_scroll_height(self._stream.height))
        self._stream.write_frame(_ansi_clear_screen())
        self._stream.write_internal_comment("draw screen")
        for index in range(start_row, start_row + num_rows):
            self._stream.write_frame(self._data_lines[index] + newline())
        self._stream.write_internal_comment("restore and show cursor")
        self._stream.write_frame(_ansi_cursor_to_row(cursor_row))
        self._stream.write_frame(_ansi_show_cursor())


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


def _ansi_save_cursor_position():
    return "\u001b[s"


def _ansi_restore_cursor_position():
    return "\u001b[r"


def _ansi_cursor_to_row(num_row):
    return "\u001b[{};1H".format(num_row + 1)


def _ansi_cursor_down(num_lines: int):
    return "\u001b[{}B".format(num_lines)


def _ansi_cursor_up(num_lines: int):
    return "\u001b[{}A".format(num_lines)
