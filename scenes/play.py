"""
Play game scene
"""
from pyghelpers import Scene

from color import Color
from constants import PLAY_SCENE
from game import Game
from puzzle import PuzzleGenerator


class PlayScene(Scene):
    """Play scene"""

    def __init__(self, window) -> None:
        """Init play scene"""
        self.window = window
        self.game = Game(window)

    def getSceneKey(self) -> str:
        """Get unique scene key"""
        return PLAY_SCENE

    def handleInputs(self, events, keyPressedList) -> None:
        """Handle events"""
        for event in events:
            # handle events
            for elem in self.game.get_piles():
                elem.handle_event(event)

    def enter(self, data) -> None:
        """Enter scene"""
        PuzzleGenerator.generate(self.game, 5, 4)

    def draw(self) -> None:
        """Draw UI elements"""
        self.window.fill(Color.WHITE.value)

        # draw game elements
        for elem in self.game.get_piles():
            elem.draw()
