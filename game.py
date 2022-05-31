import sys
from typing import Optional

import pygame
from color import Color
from pile import Pile

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

    def activate_element(self, _, activated_pile: Pile) -> None:
        """Activate element event callback"""
        if activated_pile.empty:
            activated_pile.deactivate()
        for idx, pile in enumerate(self.piles):
            if pile is activated_pile:
                if self.active_idx is not None:
                    old_pile = self.piles[self.active_idx]
                    if old_pile.can_move(activated_pile):
                        old_pile.move(activated_pile)
                        self.active_idx = None
                        activated_pile.deactivate()
                        return
                self.active_idx = idx
                return


if __name__ == "__main__":
    game = Game(WINDOW_WIDTH, WINDOW_HEIGHT)

    pile1 = Pile(game.window, 50, 50, 30, 40, 4, callback=game.activate_element)
    pile1.push(Color.BLUE)
    pile1.push(Color.RED)
    pile1.push(Color.GREEN)
    pile1.push(Color.GREEN)

    pile2 = Pile(game.window, 150, 50, 30, 40, 4, callback=game.activate_element)
    pile2.push(Color.GREEN)

    pile3 = Pile(game.window, 250, 50, 30, 40, 4, callback=game.activate_element)

    pile4 = Pile(game.window, 350, 50, 30, 40, 4, callback=game.activate_element)
    pile4.push(Color.RED)
    pile4.push(Color.GREEN)

    piles = [
        pile1,
        pile2,
        pile3,
        pile4,
    ]
    for pile in piles:
        game.add_element(pile)

    game.start()
