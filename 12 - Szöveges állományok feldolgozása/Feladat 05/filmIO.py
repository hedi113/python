from typing import *
from film import *
import os
from io import open

def readFilmFromFile(fileName: str) -> List[Film]:
    films: List[Film] = []
    film: Film = None

    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try: 
        with open(fileFullPath, encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split(",")

                film = Film()

                film.name = data[0]
                film.genre = data[1]
                film.distributor = data[2]
                film.viewerRating = int(data[3])
                film.payOff = float(data[4])
                film.rottenTomatoes = int(data[5])
                film.income = float(data[6].replace("$", ""))
                film.releaseYear = int(data[7])

                films.append(film)
        return films
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []
    
