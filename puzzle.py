"""
Puzzle
"""
import random

from color import Color
from pile import Pile


class Puzzle:
    """Puzzle class"""

    @staticmethod
    def generate(game: "Game", num_groups: int = 5, group_size: int = 4) -> None:
        """Generate random puzzle"""

        x = 50
        x_offset = 100
        y = 50
        width = 30
        height = 40

        # generate empty piles
        piles = [
            Pile(
                game.window,
                x + idx * x_offset,
                y,
                width,
                height,
                group_size,
                callback=game.activate_element,
            )
            for idx in range(num_groups + 2)
        ]
        random_colors = list(set(Color.colors()))[:group_size]
        colors = [
            Color[color]
            for color in random_colors
            for _ in range(num_groups)
        ]
        random.shuffle(colors)

        for group_idx in range(num_groups):
            for block_idx in range(group_size):
                piles[group_idx].push(colors[block_idx + group_idx * group_size])

        # link piles to game object
        for pile in piles:
            game.add_element(pile)
