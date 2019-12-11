import json
from decimal import Decimal


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

    def write_section_comment(self, comment):
        formatted_comment = "~~~~~~~~~~~~~  {}  ~~~~~~~~~~~~~".format(comment)
        self.write_frame(frame_type="i", content=formatted_comment)

    def write_internal_comment(self, comment):
        formatted_comment = "## -- {}".format(comment)
        self.write_frame(frame_type="i", content=formatted_comment)

    def wait(self, ticks: int):
        self.write_frame(ticks_before=ticks)

    def write_frame(self, content: str = "", frame_type: str = "o", ticks_before: int = 0, ticks_after: int = 0):
        self._current_time_sec += Decimal(self._length_of_one_tick_in_seconds * ticks_before)
        asciicast_v2_line = [self._current_time_sec, frame_type, content]
        json.dump(asciicast_v2_line, self._stream, cls=DecimalEncoder)
        self._stream.write("\n")
        self._current_time_sec += Decimal(self._length_of_one_tick_in_seconds * ticks_after)


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float("{:.2f}".format(obj))
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
