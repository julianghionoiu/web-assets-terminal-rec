import io

from approvaltests.approvals import verify

from asciicast import appear, Text, delete, AsciicastV2
from asciicast import wait, type_chars, press_enter


def test_appear_and_type():
    _render_and_verify_cast([
        wait(ticks=10),
        appear("> "),
        type_chars("hostname"),
        press_enter(),
        appear("candidate-laptop.local" + Text.newline()),
    ])


def test_delete():
    _render_and_verify_cast([
        appear("> "),
        appear("foocar"),
        delete(3),
        appear("bar"),
    ])


def test_colours():
    _render_and_verify_cast([
        appear("1. " + Text.red("some red text") + " " + Text.green('some green text') + Text.newline()),
        appear("2. " + Text.dim(Text.red('x')) + " " + Text.bright(Text.red('x')) + Text.newline()),
    ])


# ~~~~~~ Test helper

def _render_and_verify_cast(list_of_actions):
    asciicast = AsciicastV2(width=60, height=21)
    asciicast.add_all_lines(list_of_actions)
    asciicast_v2_file = io.StringIO()
    asciicast.write_to_stream(asciicast_v2_file)
    verify(asciicast_v2_file.getvalue())
