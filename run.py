#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import os

from asciicast import wait, appear, press_enter, type_chars, Text, AsciicastV2

asciicast = AsciicastV2(width=60, height=21)
asciicast.add_all_lines([
    wait(ticks=10),
    appear(Text.console_arrow()),
    type_chars("hostname"),
    press_enter(),
    appear("candidate-laptop.local" + Text.newline())
])

if not os.path.exists('build'):
    os.makedirs('build')

with open('build/data.cast', 'w') as f:
    string_stream = io.StringIO("some initial text data")
    asciicast.write_to_stream(string_stream)
    f.write(string_stream.getvalue())
