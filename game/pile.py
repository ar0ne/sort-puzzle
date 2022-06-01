"""Pile"""

from collections import deque
from typing import Any, Callable, Optional

import pygame

from .color import Color


class Stack:
    """Simple stack"""

    __slots__ = ("max_length", "_elements")

    def __init__(self, max_length: int = 4) -> None:
        """Init stack"""
        self.max_length = max_length
        self._elements = deque(maxlen=self.max_length)

    def push(self, value: Any) -> bool:
        """Add element to stack"""
        if self.size < self.max_length:
            self._elements.append(value)
            return True
        return False

    def pop(self) -> Optional[Any]:
        """Pop element from stack"""
        if self._elements:
            return self._elements.pop()

    def peek(self) -> Optional[Any]:
        """Peek top element"""
        if not self.empty:
            return self._elements[-1]

    @property
    def empty(self) -> bool:
        """True if stack is empty"""
        return not self.size

    @property
    def size(self) -> int:
        """Get size of elements"""
        return len(self._elements)

    @property
    def full(self) -> bool:
        """True if pile is full"""
        return self.size == self.max_length

    @property
    def elements(self) -> deque:
        return self._elements


class Pile(Stack):
    """Container for elements"""

    NO_BORDER = 0
    BORDER_WIDTH = 2

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
        """Init pile"""
        self.window = window
        self.block_width = width
        self.block_height = height
        self.x = x
        self.y = y
        self.padding = width // 2
        self.rect = pygame.Rect(
            self.x - self.padding,
            self.y - self.padding,
            self.block_width + 2 * self.padding,
            self.block_height * size + 2 * self.padding,
        )
        self.activated = False
        self.callback = callback
        super().__init__(size)

    def draw(self) -> None:
        """Draw elements"""
        for idx, color in enumerate(self.elements):
            pygame.draw.rect(
                self.window,
                color.value,
                (
                    self.x,
                    self.y + (self.max_length - idx - 1) * self.block_height,
                    self.block_width,
                    self.block_height,
                ),
                self.NO_BORDER,
            )
        # draw border
        pygame.draw.rect(
            self.window,
            Color.GOLD.value if self.activated else Color.BLACK.value,
            (
                self.x,
                self.y,
                self.block_width,
                self.block_height * self.max_length,
            ),
            self.BORDER_WIDTH,
        )

    def activate(self) -> None:
        """Activate pile"""
        self.activated = True

    def deactivate(self) -> None:
        """Deactivate pile"""
        self.activated = False

    def handle_event(self, event) -> None:
        """Handle event"""
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                self.activate()
                if self.callback:
                    self.callback(event, self)
            else:
                self.deactivate()

    def can_merge(self, pile: "Pile") -> bool:
        """Check if we can merge elements with another pile"""
        return not pile.full and (pile.empty or pile.peek() == self.peek())

    def merge(self, pile: "Pile") -> None:
        """Move elements from one pile to another"""
        color = self.peek()
        if self.empty:
            return
        for _ in range(pile.max_length - pile.size):
            if self.peek() != color:
                return
            pile.push(self.pop())
