#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from asciicast.shell import Shell
from asciicast.stream import AsciicastStream
from asciicast.text import newline, bright, cyan, green, blue, console_arrow, yellow, white, dim, magenta, thumbs_up
from asciicast.vim import VimEditor

if not os.path.exists('build'):
    os.makedirs('build')


def section_01_hostname(asciicast_stream):
    shell = Shell(asciicast_stream)

    shell.type_chars("hostname")
    shell.press_enter()
    shell.appear("candidate-laptop.local" + newline())


def section_02_clone_project(asciicast_stream):
    shell = Shell(asciicast_stream)

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


def section_03_standard_project(asciicast_stream):
    shell = Shell(asciicast_stream)

    shell.type_chars("ls -1")
    asciicast_stream.wait(4)
    shell.press_enter()
    shell.appear(
        "README.md" + newline() +
        bright(blue("config")) + newline() +
        bright(blue("lib")) + newline() +
        "requirements.txt" + newline() +
        bright(blue("test")) + newline() +
        bright(blue("venv")) + newline()
    )


def section_04_start_challenge(asciicast_stream):
    shell = Shell(asciicast_stream)

    _send_command_show_status(shell, ChallengeStatus.NOT_STARTED)

    shell.appear(yellow("Type \"start\" to start challenge") + newline())
    shell.appear(">>> ")
    asciicast_stream.wait(10)
    shell.type_chars("start")
    shell.press_enter()

    shell.appear(newline())
    shell.appear(green("CHALLENGE STARTED") + newline())
    shell.appear("Round 1 description saved to: challenge/round1.txt")
    shell.appear(newline())


def section_05_real_world(asciicast_stream):
    shell = Shell(asciicast_stream)

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
    asciicast_stream.wait(10)


def section_06_structure_code(asciicast_stream):
    shell = Shell(asciicast_stream)

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


def section_07_use_ide_of_choice(asciicast_stream):
    shell = Shell(asciicast_stream)

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
        "width=" + dim(white("=")) + magenta("60") + ", " +
        "height" + dim(white("=")) + magenta("21") + ", " +
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
    asciicast_stream.wait(4)
    vim.cursor_down(4)
    vim.cursor_right(7)
    vim.cursor_right(6)
    asciicast_stream.wait(4)

    vim.appear_in_footer("-- INSERT --")
    asciicast_stream.wait(4)
    vim.delete_at_cursor(num_chars=3)
    asciicast_stream.wait(4)
    vim.type_at_cursor("3.5")
    asciicast_stream.wait(5)

    vim.type_in_footer(":wq!")
    asciicast_stream.wait(5)
    vim.close()


def section_08_your_tests_your_way(asciicast_stream):
    shell = Shell(asciicast_stream)

    shell.type_chars("py.test")
    shell.press_enter()

    shell.appear(bright(white("=== test session starts ===")) + newline())
    shell.appear(newline())
    shell.appear(green("[  7%]  ") + "tests/acceptance/test_e2e.py" + green(" .") + newline())
    shell.appear(green("[ 38%]  ") + "tests/unit/test_main.py" + green(" ....") + newline())
    shell.appear(green("[100%]  ") + "tests/unit/test_class.py" + green(" ........") + newline())
    shell.appear(newline())
    shell.appear(green("=== ") + bright(green("13 passed")) + green(" in 0.20s ===") + newline())


def section_09_deploy_to_prod(asciicast_stream):
    shell = Shell(asciicast_stream)

    _send_command_show_status(shell, ChallengeStatus.ROUND_1_STARTED)

    shell.appear(yellow("Type \"deploy\" to deploy to production") + newline())
    shell.appear(">>> ")
    asciicast_stream.wait(10)
    shell.type_chars("deploy")
    shell.press_enter()

    shell.appear(newline())
    shell.appear("Selected action is: deploy" + newline())
    shell.appear("Waiting for requests" + newline())
    shell.appear(newline())
    asciicast_stream.wait(5)
    shell.appear("id = REALM_R1_001, req = realm([]), resp = []" + newline())
    shell.appear("id = REALM_R1_002, req = realm([1, 1]), resp = [0, 0]" + newline())
    shell.appear("id = REALM_R1_003, req = realm([1, 2, 3]), resp = [0, 2, 0]" + newline())
    shell.appear(newline())
    asciicast_stream.wait(3)

    shell.appear("ROUND 1 result is: " + green("PASSED") + newline())
    shell.appear(yellow("Get ready for the next round!" + newline()))


