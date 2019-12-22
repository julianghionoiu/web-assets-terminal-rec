import re

from asciicast.stream import AsciicastStream
from asciicast.text import newline


class VimEditor(object):
    _stream: AsciicastStream
    _data_lines: list

    def __init__(self, asciicast_stream: AsciicastStream, block_of_text: str) -> None:
        self._stream = asciicast_stream
        self._data_lines = block_of_text.split("\n")
        self._viewport_height = min(asciicast_stream.height - 2, len(self._data_lines))
        self._data_line_row = 0
        self._cursor_row = 0
        self._cursor_col = 0

    def display_content(self):
        self._stream.write_section_comment("display_content()")
        self._stream.wait(5)
        self._stream.write_internal_comment("save screen status - will be used on exit")
        self._stream.write_frame(_ansi_save_screen())
        self._render_data_lines(self._data_line_row)

    def cursor_down(self, num_rows):
        self._stream.write_section_comment("cursor_down(num_lines={})".format(num_rows))
        max_cursor_down = self._viewport_height - self._cursor_row - 1
        self._stream.write_internal_comment("max_cursor_down={}".format(max_cursor_down))
        actual_cursor_down = min(max_cursor_down, num_rows)
        self._stream.write_internal_comment("actual_cursor_down={}".format(actual_cursor_down))

        new_cursor_row = self._cursor_row + actual_cursor_down
        new_cursor_col = min(self._cursor_col, self._len_of_visible_line(self._cursor_row + actual_cursor_down) - 1)
        self._stream.wait(5)
        self._render_new_cursor_location(new_cursor_row, new_cursor_col)

    def cursor_up(self, num_rows):
        self._stream.write_section_comment("cursor_up(num_lines={})".format(num_rows))
        max_cursor_up = self._cursor_row
        self._stream.write_internal_comment("max_cursor_up={}".format(max_cursor_up))
        actual_cursor_up = min(max_cursor_up, num_rows)
        self._stream.write_internal_comment("actual_cursor_up={}".format(actual_cursor_up))

        new_cursor_row = self._cursor_row - actual_cursor_up
        new_cursor_col = min(self._cursor_col, self._len_of_visible_line(new_cursor_row) - 1)
        self._stream.wait(5)
        self._render_new_cursor_location(new_cursor_row, new_cursor_col)

    def cursor_right(self, num_cols):
        self._stream.write_section_comment("cursor_right(num_cols={})".format(num_cols))
        max_cursor_right = self._len_of_visible_line(self._cursor_row) - self._cursor_col - 1
        self._stream.write_internal_comment("max_cursor_right={}".format(max_cursor_right))
        actual_cursor_right = min(max_cursor_right, num_cols)
        self._stream.write_internal_comment("actual_cursor_right={}".format(actual_cursor_right))

        new_cursor_row = self._cursor_row
        new_cursor_col = self._cursor_col + actual_cursor_right
        self._stream.wait(5)
        self._render_new_cursor_location(new_cursor_row, new_cursor_col)

    def cursor_left(self, num_cols):
        self._stream.write_section_comment("cursor_left(num_cols={})".format(num_cols))
        max_cursor_left = self._cursor_col
        self._stream.write_internal_comment("max_cursor_left={}".format(max_cursor_left))
        actual_cursor_left = min(max_cursor_left, num_cols)
        self._stream.write_internal_comment("actual_cursor_left={}".format(actual_cursor_left))

        new_cursor_row = self._cursor_row
        new_cursor_col = self._cursor_col - actual_cursor_left
        self._stream.wait(5)
        self._render_new_cursor_location(new_cursor_row, new_cursor_col)

    def content_scroll_down(self, num_rows):
        self._stream.write_section_comment("content_scroll_down(num_lines={})".format(num_rows))
        max_scroll_down = len(self._data_lines) - self._viewport_height - self._data_line_row
        self._stream.write_internal_comment("max_scroll_down={}".format(max_scroll_down))
        actual_scroll_down = min(max_scroll_down, num_rows)
        self._stream.write_internal_comment("actual_scroll_down={}".format(actual_scroll_down))
        self._stream.wait(5)
        self._render_data_lines(self._data_line_row + actual_scroll_down)
        self._data_line_row += actual_scroll_down

        # Update cursor
        new_cursor_row = self._cursor_row
        new_cursor_col = min(self._cursor_col, self._len_of_visible_line(self._cursor_row) - 1)
        self._render_new_cursor_location(new_cursor_row, new_cursor_col)

    def content_scroll_up(self, num_rows):
        self._stream.write_section_comment("content_scroll_up(num_lines={})".format(num_rows))
        max_scroll_up = self._data_line_row
        self._stream.write_internal_comment("max_scroll_up={}".format(max_scroll_up))
        actual_scroll_up = min(max_scroll_up, num_rows)
        self._stream.write_internal_comment("actual_scroll_up={}".format(actual_scroll_up))
        self._stream.wait(5)
        self._render_data_lines(self._data_line_row - actual_scroll_up)
        self._data_line_row -= actual_scroll_up

        # Update cursor
        new_cursor_row = self._cursor_row
        new_cursor_col = min(self._cursor_col, self._len_of_visible_line(self._cursor_row) - 1)
        self._render_new_cursor_location(new_cursor_row, new_cursor_col)

    def appear_in_footer(self, text):
        self._stream.write_section_comment("appear_in_footer(text={})".format(text))
        self._stream.wait(5)
        self._stream.write_frame(_ansi_hide_cursor())
        self._stream.write_frame(_ansi_set_cursor_position(self._viewport_height, 0))
        self._stream.write_frame(_ansi_clear_line())
        self._stream.write_frame(text)
        self._stream.write_frame(_ansi_set_cursor_position(self._cursor_row, self._cursor_col))
        self._stream.write_frame(_ansi_show_cursor())

    def type_in_footer(self, text):
        self._stream.write_section_comment("type_in_footer(text={})".format(text))
        self._stream.wait(5)
        self._stream.write_frame(_ansi_hide_cursor())
        self._stream.write_frame(_ansi_set_cursor_position(self._viewport_height, 0))
        self._stream.write_frame(_ansi_clear_line())
        self._stream.write_frame(_ansi_show_cursor())
        self._stream.write_section_comment("type_chars(text={})".format(text))
        for _char in text:
            self._stream.write_frame(content=_char, ticks_after=1)

    def delete_at_cursor(self, num_chars):
        self._stream.write_section_comment("delete_at_cursor(num_chars={})".format(num_chars))
        self._stream.wait(5)
        chars_in_row = self._len_of_visible_line(self._cursor_row)
        max_chars_to_delete = min(chars_in_row - self._cursor_col, num_chars)
        for _ in range(0, max_chars_to_delete):
            self._delete_char_at_cursor(self._cursor_row, self._cursor_col)
        self._render_individual_data_line(self._data_line_row + self._cursor_row)

    def type_at_cursor(self, text):
        self._stream.write_section_comment("type_at_cursor(text={})".format(text))
        self._stream.wait(5)
        for _char in text:
            self._insert_char_at_cursor(self._cursor_row, self._cursor_col, _char)
            self._render_individual_data_line(self._data_line_row + self._cursor_row)
            self._cursor_col += 1
            self._stream.wait(1)

    def close(self):
        self._stream.write_section_comment("close()")
        self._stream.wait(5)
        self._stream.write_internal_comment("restore screen status")
        self._stream.write_frame(_ansi_restore_screen())

    # ~~~~ reusable render methods ~~~~

    ANSI_ESCAPE_PATTERN_ALL = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')

    def _delete_char_at_cursor(self, cursor_row, cursor_col):
        data_line = self._data_lines[self._data_line_row + cursor_row]
        data_index = self._translate_cursor_col_to_data_index(data_line, cursor_col)
        new_data_line = data_line[:data_index] + data_line[data_index + 1:]
        self._data_lines[self._data_line_row + cursor_row] = new_data_line

    def _insert_char_at_cursor(self, cursor_row, cursor_col, the_char):
        data_line = self._data_lines[self._data_line_row + cursor_row]
        data_index = self._translate_cursor_col_to_data_index(data_line, cursor_col)
        new_data_line = data_line[:data_index] + the_char + data_line[data_index:]
        self._data_lines[self._data_line_row + cursor_row] = new_data_line

    def _translate_cursor_col_to_data_index(self, data_line, cursor_col):
        sanitised_line = self.ANSI_ESCAPE_PATTERN_ALL.sub(lambda match: "_" * len(match.group()), data_line)
        alpha_chars = 0
        corresponding_index = len(data_line)
        for i in range(0, len(sanitised_line)):
            if sanitised_line[i] != "_":
                alpha_chars += 1
            if alpha_chars == cursor_col + 1:
                corresponding_index = i
                break
        return corresponding_index

    def _len_of_visible_line(self, cursor_row):
        data_line = self._data_lines[self._data_line_row + cursor_row]
        visible_chars = self.ANSI_ESCAPE_PATTERN_ALL.sub("", data_line)
        return len(visible_chars)

    def _print_cursor_position(self):
        self._stream.write_internal_comment("cursor_position=(row:{},col:{}), data_line_row={}".format(
            self._cursor_row, self._cursor_col, self._data_line_row))

    def _render_new_cursor_location(self, cursor_row, cursor_col):
        self._stream.write_frame(_ansi_set_cursor_position(cursor_row, cursor_col))
        self._cursor_row = cursor_row
        self._cursor_col = cursor_col
        self._print_cursor_position()

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

    def _render_individual_data_line(self, data_row: int):
        self._stream.write_internal_comment("clear line and hide cursor")
        self._stream.write_frame(_ansi_hide_cursor())
        self._stream.write_frame(_ansi_set_cursor_position(self._cursor_row, 0))
        self._stream.write_frame(_ansi_clear_line())
        self._stream.write_internal_comment("draw line")
        self._stream.write_frame(self._data_lines[data_row])
        self._stream.write_internal_comment("restore and show cursor")
        self._stream.write_frame(_ansi_set_cursor_position(self._cursor_row, self._cursor_col))
        self._stream.write_frame(_ansi_show_cursor())


# ~~~~~~~~~~~

def _ansi_set_window_scroll_height(num_lines: int):
    return "\u001b[1;{}r".format(num_lines)


def _ansi_save_screen():
    return "\u001b[?1049h"


def _ansi_restore_screen():
    return "\u001b[?1049l"


def _ansi_clear_screen():
    return "\u001b[2J"


def _ansi_clear_line():
    return "\u001b[2K"


def _ansi_hide_cursor():
    return "\u001b[?25l"


def _ansi_show_cursor():
    return "\u001b[?25h"


def _ansi_set_cursor_position(num_row, num_col):
    return "\u001b[{};{}H".format(num_row + 1, num_col + 1)
