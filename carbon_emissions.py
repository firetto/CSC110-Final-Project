"""A file that contains the CarbonEmission dataclass
"""

import datetime
from dataclasses import dataclass
import datetime


@dataclass
class CarbonEmission:
    """ A class that represents carbon emissions for a given year and country

    Instance Attributes:
        - country: The country in which the data is from
        - emissions: The carbon emissions in kilotons
        - year: The year in which the data is from. Datetime.date in which the year is the year,
            and the month and day are placeholder values, 1

    Representation Invariants:
        - self.country == 'Canada' or self.country == 'America'
        - self.emissions > 0
        - 1960 <= self.year <= 2016

    Sample Usage:
    >>> emission1 = CarbonEmission(country='Canda', emissions=13490.893, \
        year=datetime.date(1960,1,1))
    """
    country: str
    emissions: float
    year: datetime.date
