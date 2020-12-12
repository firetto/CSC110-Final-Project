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

    # Temporary buttons
    # window.add_button(pygame.Rect((350, 480), (150, 40)),
    #                   "Add random dot", lambda: firemap.add_dot((random.randint(15, 90),
    #                                                              random.randint(-180, -45))))
    # window.add_button(pygame.Rect((550, 480), (150, 40)),
    #                   "Clear dots", lambda: firemap.clear_dots())

    window.add_button(pygame.Rect((68+100, 440), (150, 50)),
                      "Play", lambda: firemap_updater.start_animation())
    window.add_button(pygame.Rect((375, 440), (150, 50)),
                      "Pause", lambda: firemap_updater.stop_animation())
    window.add_button(pygame.Rect((683-100, 440), (150, 50)),
                      "Restart", lambda: firemap_updater.restart_animation())

    # Window loop
    while window.is_running():

        """ UPDATE STUFF """

        # Update the window's clock
        window.update_clock()

        # Update the delta of the FireMapUpdater
        firemap_updater.update_delta(window.get_delta())

        """ DRAW STUFF """

        # Draw the background first!!!!
        window.draw_background()

        # Draw the map stuff (image, dots)
        firemap.draw(window)

        # Draw the rest of the stuff and update the window!
        window.update()

    # Once loop ends, quit pygame.
    pygame.quit()
