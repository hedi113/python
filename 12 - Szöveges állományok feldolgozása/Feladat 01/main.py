from typing import *
from io import open
import os

fileName:str = "data/ip.txt"
basepath: str = os.path.dirname(os.path.abspath(__file__))
fileFullPath: str = os.path.join(basepath, fileName)

oneLine:str = None
allLines:List[str]=[]

try:
    with open(fileFullPath,encoding="utf-8", mode="r") as file:
        for line in file:
            oneLine = line.strip()
            allLines.append(oneLine)
except FileNotFoundError as ex:
    print(f"{ex.filename} nem található!")

for line in allLines:
    print(f"{line}")
