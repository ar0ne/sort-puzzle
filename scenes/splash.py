"""
Splash game scene
"""
import pygwidgets
from color import Color
from constants import GAME_SETTINGS, PLAY_SCENE, SPLASH_SCENE
from pyghelpers import Scene

GREETING = "Sort all piles to solve the puzzle!"
PLAY_BUTTON_TEXT = "Play"
PILES = "Piles:"
BLOCKS = "Blocks:"


class SpashScene(Scene):
    """Splash scene"""

    def __init__(self, window):
        self.window = window
        width = window.get_width()
        height = window.get_height()
        self.piles_count = 4
        self.blocks_count = 5
        self.message_field = pygwidgets.DisplayText(
            self.window,
            (0, 80),
            GREETING,
            fontSize=50,
            textColor=Color.PINK.value,
            width=width,
            justified="center",
        )
        self.go_to_play_button = pygwidgets.TextButton(
            self.window,
            (width / 2 - 55, height * 0.88),
            PLAY_BUTTON_TEXT,
        )
        self.piles_field = pygwidgets.DisplayText(
            self.window,
            (50, 200),
            PILES,
            fontSize=30,
            textColor=Color.WHEAT.value,
            width=100,
        )
        self.piles_count_field = pygwidgets.DisplayText(
            self.window,
            (150, 200),
            self.piles_count,
            fontSize=30,
            textColor=Color.WHEAT.value,
            width=50,
        )
        self.piles_count_plus_button = pygwidgets.TextButton(
            self.window,
            (200, 197),
            "+",
            width=25,
            height=25,
        )
        self.piles_count_minus_button = pygwidgets.TextButton(
            self.window,
            (230, 197),
            "-",
            width=25,
            height=25,
        )
        self.blocks_field = pygwidgets.DisplayText(
            self.window,
            (50, 250),
            BLOCKS,
            fontSize=30,
            textColor=Color.WHEAT.value,
            width=100,
        )
        self.blocks_count_field = pygwidgets.DisplayText(
            self.window,
            (150, 250),
            self.blocks_count,
            fontSize=30,
            textColor=Color.WHEAT.value,
            width=50,
        )
        self.blocks_count_plus_button = pygwidgets.TextButton(
            self.window,
            (200, 247),
            "+",
            width=25,
            height=25,
        )
        self.blocks_count_minus_button = pygwidgets.TextButton(
            self.window,
            (230, 247),
            "-",
            width=25,
            height=25,
        )

    def getSceneKey(self) -> str:
        """Get unique scene key"""
        return SPLASH_SCENE

    def draw(self) -> None:
        """Draw scene"""
        self.window.fill(Color.SEA_GREEN.value)
        self.message_field.draw()
        self.go_to_play_button.draw()
        self.piles_field.draw()
        self.piles_count_field.draw()
        self.blocks_field.draw()
        self.blocks_count_field.draw()
        self.piles_count_plus_button.draw()
        self.piles_count_minus_button.draw()
        self.blocks_count_plus_button.draw()
        self.blocks_count_minus_button.draw()

    def handleInputs(self, events, keyPressedList) -> None:
        """Handle input events"""
        for event in events:
            if self.go_to_play_button.handleEvent(event):
                self.goToScene(PLAY_SCENE)

            if self.piles_count_plus_button.handleEvent(event):
                self.piles_count = min(self.piles_count + 1, 12)
            elif self.piles_count_minus_button.handleEvent(event):
                self.piles_count = max(self.piles_count - 1, 2)

            if self.blocks_count_minus_button.handleEvent(event):
                self.blocks_count = max(self.blocks_count - 1, 3)
            elif self.blocks_count_plus_button.handleEvent(event):
                self.blocks_count = min(self.blocks_count + 1, 11)

        self.piles_count_field.setText(self.piles_count)
        self.blocks_count_field.setText(self.blocks_count)

    def respond(self, requestID):
        if requestID == GAME_SETTINGS:
            return (self.piles_count, self.blocks_count)
