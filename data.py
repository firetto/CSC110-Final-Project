"""
data.py:
Contains the Data class used to get and store various dataclasses

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.

#TODO: Delete this
-----------------TO BE DELETED -------------------------------------------------------
Implementation notes:

- If we need the wild_fire data stored differently, it shouldn't be too
hard to fix

- For the final version, we probably want the __init__ method to populate the data.

- Currently uses two different methods for getting the fire data depending if its the Canada
or America set. Can probably find a way to combine both methods if needed.

-----------------TO BE DELETED -------------------------------------------------------

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
        - wild_fires: A mapping of the date a fire occurred, to a list of WildFire objects for each
            fire that occured at that date.
        - carbon_emissions: A mapping of the date (year only, month and day are placeholder values)
            to a list of CarbonEmission objects for that date. The list contain two elements, one
            object for Canada and America
        - temperature_deviation: A mapping of the date (year only, month and day are placeholder
            values) to a CarbonEmissions object for that date.

    Sample Usage:
    >>> my_data = Data()
    """

    wild_fires: Dict[datetime.date, List[WildFire]]
    carbon_emissions: Dict[datetime.date, List[CarbonEmission]]
    temperature_deviation: Dict[datetime.date, TemperatureDeviance]

    def __init__(self) -> None:
        self.wild_fires = {}
        self.carbon_emissions = {}
        self.temperature_deviation = {}

    def get_wild_fires_canada(self, location: str) -> None:
        """Mutates the wild_fires local variable to include the wild_fire_data from canada

        #TODO: DELETE THIS
        Implementation Note:
        - If we do make the __init__ method populate right away, we can make this function
        return the dictionary instead of mutating, and then call the function in the __init__.

        Preconditions:
            - location is the location of the 'Canadian_Wildfire_Data.csv' file.
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

        #TODO: DELETE THIS
        Implementation Note:
        - If we do make the __init__ method populate right away, we can make this function
        return the dictionary instead of mutating, and then call the function in the __init__.

        Preconditions:
            - location is the location of the 'USA_Fire_Data.csv' file.
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

    def get_carbon_emission_data(self, location: str) -> None:
        """Mutates the carbon_emissions local variable to include the carbon emission data.

        #TODO: DELETE THIS
        Implementation Note:
        - If we do make the __init__ method populate right away, we can make this function
        return the dictionary instead of mutating, and then call the function in the __init__.

        Preconditions:
            - location is the location of the 'CO2 Data.csv' file.
        """

        with open(location) as file:
            reader = csv.reader(file)

            # Remove the first 4 lines from the reader, so they are not included in the data.
            line_1 = next(reader)
            line_2 = next(reader)
            line_3 = next(reader)
            line_4 = next(reader)

            headers = next(reader)
            country_index = find_index('Country Name', headers)
            print(country_index)
            current_index = starting_index = find_index('1960', headers)

            # Get only the data for Canada and the United States
            data = [row for row in reader if row[country_index] == 'Canada'
                    or row[country_index] == 'United States']

            for entry in data:
                country = entry[country_index]
                if country == 'United States':
                    country = 'America'  # Used to keep data consistent

                for year in range(1960, 2017):  # 2017 is not included
                    # Month and Day are placeholder values.
                    date = datetime.date(year, 1, 1)

                    carbon_emissions = float(entry[current_index])
                    carbon_data = CarbonEmission(country, carbon_emissions, date)

                    current_index += 1

                    if date not in self.carbon_emissions:
                        self.carbon_emissions[date] = [carbon_data]
                    else:
                        self.carbon_emissions[date].append(carbon_data)

                current_index = starting_index

    def get_temperature_deviance_data(self, location: str) -> None:
        """Mutates the temperature_deviation local variable to include the temperature
        deviation data.

        #TODO: DELETE THIS
        Implementation Note:
        - If we do make the __init__ method populate right away, we can make this function
        return the dictionary instead of mutating, and then call the function in the __init__.

        Preconditions:
            - location is the location of the 'Temperature_Deviation_Data.csv' file.
        """

        with open(location) as file:
            reader = csv.reader(file)

            # Remove the first 4 lines from the reader, so they are not included in the data.
            line_1 = next(reader)
            line_2 = next(reader)
            line_3 = next(reader)
            line_4 = next(reader)

            headers = next(reader)

            data = [row for row in reader]

            for entry in data:
                # Month and Day are placeholder values.
                date = datetime.date(int(entry[0]), 1, 1)
                value = float(entry[1])

                temperature_deviance_data = TemperatureDeviance(value, date)

                self.temperature_deviation[date] = temperature_deviance_data

    def write_canadian_wild_fire_data(self, location: str) -> None:
        """ Write the canadian wild fire data to a csv file named location. This removes all
        the redundant data from the original CSV file.

        Preconditions:
            - '.csv' in location
        """
        with open(location, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            headers = ['YEAR', 'MONTH', 'DAY', 'LATITUDE', 'LONGITUDE']
            writer.writerow(headers)

            for date in self.wild_fires:
                fires = [fire for fire in self.wild_fires[date] if fire.country == 'Canada']
                for fire in fires:
                    year = fire.date.year
                    month = fire.date.month
                    day = fire.date.day
                    latitude = fire.location[0]
                    longitude = fire.location[1]
                    row = [year, month, day, latitude, longitude]
                    writer.writerow(row)

    def write_american_wild_fire_data(self, location: str) -> None:
        """ Write the american wild fire data to a csv file named location. This removes all
        the redundant data from the original CSV file.

        Preconditions:
            - '.csv' in location
        """
        with open(location, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            headers = ['DISCOVERY_DATE', 'LATITUDE', 'LONGITUDE']
            writer.writerow(headers)

            for date in self.wild_fires:
                fires = [fire for fire in self.wild_fires[date] if fire.country == 'America']
                for fire in fires:
                    year = fire.date.year
                    month = fire.date.month
                    day = fire.date.day
                    date = f'{year}-{month}-{day}'
                    latitude = fire.location[0]
                    longitude = fire.location[1]
                    row = [date, latitude, longitude]
                    writer.writerow(row)


def find_index(target: str, lst: list) -> int:
    """Return the index of the target in lst

    Preconditions:
        - target in lst
    """
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
