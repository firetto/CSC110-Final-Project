"""
main.py

Launch the program from here!

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

import pygame
import random
from window import Window
from firemap import FireMap

if __name__ == "__main__":

    # Initialize PyGame
    pygame.init()

    # Create a window wrapper class instance
    window = Window()

    # Initialize map image & dots
    firemap = FireMap()

    # Temporary buttons
    window.add_button(pygame.Rect((350, 480), (150, 40)),
                      "Add random dot", lambda: firemap.add_dot((random.randint(15, 90),
                                                                 random.randint(-180, -45))))
    window.add_button(pygame.Rect((550, 480), (150, 40)),
                      "Clear dots", lambda: firemap.clear_dots())

    # Window loop
    while window.is_running():

        # Draw the background first!!!!
        window.draw_background()

        # Draw the map stuff (image, dots)
        firemap.draw(window)

        # Draw the rest of the stuff, update the window!
        window.update()

    # Once loop ends, quit pygame.
    pygame.quit()
