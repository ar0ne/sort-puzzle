"""
Play game scene
"""
from pyghelpers import Scene

from color import Color
from constants import PLAY_SCENE


class PlayScene(Scene):
    """Play scene"""

    def __init__(self, window):
        """Init play scene"""
        self.window = window

    def getSceneKey(self) -> str:
        """Get unique scene key"""
        return PLAY_SCENE

    def handleInputs(self, events, keyPressedList) -> None:
        """Handle events"""
        for event in events:
            pass

    def draw(self) -> None:
        """Draw UI elements"""
        self.window.fill(Color.WHITE.value)