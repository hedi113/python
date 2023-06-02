from typing import *
from playerIO import *
from player import Player
from smallPlayer import SmallPlayer

def writeToConsole(players: List[Player]) -> None:
    for player in players:
        print(player)

def findPlayerInfo(players: List[Player], type: str) -> List[Player]:
    allPlayerInfo: List[Player] = []

    for player in players:
        if(player.post == type): 
            allPlayerInfo.append(player)

    return allPlayerInfo

def sortPlayersBy(players: List[Player]) -> None:
    playerCount: int = len(players)
    temp: int = None

    for i in range(0, playerCount -1, 1):
        for j in range(i + 1, playerCount, 1):
            if(players[j].height < players[i].height): 

                temp = players[i]
                players[j] = players[j]
                players[j] = temp

def calculateAvarage(players: List[Player]) -> float:
    sum: float = 0 

    for player in players:
        
        sum += player.height
    
    return sum / len(players)

def getAboveAvarage(players: List[Player], avarage: float) -> List[Player]:
    aboveAvarage: List[Player] = []

    for player in players:
        if(player.height > avarage):
            aboveAvarage.append(player)

    return aboveAvarage

def getBelowAvarage(avarage: float, players: List[Player]) -> List[Player]:
    belowAvarage: List[player] = []
    for player in players:
        if(player.height < avarage):
            belowAvarage.append(player)

    return belowAvarage

def calculateHeightDifference(avarage: float, smallPlayers: List[SmallPlayer]) -> float:
    value: float = 0

    for smallPlayer in smallPlayers:
        value = value + avarage - smallPlayer.height
        smallPlayers.append(value)

    return smallPlayers


    
    