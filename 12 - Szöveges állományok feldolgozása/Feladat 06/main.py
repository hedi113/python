from auto import *
from typing import *
from autoIO import *
from service import *

fileName: str = "data/autok.csv"
autos: List[Auto] = readAutoFromFile(fileName)

#1.feladat
autoCount = countAutosInFile(autos)
writeThingsToConsole(f"Az {fileName} állományban {autoCount} autó szerepel.")

#2. feladat
weightSum = autoWeightSum(autos)
writeThingsToConsole(f"Az {fileName} állományban szerepelő autók ösz súlya {weightSum}kg.")

#3. feladat
maxTorque = determineMaxTorque(autos)
bestTorque = determineBestTorque(autos, maxTorque)
writeThingsToConsole(f"A legnagyobb nyomatékkal a {bestTorque.auto} rendelkezik ({maxTorque}Nm).")

#4. feladat
autoSpeed = determineSpeed(autos)
writeSpeedToConsole(autoSpeed)