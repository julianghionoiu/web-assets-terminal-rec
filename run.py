#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from asciicast.shell import Shell
from asciicast.stream import AsciicastStream
from asciicast.text import newline, bright, cyan, console_arrow

if not os.path.exists('build'):
    os.makedirs('build')


def with_cast(f):
    return AsciicastStream(width=60, height=21, stream=f,
                           length_of_one_tick_in_seconds=0.1)


def section_01_hostname(input_stream):
    asciicast_stream = with_cast(input_stream)
    shell = Shell(asciicast_stream)

    shell.appear(bright(cyan("# Use own laptop and tools")) + newline())
    asciicast_stream.wait(4)
    shell.appear(console_arrow())
    shell.type_chars("hostname")
    shell.press_enter()
    shell.appear("candidate-laptop.local" + newline())
    shell.appear(newline())


def section_02_clone_project(input_stream):
    asciicast_stream = with_cast(input_stream)
    shell = Shell(asciicast_stream)

    shell.appear(bright(cyan("# Clone a starting project - pick language")) + newline())
    asciicast_stream.wait(4)
    shell.appear(console_arrow())
    shell.type_chars("wget https://get")
    shell.appear(".accelerate.io/")
    asciicast_stream.wait(10)
    shell.type_chars("java")
    asciicast_stream.wait(10)
    shell.delete(4)
    shell.type_chars("python")
    asciicast_stream.wait(10)
    shell.type_chars(" | unzip")
    shell.press_enter()
    shell.appear("Resolving get.accelerate.io (get.accelerate.io)...")
    shell.appear("99.86.88.23" + newline())
    shell.appear("Connecting to get.accelerate.io ...")
    shell.appear("connected" + newline())
    shell.appear("HTTP request sent, awaiting response...")
    shell.appear("200 OK" + newline())
    shell.appear("Saving to: ‘runner.zip.’" + newline())
    shell.appear("Unzipping" + newline())
    shell.appear("Done" + newline())
    shell.appear(console_arrow())
    shell.press_enter()
    shell.appear(console_arrow())


# ~~~~~~~~~~ Putting it together ~~~~~~~~~~``

with open('build/01_hostname.cast', 'w') as f:
    section_01_hostname(f)

with open('build/02_clone_project.cast', 'w') as f:
    section_02_clone_project(f)

with open('build/e2e.cast', 'w') as f:
    main_stream = AsciicastStream(width=60, height=21, stream=f,
                                  length_of_one_tick_in_seconds=0.1)

    main_stream.write_from_input_stream(open('build/01_hostname.cast', 'r'))
    main_stream.write_from_input_stream(open('build/02_clone_project.cast', 'r'))
    main_stream.wait(ticks=50)
