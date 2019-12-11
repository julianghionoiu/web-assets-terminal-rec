import io

from approvaltests.approvals import verify

from asciicast.shell import Shell
from asciicast.stream import AsciicastStream
from asciicast.text import newline, red, dim, bright, green
from asciicast.vim import VimEditor


def test_appear_and_type():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    shell = Shell(asciicast_stream)

    asciicast_stream.wait(ticks=10)
    shell.appear("> ")
    shell.type_chars("hostname")
    shell.press_enter()
    shell.appear("candidate-laptop.local" + newline())

    verify(string_stream.getvalue())


def test_delete():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    shell = Shell(asciicast_stream)

    shell.appear("> ")
    shell.appear("foocar")
    shell.delete(3)
    shell.appear("bar")

    verify(string_stream.getvalue())


def test_colours():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    shell = Shell(asciicast_stream)

    shell.appear("1. " + red("some red text") + " " + green('some green text') + newline())
    shell.appear("2. " + dim(red('x')) + " " + bright(red('x')) + newline())

    verify(string_stream.getvalue())


def test_add_comments_to_stream():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    shell = Shell(asciicast_stream)

    asciicast_stream.wait(ticks=5)
    asciicast_stream.write_section_comment("This is a comment")
    shell.appear("candidate-laptop.local" + newline())

    verify(string_stream.getvalue())


def test_vim_cursor_move_down_then_up():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, _generate_lines(25))

    vim.display_content()
    vim.cursor_down(num_lines=5)
    vim.cursor_down(num_lines=30)
    vim.cursor_up(num_lines=5)
    vim.cursor_up(num_lines=30)

    verify(string_stream.getvalue())


def test_vim_cursor_move_right_then_left():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, "123456789\n")

    vim.display_content()
    vim.cursor_right(num_cols=2)
    vim.cursor_right(num_cols=10)
    vim.cursor_left(num_cols=2)
    vim.cursor_left(num_cols=10)

    verify(string_stream.getvalue())


def test_vim_content_scroll_down_then_up():
    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    vim = VimEditor(asciicast_stream, _generate_lines(25))

    vim.display_content()
    vim.cursor_down(num_lines=2)
    vim.content_scroll_down(num_lines=2)
    vim.content_scroll_down(num_lines=20)
    vim.content_scroll_up(num_lines=2)
    vim.content_scroll_up(num_lines=20)

    verify(string_stream.getvalue())


# ~~~~~~ Test helper

def _generate_lines(num_lines):
    block_of_text: str = ""
    index: int
    for index in range(0, num_lines):
        block_of_text += "line{}\n".format(index)
    return block_of_text
