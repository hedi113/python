from city import City
from typing import *
from cityIO import *
from services import *

fileName = "data/adatok.txt"
cities: List[City] = readCitiesFromFile(fileName)

#Írjuk ki a képernyőre az össz adatot
writeCitiesToConsole(cities)