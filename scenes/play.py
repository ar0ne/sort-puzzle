"""
Play game scene
"""
import pygwidgets
from color import Color
from constants import PLAY_SCENE, RESULT_SCENE
from game import Game
from puzzle import PuzzleGenerator
from pyghelpers import Scene

RESTART_BUTTON = "Restart"


class PlayScene(Scene):
    """Play scene"""

    def __init__(self, window) -> None:
        """Init play scene"""
        self.window = window
        self.game = None
        self.restart_button = pygwidgets.TextButton(self.window, (300, 420), RESTART_BUTTON)

    def getSceneKey(self) -> str:
        """Get unique scene key"""
        return PLAY_SCENE

    def handleInputs(self, events, keyPressedList) -> None:
        """Handle events"""
        for event in events:
            # handle events
            for elem in self.game.get_piles():
                elem.handle_event(event)
            if self.game.has_finished():
                self.goToScene(RESULT_SCENE)
            if self.restart_button.handleEvent(event):
                self.goToScene(PLAY_SCENE)

    def enter(self, data) -> None:
        """Enter scene"""
        self.game = Game(self.window)
        PuzzleGenerator.generate(self.game, 9, 5)

    def draw(self) -> None:
        """Draw UI elements"""
        self.window.fill(Color.WHITE.value)
        self.restart_button.draw()

        # draw game elements
        for elem in self.game.get_piles():
            elem.draw()
