"""
plot.py:
Contains the method used to plot the data and the methods to collect the data points.
CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""
import datetime
from typing import Dict, List, Tuple
import matplotlib
import matplotlib.backends.backend_agg as agg
import pygame
from carbon_emissions import CarbonEmission
from temperature_deviation import TemperatureDeviance
from wildfires import WildFire

# import pylab must be placed below this line or there is an error
matplotlib.use("Agg")
import pylab


def get_plot(line1: List[list], line2: List[list],
             y1_label: str, y2_label: str, title: str) -> pygame.Surface:
    """
    Plot a labelled graph of two lines which share an x-axis,
    and return the surface that it is plotted on.

    Preconditions:
        - len(line1) == 2 and len(line2) == 2
        - len(line1[0]) == len(line1[1])
        - len(line2[0]) == len(line2[1])
    """

    # Create pylab figure
    fig = pylab.figure(figsize=[800 / 85, 600 / 85],  # Inches. This is done so the final plot
                       # ends up being 800x600px.
                       dpi=85,  # Dots per inch
                       )

    # Create plot
    ax = fig.gca()

    # Create another plot on top of it, sharing the x-axis
    ax2 = ax.twinx()

    # Set title
    ax.set_title(title)

    # Set x axis label
    ax.set_xlabel('Year')

    # Set y axis labels
    ax.set_ylabel(y1_label)
    ax2.set_ylabel(y2_label)

    # Set colour for 2nd y axis label
    ax2.yaxis.label.set_color('r')

    # Plot the data
    ax.plot(line1[0], line1[1], 'k')
    ax2.plot(line2[0], line2[1], 'r')

    # Format tick labels
    ax.ticklabel_format(useOffset=False, style='plain')
    ax2.ticklabel_format(useOffset=False, style='plain')

    # Set axis 2 tick label color to be red.
    ax2.tick_params(color='r')

    # Draw the plot
    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()

    # Render the plot
    renderer = canvas.get_renderer()

    # Convert the plot into raw RGB data
    raw_data = renderer.tostring_rgb()

    size = canvas.get_width_height()

    # Create a new pygame.Surface from the raw data
    surf = pygame.image.fromstring(raw_data, size, "RGB")

    return surf


def get_data_points_wild_fires(wild_fire_dict: Dict[datetime.date, List[WildFire]], country: str) \
        -> List[list]:
    """Return the x and y coordinates of the wildfire data points
    Preconditions:
        - country == 'Canada' or country == 'America'
    """
    min_year = min([x.year for x in wild_fire_dict])
    max_year = max([x.year for x in wild_fire_dict])
    x_axis = list(range(min_year, max_year + 1))
    y_axis = [sum([len([fire for fire in wild_fire_dict[x] if fire.country == country])
                   for x in wild_fire_dict if x.year == y]) for y in x_axis]
    processed_data = remove_zero_data_points(x_axis, y_axis)
    return [processed_data[0], processed_data[1]]


def get_data_points_temp(temp_dict: Dict[datetime.date, TemperatureDeviance]) \
        -> List[list]:
    """Return the x and y coordinates of the temperature data points
    """
    min_year = min([x.year for x in temp_dict])
    x_axis = list(range(min_year, min_year + len(temp_dict)))
    y_axis = [temp_dict[datetime.date(y, 1, 1)].temperature_deviance for y in x_axis]
    processed_data = remove_zero_data_points(x_axis, y_axis)
    return [processed_data[0], processed_data[1]]


def get_data_points_carbon(carbon_dict: Dict[datetime.date, List[CarbonEmission]], i: int) \
        -> List[list]:
    """Return the x and y coordinates of the carbon data points. i=0 indicates Canada, i=1 indicates
     America

    Preconditions:
        - i == 0 or i == 1
    """
    min_year = min([x.year for x in carbon_dict])
    x_axis = list(range(min_year, min_year + len(carbon_dict)))
    y_axis = [carbon_dict[datetime.date(y, 1, 1)][i].emissions for y in x_axis]
    processed_data = remove_zero_data_points(x_axis, y_axis)
    return [processed_data[0], processed_data[1]]


def remove_zero_data_points(x_data: List[int], y_data: List[float]) -> Tuple[List[int],
                                                                             List[float]]:
    """Remove the zero y values and the associated x values from the dataset.
    Preconditions:
        - len(x_data) == len(y_data)
    """
    i = 0
    while 0 in y_data:
        if y_data[i] == 0:
            y_data.pop(i)
            x_data.pop(i)
            i -= 1
        i += 1

    return (x_data, y_data)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['datetime', 'typing', 'matplotlib', 'pylab', 'pygame',
                          'carbon_emissions', 'temperature_deviation',
                          'wildfires', 'matplotlib.backends.backend_agg', 'python_ta.contracts'],
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
