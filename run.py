#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import os

from asciicast.shell import Shell
from asciicast.vim import VimEditor
from asciicast.stream import AsciicastStream

if not os.path.exists('build'):
    os.makedirs('build')


with open('build/input.txt', 'r') as file:
    file_contents = file.read()


with open('build/data.cast', 'w') as f:
    string_stream = io.StringIO("some initial text data")

    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream,
                                       length_of_one_tick_in_seconds=0.1)
    shell = Shell(asciicast_stream)
    # vim = VimEditor(asciicast_stream, file_contents)
    vim = VimEditor(asciicast_stream, "\u001b[31mred????\u001b[0m word2\n")

    vim.display_content()
    vim.cursor_right(num_cols=3)
    vim.delete_at_cursor(num_chars=20)
    vim.type_at_cursor("word\n")

    asciicast_stream.wait(ticks=10)

    f.write(string_stream.getvalue())

