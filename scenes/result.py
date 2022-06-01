"""
Result scene
"""
import sys

import pygame
import pygwidgets
from pyghelpers import Scene

from color import Color
from constants import RESULT_SCENE, PLAY_SCENE

TITLE = "Hooray!"
RESTART = "Restart"
QUIT = "Exit"


class ResultScene(Scene):
    """Game result scene"""

    def __init__(self, window) -> None:
        """Init scene"""
        self.window = window
        self.title_text = pygwidgets.DisplayText(
            self.window,
            (15, 25),
            TITLE,
            fontSize=50,
            textColor=Color.BLUE_VIOLET.value,
            width=400,
            justified="center",
        )
        self.restart_button = pygwidgets.TextButton(self.window, (300, 100), RESTART)
        self.exit_button = pygwidgets.TextButton(self.window, (300, 400), QUIT)

    def getSceneKey(self):
        """Get unique scene key"""
        return RESULT_SCENE

    def draw(self) -> None:
        """Draw scene"""
        self.window.fill(Color.RED.value)
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

