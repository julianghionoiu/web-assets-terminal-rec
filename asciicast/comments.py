from asciicast.frame import AsciicastFrame, AsciicastFrameType
from asciicast.stream import AsciicastStream


class Comments(object):

    def __init__(self, asciicast_stream: AsciicastStream) -> None:
        self._asciicast_stream = asciicast_stream

    def add(self, comment: str) -> None:
        self._asciicast_stream.write_frame(
            AsciicastFrame(0,
                           frame_type=AsciicastFrameType.INPUT,
                           content=comment))
