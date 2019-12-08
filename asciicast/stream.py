import json
from decimal import Decimal

from asciicast.frame import AsciicastFrame


class AsciicastStream(object):
    width: int
    height: int

    def __init__(self, width: int, height: int, stream, length_of_one_tick_in_seconds=0.10) -> None:
        self.width = width
        self.height = height
        self._length_of_one_tick_in_seconds = length_of_one_tick_in_seconds

        # Start the stream
        self._stream = stream
        self._current_time_sec = Decimal(0.00)
        metadata = {"version": 2, "width": self.width, "height": self.height}
        json.dump(metadata, stream)
        stream.write("\n")

    def write_frame(self, frame: AsciicastFrame):
        asciicast_v2_line = [self._current_time_sec, frame.frame_type, frame.content]
        self._current_time_sec += Decimal(self._length_of_one_tick_in_seconds * frame.duration_in_ticks)
        json.dump(asciicast_v2_line, self._stream, cls=DecimalEncoder)
        self._stream.write("\n")


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float("{:.2f}".format(obj))
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
