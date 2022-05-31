"""Stack"""

from collections import deque
from typing import Optional

import pygame
from color import Color


class Stack:
    def __init__(self, max_length: int = 4) -> None:
        """Init stack"""
        self.max_length = max_length
        self.elements = deque(maxlen=self.max_length)

    def push(self, value: Color) -> None:
        """Add element to stack"""
        if len(self.elements) < self.max_length:
            self.elements.append(value)

    def pop(self) -> Optional[Color]:
        """Pop element from stack"""
        if self.elements:
            return self.elements.pop()

    def __iter__(self):
        for el in list(self.elements):
            yield el


class Container:
    """Container for elements"""

    def __init__(
        self,
        window,
        x: int,
        y: int,
        width: int,
        height: int,
        size: int,
    ) -> None:
        self.window = window
        self.block_width = width
        self.block_height = height
        self.size = size
        self.x = x
        self.y = y
        self.stack = Stack(self.size)
        self.rect = pygame.Rect(self.x, self.y, self.block_width, self.block_height * self.size)

    def draw(self) -> None:
        for idx, color in enumerate(self.stack.elements):
            pygame.draw.rect(
                self.window,
                color.value,
                (self.x,
                self.y + idx * self.block_height,
                self.block_width,
                self.block_height),
                0
            )
