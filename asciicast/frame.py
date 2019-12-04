class AsciicastFrame(object):
    duration_in_ticks: int
    content: str

    def __init__(self, duration_in_ticks: int, content: str) -> None:
        self.duration_in_ticks = duration_in_ticks
        self.content = content
