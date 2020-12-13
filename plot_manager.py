"""
plot_manager.py

Contains the PlotManager class, which handles drawing plots onto the window.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""
from typing import List, Tuple
import pygame
from window import Window
from data import Data
import plot


class PlotManager:
    """
    Class responsible for drawing the plots onto the window.
    """

    # Private Instance Attributes:
    # - _window: Window instance.
    # - _data: Data instance, containing all of the data information.
    # - _plot_surface: pygame.Surface that will contain the plot.
    # - _plot_displayed: which plot is being displayed. Possible values include:
    #                    "none": no plot is being displayed
    #                    "canada_vs_carbon": Canadian wildfires vs Canadian Carbon emissions
    #                    "america_vs_carbon": American wildfires vs American Carbon emissions
    #                    "canada_vs_temp": Canadian wildfires vs Temperature Deviance
    #                    "america_vs_temp": American wildfires vs Temperature Deviance
    # - _data_points_canada_wildfire: Contains the Canadian wildfire data points, which will be
    #                                 used to plot the Canadian wildfire data.
    # - _data_points_america_wildfire: Contains the American wildfire data points, which will be
    #                                 used to plot the American wildfire data.
    # - _data_points_canada_carbon: Contains the Canadian carbon data points, which will be
    #                                 used to plot the Canadian CO2 emissions data.
    # - _data_points_america_carbon: Contains the American carbon data points, which will be
    #                                used to plot the American CO2 emissions data.
    # - _data_points_temp_deviance: Contains the temperature deviance data points, which will be
    #                                used to plot the temperature deviance data.
    # - _PLOT_POSITION: Position of the top left corner of the plot when drawn.
    # Private Representation Invariants:
    # - self._plot_displayed in {"none", "canada_vs_carbon", "america_vs_carbon",
    #                            "canada_vs_temp", "america_vs_temp"}

    _window: Window
    _data: Data
    _plot_surface: pygame.Surface
    _plot_displayed: str
    _data_points_canada_wildfire: Tuple[List[int], List[int]]
    _data_points_america_wildfire: Tuple[List[int], List[int]]
    _data_points_canada_carbon: Tuple[List[int], List[int]]
    _data_points_america_carbon: Tuple[List[int], List[int]]
    _data_points_temp_deviance: Tuple[List[int], List[int]]
    _PLOT_POSITION: Tuple[int, int] = (50, 10)

    def __init__(self, window: Window, data: Data) -> None:
        """
        Initialize instance attributes.
        """
        self._window = window
        self._plot_displayed = "none"
        self._data = data
        self._setup_data_points()

    def _setup_data_points(self) -> None:
        """
        Set up all of the data points by reading the data.
        """
        self._data_points_canada_wildfire = \
            plot.get_data_points_wild_fires(self._data.wild_fires, 'Canada')
        self._data_points_america_wildfire = \
            plot.get_data_points_wild_fires(self._data.wild_fires, 'America')
        self._data_points_canada_carbon = \
            plot.get_data_points_carbon(self._data.carbon_emissions, 0)
        self._data_points_america_carbon = \
            plot.get_data_points_carbon(self._data.carbon_emissions, 1)
        self._data_points_temp_deviance = \
            plot.get_data_points_temp(self._data.temperature_deviation)

    def set_plot(self, new_plot: str) -> None:
        """
        Switch the plot displayed to the one corresponding to parameter 'new_plot'.

        Preconditions:
         - plot in {"none", "canada_vs_carbon", "america_vs_carbon",
                    "canada_vs_temp", "america_vs_temp"}
        """

        self._plot_displayed = new_plot

        if new_plot == "canada_vs_carbon":
            self._plot_surface = \
                plot.get_plot(self._data_points_canada_wildfire[0],
                              self._data_points_canada_wildfire[1],
                              self._data_points_canada_carbon[0],
                              self._data_points_canada_carbon[1],
                              'Number of Wildfires', 'Carbon Dioxide Emissions (kT)',
                              "Canadian Wildfires vs Canadian CO2 Emissions")
        elif new_plot == "america_vs_carbon":
            self._plot_surface = \
                plot.get_plot(self._data_points_america_wildfire[0],
                              self._data_points_america_wildfire[1],
                              self._data_points_america_carbon[0],
                              self._data_points_america_carbon[1],
                              'Number of Wildfires', 'Carbon Dioxide Emissions (kT)',
                              "USA Wildfires vs American CO2 Emissions")
        elif new_plot == "canada_vs_temp":
            self._plot_surface = \
                plot.get_plot(self._data_points_canada_wildfire[0],
                              self._data_points_canada_wildfire[1],
                              self._data_points_temp_deviance[0],
                              self._data_points_temp_deviance[1],
                              'Number of Wildfires', 'Temperature Deviance (°C)',
                              "Canadian Wildfires vs North American Temperature Deviance")
        elif new_plot == "america_vs_temp":
            self._plot_surface = \
                plot.get_plot(self._data_points_america_wildfire[0],
                              self._data_points_america_wildfire[1],
                              self._data_points_temp_deviance[0],
                              self._data_points_temp_deviance[1],
                              'Number of Wildfires', 'Temperature Deviance (°C)',
                              "USA Wildfires vs North American Temperature Deviance")

    def is_plot_displayed(self) -> bool:
        """
        Return whether a plot is currently being displayed.
        """
        return self._plot_displayed != "none"

    def draw_plot(self) -> None:
        """
        Draw plot, if one is supposed to be displayed.
        """

        if not self.is_plot_displayed():
            return

        self._window.draw_to_screen(self._plot_surface, self._PLOT_POSITION)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['window', 'typing', 'data', 'plot', 'pygame', 'python_ta.contracts'],
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
