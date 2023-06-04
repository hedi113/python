from city import City
from typing import *
from cityIO import *

def writeCitiesToConsole(cities: List[City]) -> None:
    for city in cities:
        print(city)

def determineCountyRights(cities: List[City]) -> List[City]:
    citiesWithCountyRights: List[City] = []

    for city in cities:
        if(city.population > 50000):
            citiesWithCountyRights.append(city)
    
    return citiesWithCountyRights

def determinePopulation(cities: List[City]) -> List[City]:
    citiesPopulation: List[City] = []

    for city in cities:
        if(city.population > 50000 and city.population < 100000):
            citiesPopulation.append(city)
    
    return citiesPopulation

def determineArea(cities: List[City]) -> List[City]:
    citiesArea: List[City] = []

    for city in cities:
        if(city.area > 200):
            citiesArea.append(city)
    
    return citiesArea

def findSpecData(cities: List[City], specific: str) -> List[City]:
    specData: List[City] = []

    for city in cities:
        if(city.countyName == specific):
            specData.append(city)

    return specData