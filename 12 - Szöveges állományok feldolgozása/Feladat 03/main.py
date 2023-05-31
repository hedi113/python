from player import Player
from playerIO import *
from typing import *
from services import *

fileName: str = "data/adatok.txt"
players: List[Player] = readPlayersFromFile(fileName)

#Írjuk ki a képernyőre az össz adatot
writeToConsole(players)

#Keressük ki az ütő játékosokat az utok.txt állömányba
allPlayerData: List[Player] = findPlayerInfo(players, "ütő")
writePlayersInFile("utok.txt", players)

