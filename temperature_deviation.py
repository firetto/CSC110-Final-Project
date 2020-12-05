"""
temperature_deviation.py:
Contains the TemperatureDeviance dataclass. Used to store the temperature deviance for a given
year.

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

from dataclasses import dataclass
import datetime


@dataclass
class TemperatureDeviance:
    """ A class that represents the temperature deviance in North America

    Instance Attributes:
        - temperature_deviance: The temperature deviance for a year
        - year: The year in which the data is from. Datetime.date in which the year is the year,
            and the month and day are placeholder values, 1

    Representation Invariants:
        - isinstance(temperature_deviance, float)
        - 1910 <= year <= 2020

    Sample Usage:
    >>> temp_deviance = TemperatureDeviance(temperature_deviance=0.45, year=datetime.date(1950,1,1))
    """
    temperature_deviance: float
    year: datetime.date

