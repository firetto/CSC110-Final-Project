"""
window.py:
Contains PyGame window wrapper class.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

from typing import Dict, List, Tuple
import pygame
import pygame_gui
from pygame_gui.elements.ui_horizontal_slider import UIHorizontalSlider
from button import Button


class Window:
    """
    Window class containing window update methods and window attributes.

    Instance Attributes:
     - BACKGROUND_COLOR: The background color of the window.


    Sample Usage:
    >>> pygame.init()
    (6, 0)
    >>> window = Window() # wow you did it!!!
    """

    # Private Instance Attributes:
    # - _width: The width of the window (in px). Preset to be 800px.
    # - _height: The height of the window (in px). Preset to be 600px.
    # - _title: The name of the window
    # - _running: Whether the window is running. If not, the window should close.
    # - _screen: PyGame display surface
    # - _gui_manager: pygame_gui UI Manager instance
    # - _background_surface: a solid color for the surface
    # - _buttons: List of buttons
    # - _sliders: A dictionary containing strings as keys
    #             and sliders as their corresponding values
    # - _clock: pygame.time.Clock instance, used for updating GUI
    # - _time_delta: the time delta in milliseconds for this update
    # - _font: PyGame font instance, used for rendering text.

    # Private Representation Invariants:
    # - self._width > 0
    # - self._height > 0

    _width: int
    _height: int
    _title: str
    _running: bool

    _buttons: List[Button]
    _sliders: Dict[str, UIHorizontalSlider]

    _screen: pygame.Surface
    _gui_manager: pygame_gui.UIManager
    _clock: pygame.time.Clock
    _time_delta: float

    _background_surface: pygame.Surface
    _font: pygame.font.Font

    BACKGROUND_COLOR: Tuple[int, int, int] = (20, 20, 30)

    def __init__(self) -> None:
        """Initialize window attributes, start window loop."""

        # Initialize basic window attributes
        self._running = True
        self._width = 900
        self._height = 700
        self._title = "Wildfire Thing!"
        self._buttons = []
        self._sliders = {}

        # Initialize Pygame stuff
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        # Initialize GUI
        self._gui_manager = pygame_gui.UIManager((self._width, self._height))

        # Initialize background surface
        self._background_surface = pygame.Surface((self._width, self._height))
        self._background_surface.fill(self.BACKGROUND_COLOR)

        # Initialize clock
        self._clock = pygame.time.Clock()
        self._time_delta = 0

        # Initialize font
        self._font = pygame.font.Font(None, 32)

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

        # Update Pygame Display
        pygame.display.flip()

        # Handle window events
        self._handle_events()

        # Update GUI manager (time takes seconds and not ms, so divide by 1000)
        self._gui_manager.update(self._time_delta / 1000.0)

    def draw_ui(self) -> None:
        """Draw the buttons and sliders and so on."""
        # Draw UI
        self._gui_manager.draw_ui(self._screen)

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

    def add_slider(self, rect: pygame.Rect, label: str,
                   start_value: float, value_range: Tuple[float, float]) -> None:
        """
        Add a slider to the dictionary of sliders.

        Preconditions:
         - label not in self._sliders
         - value_range[1] > value_range[0]
         - value_range[0] <= start_value <= value_range[1]
        """

        self._sliders[label] = UIHorizontalSlider(relative_rect=rect,
                                                  start_value=start_value,
                                                  value_range=value_range,
                                                  manager=self._gui_manager)

    def get_slider_value(self, label: str) -> float:
        """
        Return the value of the slider corresponding to label.

        Preconditions:
         - label in self._sliders
        """
        return self._sliders[label].get_current_value()

    def is_running(self) -> bool:
        """
        Return whether window is running.
        """
        return self._running

    def get_screen(self) -> pygame.Surface:
        """
        Return the background screen instance.
        """
        return self._screen

    def draw_to_screen(self, surface: pygame.Surface, position: Tuple[int, int]) -> None:
        """
        Draw surface at position onto self._screen.
        """
        self._screen.blit(surface, position)

    def update_clock(self) -> None:
        """
        Update the clock and set self._time_delta to be the time delta in milliseconds.
        """
        self._time_delta = self._clock.tick(60)

    def get_delta(self) -> float:
        """
        Return the time delta in milliseconds.
        """
        return self._time_delta

    def render_text(self, text: str, antialias: bool,
                    color: pygame.color.Color, background: pygame.color.Color) -> pygame.Surface:
        """
        Return the pygame Font render given the parameters.

        Preconditions:
        - len(text) > 0
        """
        return self._font.render(text, antialias, color, background)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['pygame', 'pygame_gui', 'pygame_gui.elements.ui_horizontal_slider',
                          'typing', 'button', 'python_ta.contracts'],
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
