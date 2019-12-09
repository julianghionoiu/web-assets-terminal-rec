import io

from approvaltests.approvals import verify

from asciicast.shell import Shell
from asciicast.stream import AsciicastStream
from asciicast.text import newline, red, dim, bright, green


def test_appear_and_type():
    string_stream = io.StringIO()
    shell = Shell(AsciicastStream(width=60, height=21, stream=string_stream))

    shell.wait(ticks=10)
    shell.appear("> ")
    shell.type_chars("hostname")
    shell.press_enter()
    shell.appear("candidate-laptop.local" + newline())

    verify(string_stream.getvalue())


def test_delete():
    string_stream = io.StringIO()
    shell = Shell(AsciicastStream(width=60, height=21, stream=string_stream))

    shell.appear("> ")
    shell.appear("foocar")
    shell.delete(3)
    shell.appear("bar")

    verify(string_stream.getvalue())


def test_colours():
    string_stream = io.StringIO()
    shell = Shell(AsciicastStream(width=60, height=21, stream=string_stream))

    shell.appear("1. " + red("some red text") + " " + green('some green text') + newline())
    shell.appear("2. " + dim(red('x')) + " " + bright(red('x')) + newline())

    verify(string_stream.getvalue())


def test_add_comments_to_stream():
    string_stream = io.StringIO()
    aciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    shell = Shell(aciicast_stream)

    shell.wait(ticks=5)
    aciicast_stream.write_comment("This is a comment")
    shell.appear("candidate-laptop.local" + newline())

    verify(string_stream.getvalue())


# def test_vim_scroll_file_up_and_down():
#     string_stream = io.StringIO()
#     aciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
#     vim = VimEditor(aciicast_stream)
#
#     vim.display_content(_generate_lines(25))
#     vim.cursor_down(lines=5)
#     vim.cursor_down(lines=10)
#     vim.cursor_down(lines=10)
#     vim.cursor_up(lines=5)
#     vim.cursor_up(lines=20)
#
#     verify(string_stream.getvalue())


# ~~~~~~ Test helper

def _generate_lines(num_lines):
    block_of_text: str = ""
    index: int
    for index in range(0, num_lines):
        block_of_text += "line{}\n".format(index)
    return block_of_text
