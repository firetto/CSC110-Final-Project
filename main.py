"""
main.py

Launch the program from here!

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

import pygame
from window import Window
from firemap import FireMap
from firemap_updater import FireMapUpdater
from data import Data
from ui_handler import add_buttons, add_sliders, update_sliders, draw_ui_text
from plot_manager import PlotManager

if __name__ == "__main__":

    # Initialize PyGame
    pygame.init()

    # Create a window wrapper class instance
    window = Window()

    # Initialize map image & dots
    firemap = FireMap()

    # Initialize data
    data = Data()

    firemap_updater = FireMapUpdater(data=data, firemap=firemap)

    plot_manager = PlotManager(window=window, data=data)

    add_buttons(window, firemap_updater, plot_manager)

    add_sliders(window)

    # Window loop
    while window.is_running():

        """ UPDATE STUFF """

        # Update the window's clock
        window.update_clock()

        if not plot_manager.is_plot_displayed():
            # Update the delta of the FireMapUpdater
            firemap_updater.update_delta(window.get_delta())

        # Update the sliders
        update_sliders(window, firemap_updater)

        """ DRAW STUFF """

        # Draw the background first!!!!
        window.draw_background()

        # Draw the buttons etc.
        window.draw_ui()

        if plot_manager.is_plot_displayed():
            plot_manager.draw_plot()

        else:
            # Draw the map stuff (image, dots)
            firemap.draw(window)

            # Draw the UI text
            draw_ui_text(window)

        # Draw the rest of the stuff and update the window!
        window.update()

    # Once loop ends, quit pygame.
    pygame.quit()
