"""
Play game scene
"""
import pygwidgets
from pyghelpers import Scene

from ..color import Color
from ..constants import GAME_SETTINGS, MENU_BUTTON_TXT, PLAY_SCENE, RESTART_BUTTON_TXT, RESULT_SCENE, SPLASH_SCENE
from ..game import Game
from ..puzzle_generator import generate_simple_puzzle


class PlayScene(Scene):
    """Play scene"""

    def __init__(self, window) -> None:
        """Init play scene"""
        self.window = window
        self.game = None
        width = window.get_width()
        self.restart_button = pygwidgets.TextButton(
            self.window,
            (width / 7 * 2, int(self.window.get_height() * 0.88)),
            RESTART_BUTTON_TXT,
        )
        self.menu_button = pygwidgets.TextButton(
            self.window,
            (width / 3 * 2, int(self.window.get_height() * 0.88)),
            MENU_BUTTON_TXT,
        )

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
            if self.menu_button.handleEvent(event):
                self.goToScene(SPLASH_SCENE)

    def enter(self, data) -> None:
        """Enter scene"""
        self.game = Game(self.window)
        num_groups, group_size = self.request(SPLASH_SCENE, GAME_SETTINGS)
        generate_simple_puzzle(self.game, num_groups, group_size)

    def draw(self) -> None:
        """Draw UI elements"""
        self.window.fill(Color.WHEAT.value)
        self.restart_button.draw()
        self.menu_button.draw()

        # draw game elements
        for elem in self.game.get_piles():
            elem.draw()
