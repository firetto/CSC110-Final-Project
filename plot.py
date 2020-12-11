"""
plot.py:
Contains the method used to plot the data
CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""
import matplotlib
import matplotlib.backends.backend_agg as agg
import pylab
import pygame
from pygame.locals import *
from typing import List
matplotlib.use("Agg")


def plot(x1_axis: List[int], y1_axis: List[float], x2_axis: List[int],
         y2_axis: List[float], y1_label: str, y2_label: str):
    """Plot a labelled graph of two lines which share an x-axis
    Preconditions:
        all({x > 0 for x in x1_axis}) and all({x > 0 for x in x2_axis})
    """
    fig = pylab.figure(figsize=[8, 8],  # Inches
                       dpi=100,  # 100 dots per inch, so the resulting buffer is 400x400 pixels
                       )
    ax = fig.gca()
    ax2 = ax.twinx()
    ax.set_xlabel('Year')
    ax.set_ylabel(y1_label)
    ax2.set_ylabel(y2_label)
    ax.plot(x1_axis, y1_axis, 'k')
    ax2.plot(x2_axis, y2_axis, 'r')
    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    pygame.init()

    window = pygame.display.set_mode((800, 800), DOUBLEBUF)
    screen = pygame.display.get_surface()

    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (0, 0))
    pygame.display.flip()
    running = True
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
    except SystemExit:
        pygame.quit()
