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
                                       length_of_one_tick_in_seconds=1)
    shell = Shell(asciicast_stream)
    vim = VimEditor(asciicast_stream)

    vim.display_content(file_contents)
    vim.cursor_down(num_lines=5)
    vim.cursor_down(num_lines=14)
    vim.cursor_down(num_lines=1)
    vim.cursor_down(num_lines=4)
    vim.cursor_up(num_lines=5)
    vim.cursor_up(num_lines=20)

    shell.wait(2)

    f.write(string_stream.getvalue())

