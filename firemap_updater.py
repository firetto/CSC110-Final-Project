"""
firemap_updater.py

Contains the FireMapUpdater class,
which accesses the wildfire data, plotting it on the FireMap, and animating it.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

from data import Data
from firemap import FireMap
from wildfires import WildFire
import datetime


class FireMapUpdater:
    """
    Class containing functions for updating the fire map by using the wildfire data.
    """

    # Private Instance Attributes:
    # - _data: Data class instance containing the wildfire, carbon, and temperature deviance data
    # - _map: FireMap class instance that will be used to plot wildfire data onto.
    # - _date: datetime.date of the current day that is being examined in the data.
    _data: Data
    _map: FireMap
    _date: datetime.date

    def __init__(self, data: Data, firemap: FireMap) -> None:
        """Initialize instances"""
        self._data = data
        self._map = firemap
        self._date = data.find_first_date()

        # TEST:
        self._draw_wildfire_dots()

    def _draw_wildfire_dots(self) -> bool:
        """
        Draw the corresponding date's wildfire dots onto the firemap,
        return whether there are any dots to draw (that is, whether the number of wildfires
        for this day is nonzero).
        """
        if (self._date not in self._data.wild_fires) or len(self._data.wild_fires[self._date]) < 1:
            return False

        for fire in self._data.wild_fires[self._date]:
            self._map.add_dot(fire.location)

        return True
