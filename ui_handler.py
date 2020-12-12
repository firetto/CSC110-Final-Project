"""
ui_handler.py:
Contains functions for adding buttons and sliders to window, as well as managing the sliders.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

from window import Window
from firemap_updater import FireMapUpdater
import pygame


def add_buttons(window: Window, updater: FireMapUpdater) -> None:
    """Add the necessary buttons to the window, such as
    the animation control buttons"""

    window.add_button(pygame.Rect((68 + 100, 440), (150, 50)),
                      "Play", lambda: updater.start_animation())
    window.add_button(pygame.Rect((375, 440), (150, 50)),
                      "Pause", lambda: updater.stop_animation())
    window.add_button(pygame.Rect((683 - 100, 440), (150, 50)),
                      "Restart", lambda: updater.restart_animation())


def add_sliders(window: Window) -> None:
    """
    Add the necessary sliders to the window.
    """
    window.add_slider(rect=pygame.Rect((375, 570), (150, 25)), label="speed",
                      start_value=1, value_range=(0.25, 6))


def update_sliders(window: Window, updater: FireMapUpdater) -> None:
    """
    Update fire map based on slider values.

    Preconditions:
     - window has a slider "speed"
    """
    updater.set_animation_speed(window.get_slider_value("speed"))


def draw_ui_text(window: Window) -> None:
    """
    Render the UI text, such as the slider label and animation speed.
    """

    window.draw_to_screen(window.render_text(
        f"Timelapse Speed: {round(window.get_slider_value('speed'), 1)}x",
        True, pygame.Color(255, 255, 255),
        pygame.Color(window.BACKGROUND_COLOR[0], window.BACKGROUND_COLOR[1],
                     window.BACKGROUND_COLOR[2])), (335, 540))
