from city import City
from typing import *
from cityIO import *
from services import *

fileName = "data/adatok.txt"
cities: List[City] = readCitiesFromFile(fileName)

#Írjuk ki a képernyőre az össz adatot
writeCitiesToConsole(cities)

#Keressük ki a megyeszékhely megyei jogú városokat és mentsük el a megyejoguvarosok.txt állományba
citiesWithCountyRights: List[City] = determineCountyRights(cities)
writeCitiesToFile("megyejoguvarosok.txt", citiesWithCountyRights)

#Az nepesseg.txt állományba mentsük el azokat a településeket és a hozzájuk tartozó adatokat, ahol a népesség 50.000 és 100.000 közt van
citiesPopulation: List[City] = determinePopulation(cities)
writeCitiesToFile("nepesseg.txt", citiesPopulation)

#Keressük ki azokat a településeket, melyek területei meghaladják az 200-at  és a  nagyteruletek.txt állományba mentsük el.
citiesArea: list[City] = determineArea(cities)
writeCitiesToFile("nagyteruletek.txt", citiesArea)

#Keressük ki Békés megye össz települését és a bekes.txt állományba mentsük el.
specData: List[City] = findSpecData(cities, "B�k�s")
writeCitiesToFile("bekes.txt", specData)

 #megyeterületek.txt állományba mentsük el a megye nevét és területének nagyságát.
writeCountyAreasToFile("megyeteruletek.txt", cities)