"""A file that contains the TemperatureDeviance dataclass

Implementation Note: year is an integer, however if needed we can make it a
datetime.date(year, 1, 1). The month and day are needed, so 1's can be placeholders.
"""

from dataclasses import dataclass


@dataclass
class TemperatureDeviance:
    """ A class that represents the temperature deviance in North America

    Instance Attributes:
        - temperature_deviance: The temperature deviance for a year
        - year: The year in which the data was recorded

    Representation Invariants:
        - isinstance(temperature_deviance, float)
        - 1910 <= year <= 2020

    Sample Usage:
    >>> temp_deviance = TemperatureDeviance(temperature_deviance=0.45, year=1950)
    """
    temperature_deviance: float
    year: int
