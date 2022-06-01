"""Color"""
from enum import Enum
from typing import List


class Color(Enum):
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    BLUE_VIOLET = (138, 43, 226)
    CORAL = (255, 127, 80)
    CYAN = (0, 255, 255)
    DARK_GREEN = (0, 100, 0)
    DEAP_SKY_BLUE = (0, 191, 255)
    GOLD = (255, 215, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    MAROON = (128, 0, 0)
    NAVY = (0, 0, 128)
    OLIVE = (128, 128, 0)
    ORCHID = (218, 112, 214)
    PINK = (255, 192, 203)
    RED = (255, 0, 0)
    SEA_GREEN = (46, 139, 87)
    SILVER = (192, 192, 192)
    TEAL = (0, 128, 128)
    WHEAT = (245, 222, 179)
    WHITE = (255, 255, 255)

    @classmethod
    def colors(cls) -> List[str]:
        """Get available color names"""
        excluded = map(lambda x: x.name, [Color.WHITE, Color.GOLD])
        return list(filter(lambda n: n not in excluded, cls._member_names_))
