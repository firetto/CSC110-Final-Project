"""
carbon_emissions.py:
Contains the CarbonEmission dataclass. Used to store the carbon emission data of a country for
a given year

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

from dataclasses import dataclass
import datetime


@dataclass
class CarbonEmission:
    """ A class that represents carbon emissions for a given year and country

    Instance Attributes:
        - country: The country in which the data is from
        - emissions: The carbon emissions in kilotons
        - year: The year in which the data is from. datetime.date in which the year is the year,
            and the month and day are placeholder values of 1

    Representation Invariants:
        - self.country == 'Canada' or self.country == 'America'
        - self.emissions > 0
        - 1960 <= self.year <= 2016

    Sample Usage:
    >>> emission1 = CarbonEmission(country='Canada', emissions=13490.893, \
        year=datetime.date(1960,1,1))
    """
    country: str
    emissions: float
    year: datetime.date


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['datetime', 'dataclasses', 'python_ta.contracts'],
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
