from motorcycle import Motorcycle
from io import open
import os
from typing import *

def readMotorcycleFromFile(fileName: str) -> List[Motorcycle]:
    motorcycles: List[Motorcycle] = []
    motorcycle: Motorcycle = None

    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)
    
    try:
        with open(fileFullPath, encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split('\t')

                motorcycle = Motorcycle()

                motorcycle.manufacturer = data[0]
                motorcycle.model = data[1]
                motorcycle.productionYear = int(data[2])
                motorcycle.price = int(data[3])

                motorcycles.append(motorcycle)

        return motorcycles   
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem atlálható!")
        return []

def writeMotorcyclesInFile(fileName: str, motorcycles: List[Motorcycle]) -> None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding="utf-8", mode="w") as file:
            for motorcycle in motorcycles:
               file.write(f"{motorcycle.manufacturer} - {motorcycle.model} - {motorcycle.productionYear} - {motorcycle.price}\n")
    except FileNotFoundError as ex:
        print(f"{ex.filename} írásakor hiba lépett fel!")
     

