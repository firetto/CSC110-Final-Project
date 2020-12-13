"""
ui_handler.py:
Contains functions for adding buttons and sliders to window, as well as managing the sliders.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

import pygame
from window import Window
from firemap_updater import FireMapUpdater
from plot_manager import PlotManager


def add_buttons(window: Window, updater: FireMapUpdater, plot_manager: PlotManager) -> None:
    """Add the necessary buttons to the window, such as
    the animation control buttons"""

    window.add_button(pygame.Rect((68 + 100, 440), (150, 50)),
                      "Play", lambda: start_map_animation(updater, plot_manager))
    window.add_button(pygame.Rect((375, 440), (150, 50)),
                      "Pause", lambda: stop_map_animation(updater, plot_manager))
    window.add_button(pygame.Rect((683 - 100, 440), (150, 50)),
                      "Restart", lambda: restart_map_animation(updater, plot_manager))

    window.add_button(pygame.Rect((75, 620), (120, 50)),
                      "View Map", lambda: plot_manager.set_plot("none"))

    window.add_button(pygame.Rect((225, 620), (120, 50)),
                      "View Plot 1", lambda: plot_manager.set_plot("canada_vs_carbon"))

    window.add_button(pygame.Rect((375, 620), (120, 50)),
                      "View Plot 2", lambda: plot_manager.set_plot("america_vs_carbon"))

    window.add_button(pygame.Rect((525, 620), (120, 50)),
                      "View Plot 3", lambda: plot_manager.set_plot("canada_vs_temp"))

    window.add_button(pygame.Rect((675, 620), (120, 50)),
                      "View Plot 4", lambda: plot_manager.set_plot("america_vs_temp"))


def add_sliders(window: Window) -> None:
    """
    Add the necessary sliders to the window.
    """
    window.add_slider(rect=pygame.Rect((375, 550), (150, 25)), label="speed",
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
                     window.BACKGROUND_COLOR[2])), (335, 520))


def start_map_animation(updater: FireMapUpdater, plot_manager: PlotManager) -> None:
    """
    Start the map timelapse ONLY IF a plot is currently not being displayed.
    This is done so you can't click the buttons through the plots.
    """
    if not plot_manager.is_plot_displayed():
        updater.start_animation()


def stop_map_animation(updater: FireMapUpdater, plot_manager: PlotManager) -> None:
    """
    Stop the map timelapse ONLY IF a plot is currently not being displayed.
    This is done so you can't click the buttons through the plots.
    """
    if not plot_manager.is_plot_displayed():
        updater.stop_animation()


def restart_map_animation(updater: FireMapUpdater, plot_manager: PlotManager) -> None:
    """
    Restart the map timelapse ONLY IF a plot is currently not being displayed.
    This is done so you can't click the buttons through the plots.
    """
    if not plot_manager.is_plot_displayed():
        updater.restart_animation()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['window', 'firemap_updater', 'pygame', 'plot_manager',
                          'python_ta.contracts'],
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
