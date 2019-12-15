import io

from approvaltests.approvals import verify

from asciicast.stream import AsciicastStream
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


def test_cursor_move_right_with_colours():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, "\u001b[31mredtext\u001b[0m\n")

    vim.display_content()
    vim.cursor_right(num_cols=2)
    vim.cursor_right(num_cols=10)

    verify(string_stream.getvalue())


def test_cursor_adjust_location_to_content():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, "123456789\n12345\n12")

    vim.display_content()
    vim.cursor_right(num_cols=10)
    vim.cursor_down(num_rows=1)
    vim.content_scroll_down(1)

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


def test_footer_appear_and_type():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, "some_text\n")

    vim.display_content()
    vim.appear_in_footer("-- INSERT --")
    vim.type_in_footer(":wq")

    verify(string_stream.getvalue())


def test_content_delete_and_insert():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, "\u001b[31mred????\u001b[0m word2\n")

    vim.display_content()
    vim.cursor_right(num_cols=3)
    vim.delete_at_cursor(num_chars=20)
    vim.type_at_cursor("word\n")

    verify(string_stream.getvalue())


def test_quitting():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, "some content\n")

    vim.display_content()
    vim.close()

    verify(string_stream.getvalue())


# ~~~~~~ Test helper

def _generate_lines(num_lines):
    block_of_text: str = ""
    index: int
    for index in range(0, num_lines):
        block_of_text += "line{}\n".format(index)
    return block_of_text
