"""
data.py:
Contains the Data class used to get and store various dataclasses

CSC110 Final Project by Anatoly Zavyalov, Austin Blackman, Elliot Schrider.
"""

from typing import Dict, List
import datetime
import csv
from wildfires import WildFire
from carbon_emissions import CarbonEmission
from temperature_deviation import TemperatureDeviance


class Data:
    """A Class used to handle various types of data

    Instance Attributes:
        - wild_fires: A mapping of the date a fire occurred, to a list of WildFire objects for each
            fire that occurred at that date.
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
        """
        Initialize empty dictionaries.
        """
        self.wild_fires = {}
        self.carbon_emissions = {}
        self.temperature_deviation = {}
        self.get_wild_fires_canada('canada_wildfire_data.csv')
        self.get_wild_fires_america('america_wildfire_data.csv')
        self.get_carbon_emission_data('carbon_data.csv')
        self.get_temperature_deviance_data('temperature_deviance_data.csv')

    def get_wild_fires_canada(self, location: str) -> None:
        """Mutates the wild_fires local variable to include the wild_fire_data from canada

        Preconditions:
            - location is the location of the 'canada_wildfire_data.csv file.
        """

        with open(location, encoding="utf8") as file:
            reader = csv.reader(file)

            # Gets the headers of the list, and moves the reader so the header is not included
            # in the data.
            headers = next(reader)

            latitude_index = headers.index('LATITUDE')
            longitude_index = headers.index('LONGITUDE')
            year_index = headers.index('YEAR')
            month_index = headers.index('MONTH')
            day_index = headers.index('DAY')

            for row in reader:

                if int(row[year_index]) != 0 and int(row[month_index]) != 0 \
                        and int(row[day_index]) != 0:
                    location = (float(row[latitude_index]), float(row[longitude_index]))
                    date = datetime.date(int(row[year_index]), int(row[month_index]),
                                         int(row[day_index]))

                    fire = WildFire('Canada', location, date)
                    self._add_fire(date, fire)

    def get_wild_fires_america(self, location: str) -> None:
        """Mutates the wild_fires local variable to include the wild_fire_data from america

        Preconditions:
            - location is the location of the 'america_wildfire_data.csv' file.
        """

        with open(location) as file:
            reader = csv.reader(file)

            # Gets the headers of the list, and moves the reader so the header is not included
            # in the data.
            headers = next(reader)

            latitude_index = headers.index('LATITUDE')
            longitude_index = headers.index('LONGITUDE')
            date_index = headers.index('DISCOVERY_DATE')

            for row in reader:
                location = (float(row[latitude_index]), float(row[longitude_index]))

                # Stored in the data as "year-month-day"
                date_list = row[date_index].split('-')

                date = datetime.date(year=int(date_list[0]),
                                     month=int(date_list[1]),
                                     day=int(date_list[2]))

                fire = WildFire('America', location, date)
                self._add_fire(date, fire)

    def get_carbon_emission_data(self, location: str) -> None:
        """Mutates the carbon_emissions local variable to include the carbon emission data.

        Preconditions:
            - location is the location of the 'carbon_data.csv' file.
        """

        with open(location) as file:
            reader = csv.reader(file)

            # Remove the first 4 lines from the reader, so they are not included in the data.
            for _ in range(4):
                next(reader)

            headers = next(reader)
            country_index = headers.index('Country Name')
            current_index = starting_index = headers.index('1960')

            # Get only the data for Canada and the United States
            data = [row for row in reader if row[country_index] == 'Canada'
                    or row[country_index] == 'United States']

            for entry in data:
                country = entry[country_index]
                if country == 'United States':
                    country = 'America'  # Used to keep data consistent

                for year in range(1960, 2017):  # 2017 is not included
                    # Month and Day are placeholder values.

                    carbon_emissions = float(entry[current_index])
                    carbon_data = CarbonEmission(country, carbon_emissions,
                                                 datetime.date(year, 1, 1))

                    current_index += 1

                    if datetime.date(year, 1, 1) in self.carbon_emissions:
                        self.carbon_emissions[datetime.date(year, 1, 1)].append(carbon_data)

                    else:
                        self.carbon_emissions[datetime.date(year, 1, 1)] = [carbon_data]

                current_index = starting_index

    def get_temperature_deviance_data(self, location: str) -> None:
        """Mutates the temperature_deviation local variable to include the temperature
        deviation data.

        Preconditions:
            - location is the location of the 'temperature_deviance_data.csv' file.
        """

        with open(location) as file:
            reader = csv.reader(file)

            # Remove the first 4 lines from the reader, so they are not included in the data.
            for _ in range(4):
                next(reader)

            # Remove the headers
            _ = next(reader)

            for entry in reader:
                # Month and Day are placeholder values.
                date = datetime.date(int(entry[0]), 1, 1)
                value = float(entry[1])

                temperature_deviance_data = TemperatureDeviance(value, date)

                self.temperature_deviation[date] = temperature_deviance_data

    def write_canadian_wild_fire_data(self, location: str) -> None:
        """Write the canadian wild fire data to a csv file named location. This removes all
        the redundant data from the original CSV file.

        Preconditions:
            - '.csv' in location
        """

        with open(location, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            headers = ['YEAR', 'MONTH', 'DAY', 'LATITUDE', 'LONGITUDE']
            writer.writerow(headers)

            for date in self.wild_fires:
                for fire in self.wild_fires[date]:
                    if fire.country == 'Canada':
                        year, month, day = fire.date.year, fire.date.month, fire.date.day
                        latitude, longitude = fire.location
                        row = [year, month, day, latitude, longitude]
                        writer.writerow(row)

    def write_american_wild_fire_data(self, location: str) -> None:
        """Write the american wild fire data to a csv file named location. This removes all
        the redundant data from the original CSV file.

        Preconditions:
            - '.csv' in location
        """

        with open(location, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            headers = ['DISCOVERY_DATE', 'LATITUDE', 'LONGITUDE']
            writer.writerow(headers)

            for date in self.wild_fires:
                for fire in self.wild_fires[date]:
                    if fire.country == 'America':
                        year, month, day = fire.date.year, fire.date.month, fire.date.day
                        latitude, longitude = fire.location
                        date = f'{year}-{month}-{day}'

                        row = [date, latitude, longitude]
                        writer.writerow(row)

    def write_carbon_emission_data(self, location: str) -> None:
        """Write the carbon emission data to a csv file named location. This removes all the
        redundant data from the original CSV file.

        Preconditions:
            - '.csv' in location
        """

        with open(location, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            headers = ['Country Name']

            for i in range(1960, 2017):  # 2017 is not included
                headers.append(i)

            # Write 4 blank rows at the top of the csv file to be consistent with the original
            # CSV file
            for _ in range(0, 4):
                writer.writerow([])

            writer.writerow(headers)

            american_emissions = ['United States']
            canadian_emissions = ['Canada']

            for i in range(1960, 2017):
                emissions = self.carbon_emissions[datetime.date(i, 1, 1)]
                for emission in emissions:
                    if emission.country == 'America':
                        american_emissions.append(emission.emissions)
                    else:
                        canadian_emissions.append(emission.emissions)

            writer.writerow(canadian_emissions)
            writer.writerow(american_emissions)

    def write_temperature_deviance_data(self, location: str) -> None:
        """Write the temperature deviance data to a csv file named location. This removes all the
        redundant data from the original CSV file

        Preconditions:
            - '.csv' in location

        """

        with open(location, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            headers = ['Year', 'Value']

            # Write 4 blank rows at the top of the csv file to be consistent with the original
            # CSV file
            for _ in range(0, 4):
                writer.writerow([])

            writer.writerow(headers)

            for date in self.temperature_deviation:
                year = date.year
                value = self.temperature_deviation[date].temperature_deviance
                writer.writerow([year, value])

    def _add_fire(self, date: datetime.date, fire: WildFire) -> None:
        """Mutate the wild_fires dictionary to include the fire that corresponds to date. If the
        date already exists within the dictionary append the fire, otherwise, create a new key
        of date with the value of fire.

        Only accept fires that occurred in or after 1950.

        This function is called within get_wild_fires_canada and get_wild_fires_america.
        """

        if date >= datetime.date(1950, 1, 1):
            if date in self.wild_fires:
                self.wild_fires[date].append(fire)
            else:
                self.wild_fires[date] = [fire]

    def find_first_date(self) -> datetime.date:
        """
        Return the first date entry that appears in self.wild_fires.
        """
        return min(self.wild_fires)

    def find_last_date(self) -> datetime.date:
        """Return the last date entry that appears in self.wild_fires."""
        return max(self.wild_fires)


if __name__ == '__main__':

    # NOTE THE PYTA CALLS IN THE CONSOLE WILL TAKE A LONG TIME TO FINISH. IT IS CHECKING THE
    # CONTRACTS OF EVERY ENTRY FROM THE SAMPLE CALL ON LINE 29.
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['datetime', 'csv', 'python_ta.contracts', 'wildfires',
                          'carbon_emissions', 'temperature_deviation'],
        # the names (strs) of imported modules
        'allowed-io': ['get_wild_fires_canada', 'get_wild_fires_america',
                       'get_carbon_emission_data', 'get_temperature_deviance_data',
                       'write_canadian_wild_fire_data', 'write_american_wild_fire_data',
                       'write_carbon_emission_data', 'write_temperature_deviance_data'],
        # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
