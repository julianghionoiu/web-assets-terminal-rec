import json
from decimal import Decimal
from typing import List

from asciicast.action import AsciicastAction


class AsciicastV2(object):
    width: int
    height: int
    asciicast_actions: List[AsciicastAction]

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.asciicast_actions = []

    def add_actions(self, list_of_actions: List[AsciicastAction]):
        self.asciicast_actions += list_of_actions

    def write_to_stream(self, stream, length_of_one_tick_in_seconds=0.10):
        metadata = {"version": 2, "width": self.width, "height": self.height}
        json.dump(metadata, stream)
        stream.write("\n")
        current_time_sec = Decimal(0.00)
        for asciicast_action in self.asciicast_actions:
            frames = asciicast_action.render_frames(self.width, self.height)
            for frame in frames:
                asciicast_v2_line = [current_time_sec, "o", frame.content]
                current_time_sec += Decimal(length_of_one_tick_in_seconds * frame.duration_in_ticks)
                json.dump(asciicast_v2_line, stream, cls=DecimalEncoder)
                stream.write("\n")


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float("{:.2f}".format(obj))
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
