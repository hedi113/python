from motorcycle import Motorcycle
from typing import *
from motorcycleIO import *

def writeMotorcycleToConsole(motorcycles: List[Motorcycle]) -> None:
    for motorcycle in motorcycles: 
        print(motorcycle)

def writeThingToConsole(thing: str):
    print(thing)


def madeAfter2000(motorcycles: List[Motorcycle]) -> List[Motorcycle]:
    after2000: List[Motorcycle] = []

    for motorcycle in motorcycles:
        if(motorcycle.productionYear > 2000):
            after2000.append(motorcycle)
    
    return after2000

def howManyMotorcycles(motorcycles: List[Motorcycle]) -> int:
    motorcyleCount: int = len(motorcycles)

    return motorcyleCount

def getPriceAvarage(motorcycles: List[Motorcycle]) -> float:
    
    sum: int = 0
    for motorcycle in motorcycles:
        sum += motorcycle.price
    
    priceAvarage: float = sum / len(motorcycles)

    return priceAvarage

def getOldestMotorcycle(motorcyles: List[Motorcycle]) -> Motorcycle:
    oldestMotorcycle: Motorcycle = motorcyles[0]

    for index in range(1, len(motorcyles), 1):
        if(motorcyles[index].productionYear < oldestMotorcycle.productionYear):
            oldestMotorcycle = motorcyles[index]

    return oldestMotorcycle

def sortByPrice(motorcycles: List[Motorcycle]) -> None:
    motorcycleCount: int = len(motorcycles)
    temp: int = None

    for i in range(0, motorcycleCount -1, 1):
        for j in range(i + 1, motorcycleCount, 1):

            if(motorcycles[j].price < motorcycles[i].price):

                temp = motorcycles[i]
                motorcycles[j] = motorcycles[j]
                motorcycles[j] = temp




