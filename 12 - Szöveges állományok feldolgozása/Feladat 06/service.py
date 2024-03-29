from auto import *
from typing import *
from autoIO import *

def writeThingsToConsole(thing: str):
    print(thing)

def countAutosInFile(autos: List[Auto]) -> int:

    autoCount: int = len(autos)

    return autoCount

def autoWeightSum(autos: List[Auto]) -> int:
    weightSum: int = 0

    for auto in autos:
        weightSum = weightSum + auto.weight

    return weightSum

def getBestTorque(autos: List[Auto]) -> Auto:
    bestTorque: Auto = autos[0]

    for index in range(1, len(autos), 1):
        if(autos[index].torque > bestTorque.torque):
            bestTorque = autos[index]
    
    return bestTorque

def determineSpeed(autos: List[Auto]) -> bool:
    autoSpeed: bool = False

    for auto in autos:
        if(auto.speed > 7):
            autoSpeed = True
        else:
            autoSpeed = False

    return autoSpeed

def writeSpeedToConsole(autoSpeed: bool):
    if(autoSpeed == True):
        print("Van olyan autó, amely a 7s alatt gyorsul fel 100km/h sebességre.")
    else:
        print("Nincs olyan autó, amely a 7s alatt gyorsul fel 100km/h sebességre.")