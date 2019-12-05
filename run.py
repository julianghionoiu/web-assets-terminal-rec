#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import os

from asciicast.shell import Shell
from asciicast.text import console_arrow, newline
from asciicast.stream import AsciicastStream

if not os.path.exists('build'):
    os.makedirs('build')

with open('build/data.cast', 'w') as f:
    string_stream = io.StringIO("some initial text data")

    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)
    shell = Shell(asciicast_stream)
    shell.wait(ticks=10)
    shell.appear(console_arrow())
    shell.type_chars("hostname")
    shell.press_enter()
    shell.appear("candidate-laptop.local" + newline())

    f.write(string_stream.getvalue())
