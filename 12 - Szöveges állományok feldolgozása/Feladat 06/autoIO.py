from auto import *
from typing import *
import os
from io import open

def readAutoFromFile(fileName: str) -> List[Auto]:
    autos: List[Auto] = []
    auto: Auto = None

    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split(",")

                auto = Auto()

                auto.auto = data[0]
                auto.mpg = float(data[1])
                auto.cylinder = int(data[2])
                auto.torque = float(data[3])
                auto.horsePower = float(data[4])
                auto.weight = int(data[5])
                auto.speed = float(data[6])
                auto.publicationYear = int(data[7])
                auto.origin = data[8]
                
                autos.append(auto)
        return autos
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []
    