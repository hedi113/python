from city import City
from typing import *
from cityIO import *

def writeCitiesToConsole(cities: List[City]) -> None:
    for city in cities:
        print(city)