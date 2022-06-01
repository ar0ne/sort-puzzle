"""
Splash game scene
"""
import pygwidgets
from color import Color
from constants import PLAY_SCENE, SPLASH_SCENE
from pyghelpers import Scene

GREETING = "Hello world"
PLAY_BUTTON_TEXT = "Play"


class SpashScene(Scene):
    """Splash scene"""

    def __init__(self, window):
        self.window = window
        self.message_field = pygwidgets.DisplayText(
            self.window,
            (15, 25),
            GREETING,
            fontSize=50,
            textColor=Color.BLACK.value,
            width=400,
            justified="center",
        )
        self.go_to_play_button = pygwidgets.TextButton(self.window, (250, 100), PLAY_BUTTON_TEXT)

    def getSceneKey(self) -> str:
        """Get unique scene key"""
        return SPLASH_SCENE

    def draw(self) -> None:
        """Draw scene"""
        self.window.fill(Color.SEA_GREEN.value)
        self.message_field.draw()
        self.go_to_play_button.draw()

    def handleInputs(self, events, keyPressedList) -> None:
        """Handle input events"""
        for event in events:
            if self.go_to_play_button.handleEvent(event):
                self.goToScene(PLAY_SCENE)
