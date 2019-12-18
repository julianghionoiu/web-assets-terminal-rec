#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from asciicast.shell import Shell
from asciicast.stream import AsciicastStream
from asciicast.text import newline, bright, cyan, green, blue, console_arrow, yellow, white, dim, magenta
from asciicast.vim import VimEditor

if not os.path.exists('build'):
    os.makedirs('build')


def section_01_hostname(asciicast_stream):
    shell = Shell(asciicast_stream)

    shell.appear(bright(cyan("# Use own laptop and tools")) + newline())
    shell.appear(console_arrow())
    asciicast_stream.wait(5)

    shell.type_chars("hostname")
    shell.press_enter()
    shell.appear("candidate-laptop.local" + newline())
    shell.appear(newline())


def section_02_clone_project(asciicast_stream):
    shell = Shell(asciicast_stream)

    shell.appear(bright(cyan("# Clone a starting project - pick language")) + newline())
    shell.appear(console_arrow())
    asciicast_stream.wait(5)

    shell.type_chars("wget https://get")
    shell.appear(".accelerate.io/")
    asciicast_stream.wait(10)
    shell.type_chars("java")
    asciicast_stream.wait(5)
    shell.delete(4)
    shell.type_chars("python")
    asciicast_stream.wait(5)
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
    shell.appear(newline())
    asciicast_stream.wait(10)


def section_03_standard_project_setup(asciicast_stream):
    shell = Shell(asciicast_stream)

    shell.appear(bright(cyan("# Standard project for the language of choice")) + newline())
    shell.appear(console_arrow())
    asciicast_stream.wait(5)

    shell.type_chars("ls -1")
    asciicast_stream.wait(4)
    shell.press_enter()
    shell.appear(
        "README.md" + newline() +
        bright(cyan("config")) + newline() +
        bright(cyan("lib")) + newline() +
        "requirements.txt" + newline() +
        bright(cyan("test")) + newline() +
        bright(cyan("venv")) + newline()
    )
    shell.appear(newline())
    asciicast_stream.wait(10)


def section_04_start_challenge(asciicast_stream):
    shell = Shell(asciicast_stream)

    shell.appear(bright(cyan("# Start challenge from CLI or IDE")) + newline())
    shell.appear(console_arrow())
    asciicast_stream.wait(5)

    shell.type_chars("py")
    shell.appear("thon")
    shell.type_chars(" lib/se")
    shell.appear("nd_command_to_server.py")
    shell.press_enter()

    shell.appear("Connecting to accelerate.io" + newline())
    shell.appear(newline())
    shell.appear("Your progress (1/2):" + newline())
    shell.appear(
        " " + green("✓") + " WARMUP (3 rounds) - " + green("completed in 5 min") + newline() +
        " " + bright(blue(">")) + " REALM  (5 rounds) - official" + newline() +
        "             ROUND 1 - not started" + newline() +
        "             ROUND 2 - not started" + newline() +
        "             ROUND 3 - not started" + newline() +
        "             ROUND 4 - not started" + newline() +
        "             ROUND 5 - not started" + newline()
    )
    shell.appear("-------------------" + newline())
    shell.appear(yellow("Type \"start\" to start challenge") + newline())
    shell.appear(">>> ")
    asciicast_stream.wait(10)
    shell.type_chars("start")
    shell.press_enter()

    shell.appear(newline())
    shell.appear(green("CHALLENGE STARTED") + newline())
    shell.appear("Round 1 description saved to: challenge/round1.txt")
    shell.appear(newline())
    shell.appear(newline())
    shell.appear(console_arrow())
    asciicast_stream.wait(7)


def section_05_real_world_challenge(asciicast_stream):
    shell = Shell(asciicast_stream)

    shell.appear(bright(cyan("# Solve a real-world, scenario based challenge")) + newline())
    shell.appear(console_arrow())
    asciicast_stream.wait(5)

    shell.type_chars("cat ")
    shell.type_chars("c")
    shell.appear("hallenge/")
    shell.type_chars("r")
    shell.appear("ound1.txt")
    asciicast_stream.wait(4)
    shell.press_enter()

    shell.appear(
        bright(white("Round 1 - Welcome to REALM")) + newline() +
        newline() +
        "Welcome to the REALM startup - Realtime Elastic Assets Location Map." + newline() +
        "Together we are going to revolutionise the way people think about maps." + newline() +
        "See details below." + newline() +
        newline() +
        dim(white("<21 more lines>")) + newline()
    )
    asciicast_stream.wait(15)


