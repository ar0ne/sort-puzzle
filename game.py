import pygame
import sys

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

class Game:
    """Game class"""
    def __init__(self, width: int, height: int):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def start(self):
        """Start game cycle"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.fill(BLACK)

            pygame.display.update()

            self.clock.tick(FRAMES_PER_SECOND)


if __name__ == "__main__":
    game = Game(WINDOW_WIDTH, WINDOW_HEIGHT)
    game.start()