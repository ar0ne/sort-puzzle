import sys
from typing import Optional

import pygame
from color import Color
from pile import Pile
from puzzle import Puzzle

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


class Game:
    """Game class"""

    def __init__(self, width: int, height: int):
        pygame.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.piles = []
        self.active_idx: Optional[int] = None

    def start(self):
        """Start game cycle"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # handle events
                for elem in self.piles:
                    elem.handle_event(event)

            # fill background
            self.window.fill(Color.WHITE.value)

            # draw game elements
            for elem in self.piles:
                elem.draw()

            # refresh display
            pygame.display.update()

            # stick to frame rate
            self.clock.tick(FRAMES_PER_SECOND)

    def add_element(self, element) -> None:
        """Add element"""
        self.piles.append(element)

    def activate_element(self, _, active_pile: Pile) -> None:
        """Activate element event callback"""
        if active_pile.empty:
            # don't let activate empty pile
            active_pile.deactivate()
        for idx, pile in enumerate(self.piles):
            if pile is active_pile:
                if self.active_idx is not None:
                    ex_active_pile = self.piles[self.active_idx]
                    if ex_active_pile.can_merge(active_pile):
                        ex_active_pile.merge(active_pile)
                        # reset active index and deactivate last activation
                        self.active_idx = None
                        active_pile.deactivate()
                        return
                self.active_idx = idx
                return


if __name__ == "__main__":
    game = Game(WINDOW_WIDTH, WINDOW_HEIGHT)
    Puzzle.generate(game, 3, 4)
    game.start()
