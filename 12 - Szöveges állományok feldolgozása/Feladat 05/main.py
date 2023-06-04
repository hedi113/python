from typing import *
from services import *
from film import *
from filmIO import *

fileName = "data/filmek.csv"
films: List[Film] = readFilmFromFile(fileName)

#1. feladat
howManyFilms = howManyFilms(films)
writeThingsToConsole(f"{fileName} állományban {howManyFilms} film szerepel.")

#2. feladat
allIncome = determineAllIncome(films)
writeThingsToConsole(f"A {fileName} állományban szerepelő filmek ösz bevétele ${allIncome:1.2f} millió dollár.")

#3. feladat
maxValue = getMaxValue(films)
bestRating = detrermineBestrating(films, maxValue)
writeThingsToConsole(f"A legnagyobb értékelést a {bestRating.name} című film kapta ({maxValue}%)")

#4.feladat
tomatoRating = determineTomatoRating(films)
writeTomatoToConsole(tomatoRating)