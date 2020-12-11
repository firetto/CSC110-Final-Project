"""
firemap_update.py

Contains the FireMapUpdate class,
which accesses the wildfire data, plotting it on the FireMap, and animating it.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

from data import Data
from firemap import FireMap


class FireMapUpdate:
    """
    Class containing functions for updating the fire map by using the wildfire data.
    """

    # Private Instance Attributes:
    # - _data: Data class instance containing the wildfire, carbon, and temperature deviance data
    # - _map: FireMap class instance that will be used to plot wildfire data onto.
    _data: Data
    _map: FireMap

    def __init(self, data: Data, firemap: FireMap) -> None:
        """Initialize instances"""
        _data = data
        _map = firemap
