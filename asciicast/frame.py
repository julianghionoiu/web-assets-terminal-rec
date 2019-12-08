from enum import Enum


class AsciicastFrameType(object):
    INPUT = "i"
    OUTPUT = "o"


class AsciicastFrame(object):
    duration_in_ticks: int
    content: str

    def __init__(self,
                 duration_in_ticks: int = 1,
                 frame_type: str = AsciicastFrameType.OUTPUT,
                 content: str = "") -> None:
        self.duration_in_ticks = duration_in_ticks
        self.frame_type = frame_type
        self.content = content
