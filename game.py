
import pygame
import sys

from color import Color
from stack import Container

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
        self.elements = []

    def start(self):
        """Start game cycle"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            # fill background
            self.window.fill(Color.BLACK.value)

            # draw game elements
            for elem in self.elements:
                elem.draw()

            # refresh display
            pygame.display.update()

            # stick to frame rate
            self.clock.tick(FRAMES_PER_SECOND)

    def add_element(self, element) -> None:
        """Add element"""
        self.elements.append(element)


if __name__ == "__main__":
    game = Game(WINDOW_WIDTH, WINDOW_HEIGHT)
    container = Container(game.window, 100, 50, 100, 75, 4)
    container.stack.push(Color.BLUE)
    container.stack.push(Color.RED)
    container.stack.push(Color.GREEN)
    game.add_element(container)
    game.start()