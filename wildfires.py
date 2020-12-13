"""
wildfires.py:
Contains the WildFire dataclass. Used to store information about wildfires such as their country
of origin, location, and date of occurrence.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

import datetime
from dataclasses import dataclass
from typing import Tuple


@dataclass
class WildFire:
    """ A class that represents data for a wildfire within Canada or America

    Instance Attributes:
        - country: The country where the fire occurred.
        - location: The location of the fire represented as (latitude, longitude)
        - date: The date in which the fire took place.

    Representation Invariants:
        - self.country == 'Canada' or self.country == 'America'
        - -90 <= self.location[0] <= 90
        - -180 <= self.location[1] <= 180

    Sample Usage:
    >>> wildfire_1 = WildFire(country='Canada', location=(59.963, -128.172),\
     date=datetime.date(1953,5,26))
    """
    country: str
    location: Tuple[float, float]
    date: datetime.date


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['datetime', 'dataclasses', 'python_ta.contracts', 'typing'],
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
