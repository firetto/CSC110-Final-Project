"""
window.py:
Contains PyGame window wrapper class.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

import pygame
import pygame_gui
from typing import Dict
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
     - _buttons: Dictionary of buttons with button string names as keys and Button instances
                 as corresponding values.

     Representation Invariants:
    - self._width > 0
    - self._height > 0

    """
    _width: int
    _height: int
    _title: str
    _running: bool

    _buttons: Dict[str, Button]

    _screen: pygame.Surface
    _gui_manager: pygame_gui.UIManager

    _background_surface: pygame.Surface

    def __init__(self) -> None:
        """Initialize window attributes, start window loop."""

        # Initialize basic window attributes
        self._running = True
        self._width = 800
        self._height = 600
        self._title = "Wildfire Thing!"

        self._buttons = {}

        # Initialize Pygame stuff
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        # Initialize GUI
        self._gui_manager = pygame_gui.UIManager((self._width, self._height))

        # Initialize background surface
        self._background_surface = pygame.Surface((self._width, self._height))
        self._background_surface.fill(self._gui_manager.ui_theme.get_colour('dark_bg'))

        # Initialize buttons
        self._init_buttons()

        # Start window loop
        self._start_loop()

    def _start_loop(self) -> None:
        """Start infinite window loop"""

        # Start infinite loop
        while self._running:
            self._update()

        # Once loop ends, quit pygame.
        pygame.quit()

    def _update(self) -> None:
        """Window loop body."""

        # self._manager.update(time_delta)

        # Display background surface
        self._screen.blit(self._background_surface, (0, 0))

        # Draw UI
        self._gui_manager.draw_ui(self._screen)

        # Update Pygame Display
        pygame.display.update()

        # Handle window events
        self._handle_events()

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
                        if event.ui_element == self._buttons[button]:
                            self._buttons[button].press()
                            break

    def _init_buttons(self) -> None:
        """
        Initialize window buttons with their sizes, pygame_gui manager,
        and function that is to be called when the button is pressed.
        """

        self._buttons['test'] = Button(rect=pygame.Rect((350, 280), (150, 40)),
                                       label="Hey there!",
                                       manager=self._gui_manager,
                                       function=lambda: print("Hello!"))


if __name__ == "__main__":
    pygame.init()
    window = Window()
