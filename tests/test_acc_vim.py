import io

from approvaltests.approvals import verify

from asciicast.shell import Shell
from asciicast.stream import AsciicastStream
from asciicast.text import newline, red, dim, bright, green
from asciicast.vim import VimEditor


def test_cursor_move_down_then_up():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, _generate_lines(25))

    vim.display_content()
    vim.cursor_down(num_rows=5)
    vim.cursor_down(num_rows=30)
    vim.cursor_up(num_rows=5)
    vim.cursor_up(num_rows=30)

    verify(string_stream.getvalue())


def test_cursor_move_right_then_left():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, "123456789\n")

    vim.display_content()
    vim.cursor_right(num_cols=2)
    vim.cursor_right(num_cols=10)
    vim.cursor_left(num_cols=2)
    vim.cursor_left(num_cols=10)

    verify(string_stream.getvalue())


def test_cursor_move_right_then_down():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, "123456789\n123\n")

    vim.display_content()
    vim.cursor_right(num_cols=10)
    vim.cursor_down(num_rows=1)

    verify(string_stream.getvalue())


def test_content_scroll_down_then_up():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, _generate_lines(25))

    vim.display_content()
    vim.cursor_down(num_rows=2)
    vim.content_scroll_down(num_rows=2)
    vim.content_scroll_down(num_rows=20)
    vim.content_scroll_up(num_rows=2)
    vim.content_scroll_up(num_rows=20)

    verify(string_stream.getvalue())


# ~~~~~~ Test helper

def _generate_lines(num_lines):
    block_of_text: str = ""
    index: int
    for index in range(0, num_lines):
        block_of_text += "line{}\n".format(index)
    return block_of_text
