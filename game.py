from typing import Optional, List

from pile import Pile


class Game:
    """Game class"""

    __slots__ = ("window", "_piles", "_active_idx")

    def __init__(self, window):
        self.window = window
        self._piles = []
        self._active_idx: Optional[int] = None

    def get_piles(self) -> Optional[List[Pile]]:
        """Get list of piles"""
        return self._piles

    def add_element(self, element) -> None:
        """Add element"""
        self._piles.append(element)

    def has_finished(self) -> bool:
        """True if nothing to solve more"""
        for pile in self._piles:
            if pile.empty:
                continue
            if pile.max_length != pile.size:
                return False
            color = pile._elements[0]
            for elem in pile._elements:
                if elem != color:
                    return False
        return True

    def activate_element(self, _, active_pile: Pile) -> None:
        """Activate element event callback"""
        if active_pile.empty:
            # don't let activate empty pile
            active_pile.deactivate()
        for idx, pile in enumerate(self._piles):
            if pile is active_pile:
                if self._active_idx is not None:
                    ex_active_pile = self._piles[self._active_idx]
                    if ex_active_pile.can_merge(active_pile):
                        ex_active_pile.merge(active_pile)
                        # reset active index and deactivate last activation
                        self._active_idx = None
                        active_pile.deactivate()
                        return
                self._active_idx = idx
                return
