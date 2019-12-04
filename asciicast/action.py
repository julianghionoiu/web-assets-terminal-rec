from abc import ABC, abstractmethod
from typing import List

from asciicast.frame import AsciicastFrame


class AsciicastAction(ABC):

    @abstractmethod
    def render_frames(self, width: int, height: int) -> List[AsciicastFrame]:
        ...
