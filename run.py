#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

from decimal import Decimal

from colorama import Fore, Style

metadata = {"version": 2, "width": 178, "height": 21, "timestamp": 1574614914,
            "env": {"SHELL": "/bin/zsh", "TERM": "xterm-256color"}}

lines = [
    {"duration_in_ticks": 10, "content": ""},
    {"duration_in_ticks": 1, "content": Fore.CYAN + "➜ " + Style.RESET_ALL},
    {"duration_in_ticks": 1, "content": "h"},
    {"duration_in_ticks": 1, "content": "o"},
    {"duration_in_ticks": 1, "content": "s"},
    {"duration_in_ticks": 1, "content": "t"},
    {"duration_in_ticks": 1, "content": "n"},
    {"duration_in_ticks": 1, "content": "a"},
    {"duration_in_ticks": 1, "content": "m"},
    {"duration_in_ticks": 1, "content": "e"},
    {"duration_in_ticks": 1, "content": "\r\r\n"},
    {"duration_in_ticks": 1, "content": "candidate-laptop.local\r\n"}
]


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

    for line in lines:
        asciicast_v2_line = [current_time_sec, "o", line["content"]]
        current_time_sec += Decimal(length_of_one_tick_in_seconds * line["duration_in_ticks"])

        json.dump(asciicast_v2_line, f, cls=DecimalEncoder)
        f.write("\n")
