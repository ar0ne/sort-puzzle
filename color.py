"""Color"""
from enum import Enum
from typing import List


class Color(Enum):
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    PINK = (255, 51, 153)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    @classmethod
    def colors(cls) -> List[str]:
        """Get available color names"""
        all = cls._member_names_
        return list(filter(lambda n: n != Color.WHITE.name, all))