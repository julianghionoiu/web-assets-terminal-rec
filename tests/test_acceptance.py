import io

from approvaltests.approvals import verify

from asciicast.v2 import AsciicastV2
from asciicast.actions import Wait, Appear, PressEnter, TypeChars, Delete
from asciicast.text import newline, red, dim, bright, green


def test_appear_and_type():
    _render_and_verify_cast([
        Wait(ticks=10),
        Appear("> "),
        TypeChars("hostname"),
        PressEnter(),
        Appear("candidate-laptop.local" + newline()),
    ])


def test_delete():
    _render_and_verify_cast([
        Appear("> "),
        Appear("foocar"),
        Delete(3),
        Appear("bar"),
    ])


def test_colours():
    _render_and_verify_cast([
        Appear("1. " + red("some red text") + " " + green('some green text') + newline()),
        Appear("2. " + dim(red('x')) + " " + bright(red('x')) + newline()),
    ])


# ~~~~~~ Test helper

def _render_and_verify_cast(list_of_actions):
    asciicast = AsciicastV2(width=60, height=21)
    asciicast.add_actions(list_of_actions)
    asciicast_v2_file = io.StringIO()
    asciicast.write_to_stream(asciicast_v2_file)
    verify(asciicast_v2_file.getvalue())
