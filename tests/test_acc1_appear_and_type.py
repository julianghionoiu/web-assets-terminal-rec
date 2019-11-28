import io

from approvaltests.approvals import verify

from asciicast import wait, appear, typing, Text, press_enter, write_asciicast_v2


def test_answer():
    metadata = {"version": 2, "width": 60, "height": 21}

    asciicast_lines = []
    asciicast_lines += wait(ticks=10)
    asciicast_lines += appear(Text.CONSOLE_ARROW)
    asciicast_lines += typing("hostname")
    asciicast_lines += press_enter()
    asciicast_lines += appear("candidate-laptop.local" + Text.NEWLINE)

    asciicast_v2_file = io.StringIO("some initial text data")
    write_asciicast_v2(asciicast_v2_file, metadata, asciicast_lines)

    verify(asciicast_v2_file.getvalue())
