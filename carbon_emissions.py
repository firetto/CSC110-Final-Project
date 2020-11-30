"""A file that contains the CarbonEmission dataclass

Implementation Note: year is an integer, however if needed we can make it a
datetime.date(year, 1, 1). The month and day are needed, so 1's can be placeholders.
"""

import datetime
from dataclasses import dataclass


@dataclass
class CarbonEmission:
    """ A class that represents carbon emissions for a given year and country

    Instance Attributes:
        - country: The country in which the data is from
        - emissions: The carbon emissions in kilotons
        - year: The year in which the data is from

    Representation Invariants:
        - self.country == 'Canada' or self.country == 'America'
        - self.emissions > 0
        - 1960 <= self.year <= 2016

    Sample Usage:
    >>> emission1 = CarbonEmission(country='Canda', emissions=13490.893, year=1960)
    """
    country: str
    emissions: float
    year: int
