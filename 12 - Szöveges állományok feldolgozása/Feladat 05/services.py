from typing import *
from film import *
from filmIO import *

def writeThingsToConsole(thing: str) -> None:
    print(thing) 

def howManyFilms(films: List[Film]) -> int:
    howManyFilms: int = 0

    howManyFilms = len(films)
    
    return howManyFilms

def determineAllIncome(films: List[Film]) -> float:
    allIncome: float = 0

    for film in films:
        allIncome = allIncome + film.income

    return allIncome

def detrermineBestrating(films: List[Film]) -> Film:
    bestRating: Film = films[0]

    for index in range(1, len(films), 1):
        if(films[index].viewerRating > bestRating.viewerRating):
            bestRating = films[index]

    return bestRating

def determineTomatoRating(films: List[Film]) -> bool:
    rottenTomato: bool = False
    for film in films:
        if(film.rottenTomatoes > 90):
            rottenTomato = True
        else:
            rottenTomato = False

    return rottenTomato

def writeTomatoToConsole(tomatoRating: bool) -> None:
    if(tomatoRating == True):
        print("Van olyan film, amely a Rotten Tomatoes értékelése alapján legalább 90% értékelést kapott.")
    else:
        print("Nincs olyan film, amely a Rotten Tomatoes értékelése alapján legalább 90% értékelést kapott.")