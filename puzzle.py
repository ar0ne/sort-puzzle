"""
Puzzle
"""
import random

from color import Color
from pile import Pile

MAX_ROW_SIZE = 7

class PuzzleGenerator:
    """Puzzle class"""


    @staticmethod
    def generate(game: "Game", num_groups: int = 5, group_size: int = 4) -> None:
        """Generate random puzzle"""

        num_groups = 12
        group_size = 5

        window_width = game.window.get_width()  # 640px
        window_height = game.window.get_height()  # 480px
        bottom_offset = int(window_height * 0.1)  # 64px

        count_piles = num_groups + 2
        row_size = MAX_ROW_SIZE if count_piles >= MAX_ROW_SIZE else count_piles
        pile_width = int(window_width / row_size / 3)
        x_offset = pile_width * 3
        start_x = pile_width


        pile_block_height = int ((window_height - bottom_offset) * 0.08)
        y_offset = group_size * pile_block_height + pile_block_height
        start_y = pile_block_height / 2

        # generate empty piles
        piles = []
        for idx in range(count_piles):
            pos_x = start_x + idx * x_offset
            if idx >= row_size:
                pos_x = start_x + (idx - row_size) * x_offset
                pos_y = start_y + y_offset
            else:
                pos_y = start_y

            pile = Pile(
                game.window,
                pos_x,
                pos_y,
                pile_width,
                pile_block_height,
                group_size,
                callback=game.activate_element,
            )
            piles.append(pile)

        random_colors = random.sample(game.get_color_names_for_piles(), num_groups)
        colors = [Color[color] for color in random_colors for _ in range(group_size)]
        random.shuffle(colors)

        for group_idx in range(num_groups):
            for block_idx in range(group_size):
                piles[group_idx].push(colors[block_idx + group_idx * group_size])

        # link piles to game object
        for pile in piles:
            game.add_element(pile)
