"""
Result scene
"""
from pyghelpers import Scene

from color import Color
from constants import RESULT_SCENE


class ResultScene(Scene):
    """Game result scene"""

    def __init__(self, window) -> None:
        """Init scene"""
        self.window = window

    def getSceneKey(self):
        """Get unique scene key"""
        return RESULT_SCENE

    def draw(self) -> None:
        """Draw scene"""
        self.window.fill(Color.RED.value)

    def handleInputs(self, events, keyPressedList):
        """handle events"""
        for event in events:
            pass