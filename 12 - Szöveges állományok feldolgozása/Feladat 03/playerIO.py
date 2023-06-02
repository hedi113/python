from player import Player
import os
from typing import *
from io import open
from services import *
from smallPlayer import SmallPlayer

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

def readSmallPlayers(fileName2: str) -> List[SmallPlayer]:
    smallPlayers: List[SmallPlayer] = []
    smallPlayer: SmallPlayer = None

    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName2)

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split('\t')

                smallPlayer = SmallPlayer()
                smallPlayer.name = data[0]
                smallPlayer.height = int(data[1])
                smallPlayer.heightDifference = float(data[2])

                smallPlayers.append(smallPlayer)

        return smallPlayers
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
                file.write(f"{player.name}\t{player.height}\t{player.post}\t{player.team}\t{player.nationality}\n")
    
    except FileNotFoundError as ex:
        print(f"{ex.filename} írásakor hiba lépett fel!")

def writeSmallPlayersInFile(fileName: str, smallPlayers: List[SmallPlayer]) -> None:
    
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)


    try:
        with open(fileFullPath,encoding="utf-8", mode="w") as file:
            for smallPlayer in smallPlayers:
                file.write(f"{smallPlayer.name} - {smallPlayer.height} : {smallPlayer.heightDifference:1.2f}\n")
    
    except FileNotFoundError as ex:
        print(f"{ex.filename} írásakor hiba lépett fel!")


        