"""
button.py:
Contains PyGame GUI button wrapper class.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

import pygame
import pygame_gui


class Button:
    """
    pygame_gui.elements.UIButton wrapper class, containing initialization of button
    as well as 'lambda' instances to easily call the corresponding button function when it is
    pressed.
    """

    # Private Instance Attributes:
    # - _button: pygame_gui button instance
    # - _function: function to call when button is pressed
    _button: pygame_gui.elements.UIButton
    _function: any = lambda: None

    def __init__(self, rect: pygame.Rect, label: str, manager: pygame_gui.UIManager,
                 function: any) -> None:
        """Initialize button attributes, function."""

        self._button = pygame_gui.elements.UIButton(relative_rect=rect,
                                                    text=label,
                                                    manager=manager)
        self._function = function

    def __eq__(self, other: pygame_gui.elements.UIButton) -> bool:
        """Return whether button instance is equal to another button."""
        return self._button == other

    def press(self) -> None:
        """Call _function()."""
        self._function()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['pygame', 'pygame_gui', 'python_ta.contracts'],
        # the names (strs) of imported modules
        'allowed-io': [],
        # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
