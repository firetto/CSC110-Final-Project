"""
window.py:
Contains PyGame window wrapper class.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

import pygame
import pygame_gui
from typing import Dict, List, Tuple
from button import Button


class Window:
    """
    Window class containing window update methods and window attributes.

    Instance Attributes:
     - _width: The width of the window (in px). Preset to be 800px.
     - _height: The height of the window (in px). Preset to be 600px.
     - _title: The name of the window
     - _running: Whether the window is running. If not, the window should close.
     - _screen: PyGame display surface
     - _gui_manager: pygame_gui UI Manager instance
     - _background_surface: a solid color for the surface
     - _buttons: List of buttons
     - _clock: pygame.time.Clock instance, used for updating GUI

    Representation Invariants:
    - self._width > 0
    - self._height > 0

    Sample Usage:
    >>> window = Window() # wow you did it!!!

    """
    _width: int
    _height: int
    _title: str
    _running: bool

    _buttons: List[Button]

    _screen: pygame.Surface
    _gui_manager: pygame_gui.UIManager
    _clock: pygame.time.Clock

    _background_surface: pygame.Surface

    def __init__(self) -> None:
        """Initialize window attributes, start window loop."""

        # Initialize basic window attributes
        self._running = True
        self._width = 900
        self._height = 600
        self._title = "Wildfire Thing!"
        self._buttons = []

        # Initialize Pygame stuff
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        # Initialize GUI
        self._gui_manager = pygame_gui.UIManager((self._width, self._height))

        # Initialize background surface
        self._background_surface = pygame.Surface((self._width, self._height))
        self._background_surface.fill(self._gui_manager.ui_theme.get_colour('dark_bg'))

        # Initialize clock
        self._clock = pygame.time.Clock()

        # Initialize buttons
        self._init_buttons()

    def draw_background(self) -> None:
        """
        Draws the background, call this BEFORE drawing images onto the window!
        """

        # Display background surface
        self.draw_to_screen(self._background_surface, (0, 0))

    def update(self) -> None:
        """Window loop body."""

        # Get time delta in ms
        time_delta = self._clock.tick(60) / 1000.0

        # Draw UI
        self._gui_manager.draw_ui(self._screen)

        # Update Pygame Display
        pygame.display.flip()

        # Handle window events
        self._handle_events()

        # Update GUI manager
        self._gui_manager.update(time_delta)

    def _handle_events(self) -> None:
        """Handle PyGame window events"""

        for event in pygame.event.get():

            # If window is to be closed
            if event.type == pygame.QUIT:
                self._running = False

            # User event
            elif event.type == pygame.USEREVENT:

                # Check if button was pressed
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                    # Loop through every button, and check if it is the button that was pressed
                    # (This is kind of bad and inefficient, look for a better way to do this!)
                    for button in self._buttons:
                        if event.ui_element == button:
                            button.press()
                            break

            self._gui_manager.process_events(event)

    def _init_buttons(self) -> None:
        """
        Initialize window buttons with their sizes, pygame_gui manager,
        and function that is to be called when the button is pressed.
        """

    def add_button(self, rect: pygame.Rect, label: str, function: any) -> None:
        """
        Add a button to list of buttons.

        Preconditions:
         - len(label) > 0
         - function is of function type (callable)
        """
        self._buttons.append(Button(rect=rect, label=label,
                                    manager=self._gui_manager, function=function))

    def is_running(self) -> bool:
        """ Return whether window is running."""
        return self._running

    def get_screen(self) -> pygame.Surface:
        """ Return the background screen instance"""
        return self._screen

    def draw_to_screen(self, surface: pygame.Surface, position: Tuple[int, int]) -> None:
        """
        Draw surface with rect onto self._screen.
        """
        self._screen.blit(surface, position)


if __name__ == "__main__":
    pygame.init()
    window = Window()
