"""
Result scene
"""
import sys

import pygame
import pygwidgets
from ..color import Color
from ..constants import PLAY_SCENE, RESULT_SCENE
from pyghelpers import Scene

TITLE = "Congratulations! You won!!!"
RESTART = "Start again"
QUIT = "Exit"


class ResultScene(Scene):
    """Game result scene"""

    def __init__(self, window) -> None:
        """Init scene"""
        self.window = window
        width = window.get_width()
        height = window.get_height()
        self.title_text = pygwidgets.DisplayText(
            self.window,
            (0, 80),
            TITLE,
            fontSize=50,
            textColor=Color.BLUE_VIOLET.value,
            width=width,
            justified="center",
        )
        self.restart_button = pygwidgets.TextButton(
            self.window, (width / 2 - 55, height / 2), RESTART
        )
        self.exit_button = pygwidgets.TextButton(self.window, (width / 2 - 55, 400), QUIT)

    def getSceneKey(self):
        """Get unique scene key"""
        return RESULT_SCENE

    def draw(self) -> None:
        """Draw scene"""
        self.window.fill(Color.GOLD.value)
        self.title_text.draw()
        self.restart_button.draw()
        self.exit_button.draw()

    def handleInputs(self, events, keyPressedList):
        """handle events"""
        for event in events:
            if self.restart_button.handleEvent(event):
                self.goToScene(PLAY_SCENE)
            if self.exit_button.handleEvent(event):
                pygame.quit()
                sys.exit()
