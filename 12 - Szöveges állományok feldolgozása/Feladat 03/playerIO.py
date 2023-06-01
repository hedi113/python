from player import Player
import os
from typing import *
from io import open
from services import *

def readPlayersFromFile(fileName: str) -> List[Player]:
    players: List[Player] = []
    player: Player = None

    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split('\t')

                player = Player()
                player.name = data[0]
                player.height = int(data[1])
                player.post = data[2]
                player.team = data[3]
                player.nationality = data[4]
                player.country = data[5]

                players.append(player)
        
        return players
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []
    
def writePlayersInFile(fileName: str, players: List[Player]) -> None:
    
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)


    try:
        with open(fileFullPath,encoding="utf-8", mode="w") as file:
            for player in players:
                file.write(f"{player.name} - {player.height} : {player.post} : {player.team} : {player.nationality}\n")
    
    except FileNotFoundError as ex:
        print(f"{ex.filename} írásakor hiba lépett fel!")

def writeSmallPlayersInFile(fileName: str, players: List[Player], heightdifference: float) -> None:
    
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)


    try:
        with open(fileFullPath,encoding="utf-8", mode="w") as file:
            for player in players:
                file.write(f"{player.name} - {player.height} : {heightdifference:1.2f}\n")
    
    except FileNotFoundError as ex:
        print(f"{ex.filename} írásakor hiba lépett fel!")


        