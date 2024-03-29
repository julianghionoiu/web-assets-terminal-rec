import io

from approvaltests.approvals import verify

from asciicast.shell import Shell
from asciicast.stream import AsciicastStream
from asciicast.text import newline, red, dim, bright, green


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
