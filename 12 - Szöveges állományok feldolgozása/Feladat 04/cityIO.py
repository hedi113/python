from city import City
import os
from typing import *
from io import open

def readCitiesFromFile(fileName: str) -> List[City]:
    cities: List[City] = []
    city: City = None

    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try: 
        with open(fileFullPath, encoding='utf-8', mode='r') as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split('\t')

                city = City()
                city.name = data[0]
                city.type = data[1]
                city.countyName = data[2]
                city.jaras = data[3]
                city.microRegion = data[4]
                city.population = int(data[5])
                city.area = float(data[6])

                cities.append(city)
        return cities
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []

def writeCitiesToFile(fileName: str, cities: List[City]) -> None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding='utf-8', mode='w') as file:
            for city in cities:
                file.write(f"{city.name}\t{city.type}\t{city.area}\t{city.population}\t{city.countyName}\n")

    except FileNotFoundError as ex:
        print(f"{ex.filename} írásakor hiba lépett fel!")

def writeCountyAreasToFile(fileName: str, cities: List[City]) -> None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding='utf-8', mode='w') as file:
            for city in cities:
                file.write(f"{city.name} - {city.area}\n")

    except FileNotFoundError as ex:
        print(f"{ex.filename} írásakor hiba lépett fel!")