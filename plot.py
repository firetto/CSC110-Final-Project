"""
plot.py:
Contains the method used to plot the data and the methods to collect the data points.
CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""
import datetime
from typing import Dict, List

import matplotlib

# THIS HAS TO BE HERE FOR SOME REASON!!!!!!!!!!! BLAME MATPLOTLIB!!!!
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg
import pylab
import pygame
from carbon_emissions import CarbonEmission
from temperature_deviation import TemperatureDeviance
from wildfires import WildFire


def get_plot(x1_axis: List[int], y1_axis: List[float], x2_axis: List[int],
             y2_axis: List[float], y1_label: str, y2_label: str, title: str) \
        -> pygame.Surface:
    """Plot a labelled graph of two lines which share an x-axis
    Preconditions:
        - all({x > 0 for x in x1_axis}) and all({x > 0 for x in x2_axis})
        - len(title
    """
    fig = pylab.figure(figsize=[800/85, 600/85],  # Inches
                       dpi=85,  # 100 dots per inch, so the resulting buffer is 800x600 pixels
                       )
    ax = fig.gca()
    ax2 = ax.twinx()
    ax.set_title(title)

    ax.set_xlabel('Year')
    ax.set_ylabel(y1_label)
    ax2.set_ylabel(y2_label)
    ax2.yaxis.label.set_color('r')
    ax.plot(x1_axis, y1_axis, 'k')
    ax2.plot(x2_axis, y2_axis, 'r')
    ax.ticklabel_format(useOffset=False, style='plain')
    ax2.ticklabel_format(useOffset=False, style='plain')

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")

    return surf


def get_data_points_wild_fires(wild_fire_dict: Dict[datetime.date, List[WildFire]], country: str) \
        -> (List[int], List[int]):
    """Return the x and y coordinates of the carbon data points
    """
    min_year = min([x.year for x in wild_fire_dict])
    max_year = max([x.year for x in wild_fire_dict])
    x_axis = list(range(min_year, max_year + 1))
    y_axis = [sum([len([fire for fire in wild_fire_dict[x] if fire.country == country])
                   for x in wild_fire_dict if x.year == y]) for y in x_axis]
    return (x_axis, y_axis)


def get_data_points_temp(temp_dict: Dict[datetime.date, TemperatureDeviance]) \
        -> (List[int], List[int]):
    """Return the x and y coordinates of the carbon data points
    """
    min_year = min([x.year for x in temp_dict])
    x_axis = list(range(min_year, min_year + len(temp_dict)))
    y_axis = [temp_dict[datetime.date(y, 1, 1)].temperature_deviance for y in x_axis]
    return (x_axis, y_axis)


def get_data_points_carbon(carbon_dict: Dict[datetime.date, List[CarbonEmission]], i: int) \
        -> (List[int], List[int]):
    """Return the x and y coordinates of the carbon data points. i=0 indicates Canada, i=1 indicates America
    Preconditions:
        - i == 0 or i == 1
    """
    min_year = min([x.year for x in carbon_dict])
    x_axis = list(range(min_year, min_year + len(carbon_dict)))
    y_axis = [carbon_dict[datetime.date(y, 1, 1)][i].emissions for y in x_axis]
    return (x_axis, y_axis)
