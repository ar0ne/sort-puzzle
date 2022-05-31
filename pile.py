"""Stack"""

from collections import deque
from typing import Optional, Callable

import pygame
from color import Color


class Stack:
    def __init__(self, max_length: int = 4) -> None:
        """Init stack"""
        self.max_length = max_length
        self.elements = deque(maxlen=self.max_length)

    def push(self, value: Color) -> bool:
        """Add element to stack"""
        if len(self.elements) < self.max_length:
            self.elements.append(value)
            return True
        return False

    def pop(self) -> Optional[Color]:
        """Pop element from stack"""
        if self.elements:
            return self.elements.pop()

    def peek(self) -> Optional[Color]:
        """Peek top element"""
        if not self.empty:
            return self.elements[-1]

    @property
    def empty(self) -> bool:
        return not len(self.elements)

    def __iter__(self):
        for el in list(self.elements):
            yield el


class Pile(Stack):
    """Container for elements"""

    def __init__(
        self,
        window,
        x: int,
        y: int,
        width: int,
        height: int,
        size: int,
        callback: Optional[Callable] = None,
    ) -> None:
        self.window = window
        self.block_width = width
        self.block_height = height
        self.size = size
        self.x = x
        self.y = y
        self.stack = Stack(self.size)
        self.rect = pygame.Rect(self.x, self.y, self.block_width, self.block_height * self.size)
        self.activated = False
        self.callback = callback
        super().__init__(self.size)

    def draw(self) -> None:
        """Draw elements"""
        for idx, color in enumerate(self.stack.elements):
            pygame.draw.rect(
                self.window,
                color.value,
                (
                    self.x,
                    self.y + (self.size - idx - 1) * self.block_height,
                    self.block_width,
                    self.block_height,
                ),
                0,
            )
        # draw border
        pygame.draw.rect(
            self.window,
            Color.PINK.value if self.activated else Color.BLACK.value,
            (
                self.x,
                self.y,
                self.block_width,
                self.block_height * self.size,
            ),
            2,
        )

    @property
    def full(self) -> bool:
        return len(self.stack.elements) == self.size

    def activate(self):
        self.activated = True

    def deactivate(self):
        self.activated = False

    def handle_event(self, event) -> None:
        """Handle event"""
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback(event, self)
                self.activate()
            else:
                self.deactivate()

    def can_move(self, pile: "Pile") -> bool:
        """Check if we can move elements to another pile"""
        return not pile.full and (pile.stack.empty or pile.stack.peek() == self.stack.peek())

    def move(self, pile: "Pile"):
        """Move element from one pile to another"""
        color = self.stack.peek().value
        available_cells = pile.size - len(pile.stack.elements)
        for _ in range(available_cells):
            if self.stack.empty:
                return
            if self.stack.peek().value != color:
                return
            el = self.stack.pop()
            pile.stack.push(el)
