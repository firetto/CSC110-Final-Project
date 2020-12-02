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
    as well as 'lambda' instances to easily call the corresponding button function when it is pressed,

    Instance Attributes:
    - _button: pygame_gui button instance
    - _function: function to call when button is pressed
    """

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
        """Call corresponding function when button is pressed."""
        self._function()
