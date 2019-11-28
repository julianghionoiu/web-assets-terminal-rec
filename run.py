#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
from decimal import Decimal

from colorama import Fore, Style

metadata = {"version": 2, "width": 60, "height": 21}


class Text:
    NEWLINE = "\r\n"
    CONSOLE_ARROW = Fore.CYAN + "➜ " + Style.RESET_ALL


def wait(ticks):
    return [{"duration_in_ticks": ticks, "content": ""}]


def appear(content):
    return [{"duration_in_ticks": 1, "content": content}]


def type(text="hostname"):
    return [{"duration_in_ticks": 1, "content": char} for char in text]


def press_enter():
    return [{"duration_in_ticks": 1, "content": Text.NEWLINE}]


asciicast_lines = []
asciicast_lines += wait(ticks=10)
asciicast_lines += appear(Text.CONSOLE_ARROW)
asciicast_lines += type("hostname")
asciicast_lines += press_enter()
asciicast_lines += appear("candidate-laptop.local" + Text.NEWLINE)


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float("{:.2f}".format(obj))
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


length_of_one_tick_in_seconds = 0.10
current_time_sec = Decimal(0.00)

if not os.path.exists('build'):
    os.makedirs('build')

with open('build/data.cast', 'w') as f:
    json.dump(metadata, f)
    f.write("\n")

    for line in asciicast_lines:
        asciicast_v2_line = [current_time_sec, "o", line["content"]]
        current_time_sec += Decimal(length_of_one_tick_in_seconds * line["duration_in_ticks"])

        json.dump(asciicast_v2_line, f, cls=DecimalEncoder)
        f.write("\n")
