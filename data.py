"""A file that contains the class Data which stores data of various other data types

Implementation notes:

- If we need the wild_fire data stored differently, it shouldn't be too
hard to fix

- For the final version, we probably want the __init__ method to populate the data.

- Currently uses two different methods for getting the fire data depending if its the Canada
or America set. Can probably find a way to combine both methods if needed.

"""

from typing import Dict, List
import datetime
from wildfires import WildFire
from carbon_emissions import CarbonEmission
from temperature_deviation import TemperatureDeviance
import csv


class Data:
    """ A Class used to handle various types of data

    Instance Attributes:
        - wild_fires: A mapping of the date a fire occurred, to a WildFire object.
        - carbon_emissions: A mapping of the date (year only, month and day are placeholder values)
            to a CarbonEmissions object for that date.
        - temperature_deviation: A mapping of the date (year only, month and day are placeholder
            values) to a CarbonEmissions object for that date.

    Sample Usage:
    >>> my_data = Data()
    """

    wild_fires: Dict[datetime.date, List[WildFire]]
    carbon_emissions: Dict[datetime.date, List[CarbonEmission]]
    temperature_deviation: Dict[datetime.date, List[TemperatureDeviance]]

    def __init__(self) -> None:
        self.wild_fires = {}
        self.carbon_emissions = {}
        self.temperature_deviation = {}

    def get_wild_fires_canada(self, location: str) -> None:
        """Mutates the wild_fires local variable to include the wild_fire_data from canada

        Implementation Note:
        - If we do make the __init__ method populate right away, we can make this function
        return the dictionary instead of mutating, and then call the function in the __init__.

        Preconditions:
            - location is the location of the wild_fire data csv file
        """

        with open(location, encoding="utf8") as file:
            reader = csv.reader(file)

            # Gets the headers of the list, and moves the reader so the header is not included
            # in the data.
            headers = next(reader)

            latitude_index = find_index('LATITUDE', headers)
            longitude_index = find_index('LONGITUDE', headers)
            year_index = find_index('YEAR', headers)
            month_index = find_index('MONTH', headers)
            day_index = find_index('DAY', headers)

            data = [row for row in reader]

            for row in data:
                if int(row[year_index]) != 0 and int(row[month_index]) != 0 \
                        and int(row[day_index]) != 0:
                    location = (float(row[latitude_index]), float(row[longitude_index]))
                    date = datetime.date(int(row[year_index]), int(row[month_index]),
                                         int(row[day_index]))

                    fire = WildFire('Canada', location, date)

                    # If the current date does not have a fire, add it. Else append it
                    if date not in self.wild_fires:
                        self.wild_fires[date] = [fire]
                    else:
                        self.wild_fires[date].append(fire)

    def get_wild_fires_america(self, location: str) -> None:
        """Mutates the wild_fires local variable to include the wild_fire_data from america

        Implementation Note:
        - If we do make the __init__ method populate right away, we can make this function
        return the dictionary instead of mutating, and then call the function in the __init__.

        Preconditions:
            - location is the location of the wild_fire data csv file
        """

        with open(location) as file:
            reader = csv.reader(file)

            # Gets the headers of the list, and moves the reader so the header is not included
            # in the data.
            headers = next(reader)

            latitude_index = find_index('LATITUDE', headers)
            longitude_index = find_index('LONGITUDE', headers)
            date_index = find_index('DISCOVERY_DATE', headers)

            data = [row for row in reader]

            for row in data:
                location = (float(row[latitude_index]), float(row[longitude_index]))
                date_list = row[date_index].split('-')  # Stored in the data as "year-month-day"
                date = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
                fire = WildFire('America', location, date)

                # If the current date does not have a fire, add it. Else append it
                if date not in self.wild_fires:
                    self.wild_fires[date] = [fire]
                else:
                    self.wild_fires[date].append(fire)


def find_index(target: str, lst: list) -> int:
    """Return the index of the target in lst

    Preconditions:
        - target in lst
    """
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
