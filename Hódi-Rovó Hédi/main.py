from motorcycle import Motorcycle
from typing import *
from motorcycleIO import *
from services import *

fileName: str = "data/adatok.txt"
motorcycles: List[Motorcycle] = readMotorcycleFromFile(fileName)

writeMotorcycleToConsole(motorcycles)
#a) feladat
motorcycleCount = howManyMotorcycles(motorcycles)
writeThingToConsole(f"{motorcycleCount} motorkerékpár adatait dolgozzuk fel.")
#b) feladat
after2000 = madeAfter2000(motorcycles)
countAfter2000 = howManyMotorcycles(after2000)
writeThingToConsole(f"{countAfter2000} motorkerékpárt gyártottak 2000 után")
#c) feladat
priceAvarage = getPriceAvarage(motorcycles)
writeThingToConsole(f"{priceAvarage:1.2f}EUR a motorkerékpárok árainak átlaga")
#d) feladat
oldestMotorcycle = getOldestMotorcycle(motorcycles)
writeThingToConsole(f"A legidősebb motorkerékpár az {oldestMotorcycle.manufacturer} {oldestMotorcycle.model} ({oldestMotorcycle.productionYear})")
#e) feladat
sortedByprice = sortByPrice(motorcycles)
writeMotorcyclesInFile("olcso-draga.txt", motorcycles)
