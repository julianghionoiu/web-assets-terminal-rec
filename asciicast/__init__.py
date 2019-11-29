import json
from decimal import Decimal

from colorama import Fore, Style


class Text:
    NEWLINE = "\r\n"
    CONSOLE_ARROW = Fore.CYAN + "➜ " + Style.RESET_ALL


def wait(ticks):
    return [{"duration_in_ticks": ticks, "content": ""}]


def appear(content):
    return [{"duration_in_ticks": 1, "content": content}]


def typing(text="hostname"):
    return [{"duration_in_ticks": 1, "content": char} for char in text]


def delete(num_chars):
    return [{"duration_in_ticks": 1, "content": "\b \b"} for _ in range(0, num_chars)]


def press_enter():
    return [{"duration_in_ticks": 1, "content": Text.NEWLINE}]


def red(text):
    return Fore.RED + text + Style.RESET_ALL


def green(text):
    return Fore.GREEN + text + Style.RESET_ALL


def dim(text):
    return Style.DIM + text + Style.RESET_ALL


def bright(text):
    return Style.BRIGHT + text + Style.RESET_ALL


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float("{:.2f}".format(obj))
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


def write_asciicast_v2(stream, metadata, asciicast_lines):
    length_of_one_tick_in_seconds = 0.10
    current_time_sec = Decimal(0.00)
    json.dump(metadata, stream)
    stream.write("\n")
    for line in asciicast_lines:
        asciicast_v2_line = [current_time_sec, "o", line["content"]]
        current_time_sec += Decimal(length_of_one_tick_in_seconds * line["duration_in_ticks"])

        json.dump(asciicast_v2_line, stream, cls=DecimalEncoder)
        stream.write("\n")
