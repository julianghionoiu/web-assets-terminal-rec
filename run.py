#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import os

from asciicast.actions import Wait, Appear, TypeChars, PressEnter
from asciicast.text import console_arrow, newline
from asciicast.v2 import AsciicastV2

asciicast = AsciicastV2(width=60, height=21)
asciicast.add_actions([
    Wait(ticks=10),
    Appear(console_arrow()),
    TypeChars("hostname"),
    PressEnter(),
    Appear("candidate-laptop.local" + newline())
])

if not os.path.exists('build'):
    os.makedirs('build')

with open('build/data.cast', 'w') as f:
    string_stream = io.StringIO("some initial text data")
    asciicast.write_to_stream(string_stream)
    f.write(string_stream.getvalue())
