"""
A Python library for shows sun position
during the given day at the given location.
The library also contains function converts sun position into rotate vector
and function shows continent list, city list and helps user input city name.

Modified work Copyright 2023 Seowol Kim

"""

import ephem
import re
from cities import city_data
import math
import numpy as np
import fileseq

class City:
    """
    The City contains sun_position() as a float giving degrees and
    cal_rotate() convert to vector to apply directionalLight rotation parameter in maya.

    name (str) - City name to find sun position.
    date (str) - Date to find sun position. Year/Month/Day ex) 2023/01/25
    time (str) - Time to find sun position. Hours:Minutes:Seconds ex) 15:22:56
    """

    def __init__(self):
        self._name = None
        self._date = None
        self._time = None

    @property
    def name(self):
        """
        City Name to find sun position
        Returns: self._name
        """
        return self._name

    @name.setter
    def name(self, val):
        """
        City Name to find sun position.
        Check if a city in a list of cities.
        If not, return message and raise ValueError.
        Args:
            val: (str) entered city name

        Raise:
            ValueError: Invalid city name
        """
        city = val.title()
        if city in city_data.keys():
            self._name = city
        else:
            raise ValueError("Invalid City Name. Please Check if the City Name is in the list")

    @property
    def date(self):
        """
        Date to find sun position
        Returns: self._date
        """
        return self._date

    @date.setter
    def date(self, val):
        """
        Date to find sun position.
        Check a val to fit into regular expression.
        The Date value is all numeric equivalents to year-month-day and
        four-digit year, two-digit month, two-digit day
        Use an oblique stroke '/'  for separating digits.
        if date value mismatch, print message and raise ValueError
        Args:
            val: (str) entered date value

        Raise:
            ValueError: Invalid date
        """
        regex = r'\d{4}/\d{2}/\d{2}$'
        if bool(re.match(regex, val)):
            self._date = val
        else:
            raise ValueError("Invalid date! Input like #####/##/##")

    @property
    def time(self):
        """
        Time to find sun position
        Returns: self._time
        """
        return self._time

    @time.setter
    def time(self, val):
        """
        Time to find sun position.
        Check a val to fit into regular expression.
        The Time value is two-digit hour, two-digit minutes, two-digit seconds.
        Use a colon ':' for separating digits.
        if time value mismatch, print message and raise ValueError
        Args:
            val: (str) entered time value

        Raise:
            ValueError: Invalid time
        """
        regex = r'\d{2}:\d{2}:\d{2}$'
        if bool(re.match(regex, val)):
            self._time = val
        else:
            raise ValueError("Invalid time! Input like ##:##:##")

    def sun_position(self):
        """
        Shows sun position during the given day at the given location.
        A location on earth for which city positions are to be computed.
        Compute the positions of sun
        from a particular date entered and latitude and longitude on the Earth's surface that entered city name.
        Returns:
            azimuth (float)
                Azimuth as a float giving degrees
            altitude (float)
                Altitude as a float giving degrees
        """
        # Load the cities database and return a city.
        location = ephem.city(self.name)
        # A location on earth for which positions are to be computed.
        observer = ephem.Observer()
        observer.lon = location.lon
        observer.lat = location.lat
        observer.date = str(self.date) + ' ' + str(self.time)
        sun = ephem.Sun()
        sun.compute(observer)
        azimuth = math.degrees(sun.az)
        altitude = math.degrees(sun.alt)
        return azimuth, altitude

    def cal_rotate(self):
        """
        Converts azimuth, altitude as a float that results using self.sun_position(),
        returning rotate as a vector.
        Value can apply directionalLight rotation parameter in maya
        Returns:
            rotate (vector)
        """
        rotateX, rotateY = self.sun_position()
        rotate = np.array([rotateX, rotateY, 0])
        print(rotate)
        return rotate


def print_help():
    """
    This function shows continent list, city list and helps user input city name.
    return main() from time to time
    """
    print('''
   ++-----++-----++-----++
   Sun Position Caculation
   ++-----++-----++-----++\n
   This is little API that shows sun position during the given day at the given location \n
   - Get sun position, press -g
   - Show all cities list, press -a
   - Show continent list, press -l
   ''')
    action = input()
    if action == "-g":
        main()
    elif action == "-a":
        for key in city_data:
            print(key)
    elif action == "-l":
        while 1:
            print('''
            ++----++----++
            Continent List
            ++----++----++
            ●Africa
            ●America
            ●Asia
            ●Europe
            ●Oceania
            ''')
            continent = input("Select Continent : ")
            if continent.upper() in ["AFRICA", "AMERICA", "ASIA", "EUROPE", "OCEANIA"]:
                for key, value in city_data.items():
                    if value.lower() == continent.lower():
                        print("●", key)
                print("Select Action")
                print("- Go back select continent, press -c\n- Get Sun position, press -s\n- Quit, press any key")
                action = input()
                if action == "-c":
                    continue
                elif action == "-s":
                    main()
                    break
                else:
                    break
            else:
                print(" Invalid continent name ")
                continue
    else:
        print("Please input again!")
        print_help()


def main():
    sunpos = City()
    city = input("\ninput city : ")
    sunpos.name = city
    date = input("\ninput date :\nex) 2023/01/25\n")
    sunpos.date = date
    time = input("\ninput time :\nex) 15:22:56\n")
    sunpos.time = time
    sunpos.cal_rotate()


if __name__ == "__main__":
    main()
