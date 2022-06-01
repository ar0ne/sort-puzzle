"""
Puzzle generator
"""
import math
import random

from .color import Color
from .pile import Pile

MAX_ROW_SIZE = 7


def generate_simple_puzzle(
    game: "Game",
    num_groups: int = 5,
    group_length: int = 4,
    empty_groups: int = 2,
) -> None:
    """Generate random puzzle"""

    window_width = game.window.get_width()
    window_height = game.window.get_height()
    bottom_offset = math.ceil(window_height * 0.07)

    count_piles = num_groups + empty_groups
    row_size = MAX_ROW_SIZE if count_piles >= MAX_ROW_SIZE else count_piles
    num_rows = math.ceil(count_piles / MAX_ROW_SIZE)

    pile_width = math.ceil(window_width / row_size / 3)
    x_offset = pile_width * 3
    start_x = pile_width

    pile_block_height = math.ceil(
        (window_height - bottom_offset) / num_rows / (group_length + 1) * 0.9
    )
    y_offset = math.ceil(pile_block_height * (1 + group_length))
    start_y = pile_block_height

    # generate empty piles
    piles = []
    for idx in range(count_piles):

        if idx < row_size:
            pos_x = start_x + idx * x_offset
            pos_y = start_y
        else:
            pos_x = start_x + (idx - row_size) * x_offset
            pos_y = start_y + y_offset

        pile = Pile(
            game.window,
            pos_x,
            pos_y,
            pile_width,
            pile_block_height,
            group_length,
            callback=game.activate_element,
        )
        piles.append(pile)

    random_colors = random.sample(game.get_color_names_for_piles(), num_groups)
    colors = [Color[color] for color in random_colors for _ in range(group_length)]
    random.shuffle(colors)

    for group_idx in range(num_groups):
        for block_idx in range(group_length):
            piles[group_idx].push(colors[block_idx + group_idx * group_length])

    # link piles to game object
    for pile in piles:
        game.add_element(pile)
