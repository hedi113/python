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

#Rendezzük a játékosokat magasság szerint növekvő sorrendbe és a magaslatok.txt állományba mentsük el.
sortPlayersBy(players)
writePlayersInFile("magaslatok.txt", players)

#atlagnalmagasabbak.txt állományba keressük azon játékosok nevét és magasságát akik magasabbak mint az „adatbázisban” szereplő játékosok átlagos magasságánál.
avarage = calculateAvarage(players)
aboveAvarage = getAboveAvarage(players, avarage)
writePlayersInFile("atlagnalmagasabbak.txt", aboveAvarage)

#Egy szöveges állományba, „alacsonyak.txt” keresse ki a játékosok átlagmagasságától alacsonyabb játékosokat. Az állomány tartalmazza a játékosok nevét,  magasságát és hogy mennyivel alacsonyabbak az átlagnál, 2 tizedes pontossággal.

heightdifference = calculateBelowAvarage(avarage, players)
writeSmallPlayersInFile("alacsonyak.txt", players, heightdifference)