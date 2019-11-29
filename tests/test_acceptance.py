import io

from approvaltests.approvals import verify

from asciicast import appear, Text, write_asciicast_v2, red, green, bright, dim, delete
from asciicast import wait, typing, press_enter


def test_appear_and_type():
    metadata = {"version": 2, "width": 60, "height": 21}

    asciicast_lines = []
    asciicast_lines += wait(ticks=10)
    asciicast_lines += appear("> ")
    asciicast_lines += typing("hostname")
    asciicast_lines += press_enter()
    asciicast_lines += appear("candidate-laptop.local" + Text.NEWLINE)

    asciicast_v2_file = io.StringIO()
    write_asciicast_v2(asciicast_v2_file, metadata, asciicast_lines)

    verify(asciicast_v2_file.getvalue())


def test_delete():
    metadata = {"version": 2, "width": 60, "height": 21}

    asciicast_lines = []

    asciicast_lines += appear("> ")
    asciicast_lines += appear("foocar")
    asciicast_lines += delete(3)
    asciicast_lines += appear("bar")

    asciicast_v2_file = io.StringIO()
    write_asciicast_v2(asciicast_v2_file, metadata, asciicast_lines)

    verify(asciicast_v2_file.getvalue())


def test_colours():
    metadata = {"version": 2, "width": 60, "height": 21}

    asciicast_lines = []

    asciicast_lines += appear("1. " + red("some red text") + " " + green('some green text') + Text.NEWLINE)
    asciicast_lines += appear("2. " + dim(red('x')) + " " + bright(red('x')) + Text.NEWLINE)

    asciicast_v2_file = io.StringIO()
    write_asciicast_v2(asciicast_v2_file, metadata, asciicast_lines)

    verify(asciicast_v2_file.getvalue())