def section_10_incremental_rounds(asciicast_stream):
    shell = Shell(asciicast_stream)

    _send_command_show_status(shell, ChallengeStatus.COMPLETED)

    shell.appear(newline())
    shell.appear(green("Challenge completed in ") + bright(green("1h 40min")) + newline())
    asciicast_stream.wait(10)
    shell.appear(thumbs_up() + newline())


# ~~~~~~~~~~ Common stuff

class ChallengeStatus:
    IDENT = "             "

    NOT_STARTED = newline().join([
        IDENT + "ROUND 1 - not started",
        IDENT + "ROUND 2 - not started",
        IDENT + "ROUND 3 - not started",
        IDENT + "ROUND 4 - not started",
        IDENT + "ROUND 5 - not started",
    ])

    ROUND_1_STARTED = newline().join([
        IDENT + "ROUND 1 - " + bright(blue("running for 12 min")),
        IDENT + "ROUND 2 - not started",
        IDENT + "ROUND 3 - not started",
        IDENT + "ROUND 4 - not started",
        IDENT + "ROUND 5 - not started",
    ])

    COMPLETED = newline().join([
        IDENT + "ROUND 1 - " + green("completed in 20 min"),
        IDENT + "ROUND 2 - " + green("completed in 45 min"),
        IDENT + "ROUND 3 - " + green("completed in 13 min"),
        IDENT + "ROUND 4 - " + green("completed in 41 min"),
        IDENT + "ROUND 5 - " + green("completed in 32 min"),
    ])


def _send_command_show_status(shell: Shell, challenge_status: str):
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
        challenge_status + newline()
    )
    shell.appear("-------------------" + newline())


# ~~~~~~~~~~ Putting it together ~~~~~~~~~~``

sections = [
    ('build/01_hostname.cast', section_01_hostname, "Use own laptop and tools"),
    ('build/02_clone_project.cast', section_02_clone_project, "Clone a starting project - pick language"),
    ('build/03_standard_project.cast', section_03_standard_project, "Standard project for the language of choice"),
    ('build/04_start_challenge.cast', section_04_start_challenge, "Start challenge from CLI or IDE"),
    ('build/05_real_world.cast', section_05_real_world, "Solve a real-world, scenario based challenge"),
    ('build/06_structure_code.cast', section_06_structure_code, "Structure the code your way"),
    ('build/07_use_IDE_of_choice.cast', section_07_use_ide_of_choice, "Use the IDE of your choice"),
    ('build/08_your_tests_your_way.cast', section_08_your_tests_your_way, "Your tests - your way"),
    ('build/09_deploy_to_prod.cast', section_09_deploy_to_prod, "Deploy to Prod = run remote tests"),
    ('build/10_incremental_rounds.cast', section_10_incremental_rounds, "Solve all rounds to complete the challenge"),
]


def create_asciicast_stream(char_stream):
    return AsciicastStream(width=60, height=21, stream=char_stream, length_of_one_tick_in_seconds=0.1)


for filename, render_func, comment in sections:
    with open(filename, 'w') as f:
        _asciicast_stream = create_asciicast_stream(f)

        _shell = Shell(_asciicast_stream)
        _shell.appear(bright(cyan("# " + comment)) + newline())
        _shell.appear(console_arrow())

        _asciicast_stream.wait(20)
        render_func(_asciicast_stream)

        _shell.appear(newline())
        _asciicast_stream.wait(15)

with open('build/e2e.cast', 'w') as f:
    main_stream = create_asciicast_stream(f)
    for filename, _, _ in sections:
        main_stream.write_from_input_stream(open(filename, 'r'))

    main_stream.wait(ticks=50)
