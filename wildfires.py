"""A file that contains the Wildfire dataclass

Implementation Note: If needed we can add more information about the fires.
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
