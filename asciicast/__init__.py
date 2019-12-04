import json
from decimal import Decimal
from typing import List

from colorama import Fore, Style


class AsciicastLine(object):
    duration_in_ticks: int
    content: str

    def __init__(self, duration_in_ticks: int, content: str) -> None:
        self.duration_in_ticks = duration_in_ticks
        self.content = content


class AsciicastV2(object):
    width: int
    height: int
    asciicast_lines: List[AsciicastLine]

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.asciicast_lines = []

    def add_all_lines(self, list_of_line_lists: List[List[AsciicastLine]]):
        for line_list in list_of_line_lists:
            self.asciicast_lines += line_list

    def add_lines(self, line_list: List[AsciicastLine]):
        self.asciicast_lines += line_list

    def write_to_stream(self, stream, length_of_one_tick_in_seconds=0.10):
        metadata = {"version": 2, "width": self.width, "height": self.height}
        json.dump(metadata, stream)
        stream.write("\n")
        current_time_sec = Decimal(0.00)
        for line in self.asciicast_lines:
            asciicast_v2_line = [current_time_sec, "o", line.content]
            current_time_sec += Decimal(length_of_one_tick_in_seconds * line.duration_in_ticks)

            json.dump(asciicast_v2_line, stream, cls=DecimalEncoder)
            stream.write("\n")


class Text(object):
    @staticmethod
    def newline() -> str:
        return "\r\n"

    @staticmethod
    def console_arrow() -> str:
        return Fore.CYAN + "➜ " + Style.RESET_ALL

    @staticmethod
    def red(text: str) -> str:
        return Fore.RED + text + Style.RESET_ALL

    @staticmethod
    def green(text: str) -> str:
        return Fore.GREEN + text + Style.RESET_ALL

    @staticmethod
    def dim(text: str) -> str:
        return Style.DIM + text + Style.RESET_ALL

    @staticmethod
    def bright(text: str) -> str:
        return Style.BRIGHT + text + Style.RESET_ALL


def wait(ticks: int) -> List[AsciicastLine]:
    return [AsciicastLine(ticks, "")]


def appear(content: str) -> List[AsciicastLine]:
    return [AsciicastLine(1, content)]


def type_chars(text: str) -> List[AsciicastLine]:
    return [AsciicastLine(1, char) for char in text]


def delete(num_chars: int) -> List[AsciicastLine]:
    return [AsciicastLine(1, "\b \b") for _ in range(0, num_chars)]


def press_enter() -> List[AsciicastLine]:
    return [AsciicastLine(1, Text.newline())]


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float("{:.2f}".format(obj))
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
