"""
Puzzle
"""
import random

from color import Color
from pile import Pile


class PuzzleGenerator:
    """Puzzle class"""

    @staticmethod
    def generate(game: "Game", num_groups: int = 5, group_size: int = 4) -> None:
        """Generate random puzzle"""

        window_width = game.window.get_width()
        x = 50
        y = 50
        width = 30
        height = 40
        x_offset = 100
        y_offset = group_size * height + 50

        # generate empty piles
        piles = []
        for idx in range(num_groups + 2):
            pos_x = x + idx * x_offset
            if pos_x > window_width:
                pos_x = x
                pos_y = y + y_offset
            else:
                pos_y = y

            pile = Pile(
                game.window,
                pos_x,
                pos_y,
                width,
                height,
                group_size,
                callback=game.activate_element,
            )
            piles.append(pile)

        random_colors = random.sample(Color.available(), num_groups)
        colors = [Color[color] for color in random_colors for _ in range(group_size)]
        random.shuffle(colors)

        for group_idx in range(num_groups):
            for block_idx in range(group_size):
                piles[group_idx].push(colors[block_idx + group_idx * group_size])

        # link piles to game object
        for pile in piles:
            game.add_element(pile)