def section_06_structure_code_your_way(asciicast_stream):
    shell = Shell(asciicast_stream)

    shell.appear(bright(cyan("# Structure the code your way")) + newline())
    shell.appear(console_arrow())
    asciicast_stream.wait(5)

    shell.type_chars("> lib")
    shell.appear("/realm/")
    shell.type_chars("main.py")
    shell.press_enter()

    shell.appear(console_arrow())
    shell.type_chars("> lib")
    shell.appear("/realm/")
    shell.type_chars("a_class.py")
    shell.press_enter()

    shell.appear(console_arrow())
    shell.type_chars("ls -1")
    asciicast_stream.wait(4)
    shell.press_enter()
    shell.appear(
        green("main.py") + newline() +
        "a_class.py" + newline()
    )
    shell.appear(newline())
    asciicast_stream.wait(10)


def section_07_use_ide_of_choice(asciicast_stream):
    shell = Shell(asciicast_stream)

    shell.appear(bright(cyan("# Use the IDE of your choice")) + newline())
    shell.appear(console_arrow())
    asciicast_stream.wait(5)

    shell.type_chars("vim ")
    shell.type_chars("te")
    shell.appear("st/realm/")
    shell.type_chars("te")
    shell.appear("st_main.py")
    shell.press_enter()

    content_lines = [
        cyan("import") + " io",
        "",
        cyan("from") + " approvaltests.approvals " + cyan("import") + " verify",
        cyan("from") + " asciicast.stream " + cyan("import") + " AsciicastStream",
        "",
        "",
        cyan("def") + " " + yellow("test_merge_two_streams") + "()",
        "    string_stream1 " + dim(white("=")) + " io.StringIO(",
        "    " + green("\"\"\"{\"version\": 2, \"width\": 1, \"height\": 2}"),
        "            " + green("[1, \"o\", \"x\"]\""),
        "            " + green("[2, \"i\", \"y\"]\"\"\"") + ")",
        "    ",
        "    string_stream2 " + dim(white("=")) + " io.StringIO(",
        "    " + green("\"\"\"{\"version\": 2, \"width\": 2, \"height\": 3}"),
        "            " + green("[0.1, \"o\", \"a\"]\""),
        "            " + green("[1.2, \"i\", \"b\"]\"\"\"") + ")",
        "    ",
        "    string_stream " + dim(white("=")) + " io.StringIO()",
        "    asciicast_stream " + dim(white("=")) + " AsciicastStream(" +
        "width=" + dim(white("=")) + magenta("60")+", " +
        "height" + dim(white("=")) + magenta("21")+", " +
        "stream" + dim(white("=")) + "string_stream)",
        "    ",
        "    asciicast_stream.write_from_input_stream(string_stream1)",
        "    asciicast_stream.write_from_input_stream(string_stream2)",
        "    ",
        "    verify(string_stream.getvalue())",
        ""
    ]
    vim = VimEditor(asciicast_stream, "\n".join(content_lines))

    vim.display_content()
    asciicast_stream.wait(10)

    vim.cursor_down(6)
    vim.content_scroll_down(5)
    asciicast_stream.wait(10)
    asciicast_stream.wait(5)
    vim.cursor_right(7)
    vim.cursor_right(6)
    asciicast_stream.wait(10)

    vim.appear_in_footer("-- INSERT --")
    asciicast_stream.wait(20)
    vim.delete_at_cursor(num_chars=3)
    asciicast_stream.wait(20)
    vim.type_at_cursor("word\n")

    vim.type_in_footer(":wq!")
    asciicast_stream.wait(20)
    vim.close()
    asciicast_stream.wait(5)


# ~~~~~~~~~~ Putting it together ~~~~~~~~~~``

sections = [
    ('build/01_hostname.cast', section_01_hostname),
    ('build/02_clone_project.cast', section_02_clone_project),
    ('build/03_standard_project_setup.cast', section_03_standard_project_setup),
    ('build/04_start_challenge.cast', section_04_start_challenge),
    ('build/05_real_world_challenge.cast', section_05_real_world_challenge),
    ('build/06_structure_code_your_way.cast', section_06_structure_code_your_way),
    ('build/07_use_IDE_of_choice.cast', section_07_use_ide_of_choice),
]


def create_asciicast_stream(char_stream):
    return AsciicastStream(width=60, height=21, stream=char_stream, length_of_one_tick_in_seconds=0.1)


for filename, func in sections:
    with open(filename, 'w') as f:
        func(create_asciicast_stream(f))

with open('build/e2e.cast', 'w') as f:
    main_stream = create_asciicast_stream(f)
    for filename, func in sections:
        main_stream.write_from_input_stream(open(filename, 'r'))

    main_stream.wait(ticks=50)
