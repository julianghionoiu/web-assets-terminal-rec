#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import os

from asciicast import wait, appear, press_enter, typing, Text, write_asciicast_v2

metadata = {"version": 2, "width": 60, "height": 21}

asciicast_lines = []
asciicast_lines += wait(ticks=10)
asciicast_lines += appear(Text.CONSOLE_ARROW)
asciicast_lines += typing("hostname")
asciicast_lines += press_enter()
asciicast_lines += appear("candidate-laptop.local" + Text.NEWLINE)


if not os.path.exists('build'):
    os.makedirs('build')

with open('build/data.cast', 'w') as f:
    string_stream = io.StringIO("some initial text data")
    write_asciicast_v2(string_stream, metadata, asciicast_lines)
    f.write(string_stream.getvalue())
