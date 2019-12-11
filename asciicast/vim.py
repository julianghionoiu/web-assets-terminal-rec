from asciicast.stream import AsciicastStream
from asciicast.text import newline


class VimEditor(object):
    _stream: AsciicastStream
    _data_lines: list

    def __init__(self, asciicast_stream: AsciicastStream, block_of_text: str) -> None:
        self._stream = asciicast_stream
        self._data_lines = block_of_text.split("\n")
        self._viewport_height = min(asciicast_stream.height - 1, len(self._data_lines))
        self._data_line_row = 0
        self._cursor_row = 0
        self._cursor_col = 0

    def display_content(self):
        self._stream.write_section_comment("display_content()")
        self._stream.wait(5)
        self._render_data_lines(self._data_line_row)

    def cursor_down(self, num_rows):
        self._stream.write_section_comment("cursor_down(num_lines={})".format(num_rows))
        max_cursor_down = self._viewport_height - self._cursor_row - 1
        self._stream.write_internal_comment("max_cursor_down={}".format(max_cursor_down))
        actual_cursor_down = min(max_cursor_down, num_rows)
        self._stream.write_internal_comment("actual_cursor_down={}".format(actual_cursor_down))
        self._stream.wait(5)
        new_cursor_row = self._cursor_row + actual_cursor_down
        self._cursor_col = min(self._cursor_col, self._len_of_visible_line(new_cursor_row) - 1)
        self._stream.write_frame(_ansi_cursor_down(actual_cursor_down))
        self._cursor_row = new_cursor_row
        self._print_cursor_position()

    def cursor_up(self, num_rows):
        self._stream.write_section_comment("cursor_up(num_lines={})".format(num_rows))
        max_cursor_up = self._cursor_row
        self._stream.write_internal_comment("max_cursor_up={}".format(max_cursor_up))
        actual_cursor_up = min(max_cursor_up, num_rows)
        self._stream.write_internal_comment("actual_cursor_up={}".format(actual_cursor_up))
        self._stream.wait(5)
        new_cursor_row = self._cursor_row - actual_cursor_up
        self._cursor_col = min(self._cursor_col, self._len_of_visible_line(new_cursor_row) - 1)
        self._stream.write_frame(_ansi_cursor_up(actual_cursor_up))
        self._cursor_row = new_cursor_row
        self._print_cursor_position()

    def cursor_right(self, num_cols):
        self._stream.write_section_comment("cursor_right(num_cols={})".format(num_cols))
        max_cursor_right = self._len_of_visible_line(self._cursor_row) - self._cursor_col - 1
        self._stream.write_internal_comment("max_cursor_right={}".format(max_cursor_right))
        actual_cursor_right = min(max_cursor_right, num_cols)
        self._stream.write_internal_comment("actual_cursor_right={}".format(actual_cursor_right))
        self._stream.wait(5)
        self._stream.write_frame(_ansi_cursor_right(actual_cursor_right))
        self._cursor_col += actual_cursor_right
        self._print_cursor_position()

    def cursor_left(self, num_cols):
        self._stream.write_section_comment("cursor_left(num_cols={})".format(num_cols))
        max_cursor_left = self._cursor_col
        self._stream.write_internal_comment("max_cursor_left={}".format(max_cursor_left))
        actual_cursor_left = min(max_cursor_left, num_cols)
        self._stream.write_internal_comment("actual_cursor_left={}".format(actual_cursor_left))
        self._stream.wait(5)
        self._stream.write_frame(_ansi_cursor_left(actual_cursor_left))
        self._cursor_col -= actual_cursor_left
        self._print_cursor_position()

    def content_scroll_down(self, num_rows):
        self._stream.write_section_comment("content_scroll_down(num_lines={})".format(num_rows))
        max_scroll_down = len(self._data_lines) - self._viewport_height - self._data_line_row
        self._stream.write_internal_comment("max_scroll_down={}".format(max_scroll_down))
        actual_scroll_down = min(max_scroll_down, num_rows)
        self._stream.write_internal_comment("actual_scroll_down={}".format(actual_scroll_down))
        self._stream.wait(5)
        self._render_data_lines(self._data_line_row + actual_scroll_down)
        self._data_line_row += actual_scroll_down

    def content_scroll_up(self, num_rows):
        self._stream.write_section_comment("content_scroll_up(num_lines={})".format(num_rows))
        max_scroll_up = self._data_line_row
        self._stream.write_internal_comment("max_scroll_up={}".format(max_scroll_up))
        actual_scroll_up = min(max_scroll_up, num_rows)
        self._stream.write_internal_comment("actual_scroll_up={}".format(actual_scroll_up))
        self._stream.wait(5)
        self._render_data_lines(self._data_line_row - actual_scroll_up)
        self._data_line_row -= actual_scroll_up

    # ~~~~ reusable render methods ~~~~

    def _len_of_visible_line(self, new_cursor_row):
        return len(self._data_lines[self._data_line_row + new_cursor_row])

    def _print_cursor_position(self):
        self._stream.write_internal_comment("cursor_position=(row:{},col:{})".format(
            self._cursor_row, self._cursor_col))

    def _render_data_lines(self, start_row: int):
        self._stream.write_internal_comment("clear screen and hide cursor")
        self._stream.write_frame(_ansi_hide_cursor())
        self._stream.write_frame(_ansi_set_window_scroll_height(self._stream.height))
        self._stream.write_frame(_ansi_clear_screen())
        self._stream.write_internal_comment("draw screen")
        for index in range(start_row, start_row + self._viewport_height):
            self._stream.write_frame(self._data_lines[index] + newline())
        self._stream.write_internal_comment("restore and show cursor")
        self._stream.write_frame(_ansi_set_cursor_position(self._cursor_row, self._cursor_col))
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


def _ansi_set_cursor_position(num_row, num_col):
    return "\u001b[{};{}H".format(num_row + 1, num_col + 1)


def _ansi_cursor_up(num_lines: int):
    if num_lines > 0:
        return "\u001b[{}A".format(num_lines)
    return ""


def _ansi_cursor_down(num_lines: int):
    if num_lines > 0:
        return "\u001b[{}B".format(num_lines)
    return ""


def _ansi_cursor_right(num_cols: int):
    if num_cols > 0:
        return "\u001b[{}C".format(num_cols)
    return ""


def _ansi_cursor_left(num_cols: int):
    if num_cols > 0:
        return "\u001b[{}D".format(num_cols)
    return ""
