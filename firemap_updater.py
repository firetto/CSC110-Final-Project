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
    # - _day_increment: How many days to increment for every update
    # - _update_delay: Number of milliseconds to wait before updating the fire map
    # - _time_delta_so_far: Number of milliseconds elapsed since the last update
    # - _animating: whether the timelapse is animating, and whether the map should be updated.
    # - _last_date: The last date of the timelapse
    # - _first_date: The last date of the timelapse
    # Private Representation Invariants:
    # - self._day_increment > 0
    # - self._update_delay > 0
    _data: Data
    _map: FireMap
    _date: datetime.date
    _day_increment: int
    _update_delay: float
    _time_delta_so_far: float
    _animating: bool

    _last_date: datetime.date
    _first_date: datetime.date

    def __init__(self, data: Data, firemap: FireMap) -> None:
        """Initialize instances"""
        self._data = data
        self._map = firemap

        self._first_date = data.find_first_date()
        self._last_date = data.find_last_date()
        self._date = self._first_date

        self._day_increment = 1
        self._update_delay = 10
        self._time_delta_so_far = 0

        self._animating = True

    def _draw_wildfire_dots(self) -> bool:
        """
        Draw the corresponding date's wildfire dots onto the firemap,
        return whether there are any dots to draw (that is, whether the number of wildfires
        for this day is nonzero).
        """
        if (self._date not in self._data.wild_fires) \
                or len(self._data.wild_fires[self._date]) < 1:
            return False

        for fire in self._data.wild_fires[self._date]:
            self._map.add_dot(fire.location)

        return True

    def _increment_date(self) -> None:
        """Increment the date by self._day_increment."""
        self._date += datetime.timedelta(days=self._day_increment)

        # Check if the date is later than the last date of the timelapse. If so,
        # Stop the timelapse and set date to the last date.
        if self._date > self._last_date:
            self._date = self._last_date
            self.stop_animation()

    def _update_map(self) -> None:
        """Update the map by incrementing the date and redrawing the dots."""

        self._increment_date()

        self._map.set_map_date_text(str(self._date))

        self._map.clear_dots()
        self._draw_wildfire_dots()

    def update_delta(self, delta: float) -> bool:
        """
        Increment self._time_delta_so_far by delta, and, if the accumulator delta
        is greater than the time interval before updating the map, update the map as well.

        Return whether the map was updated.

        Preconditions:
         - delta > 0
        """

        if not self._animating:
            return False

        self._time_delta_so_far += delta

        if self._time_delta_so_far >= self._update_delay:
            self._time_delta_so_far = 0

            # Update the map here
            self._update_map()

            return True
        else:
            return False

    def start_animation(self) -> None:
        """Start the timelapse."""
        self._animating = True

    def stop_animation(self) -> None:
        """Stop the timelapse."""
        self._animating = False

    def toggle_animation(self) -> None:
        """Toggle the state of self._animating."""
        self._animating = not self._animating
