from typing import *
from playerIO import *
from player import Player

def writeToConsole(players: List[Player]) -> None:
    for player in players:
        print(player)

def findPlayerInfo(players: List[Player], type: str) -> List[Player]:
    allPlayerInfo: List[Player] = []

    for player in players:
        if(player.post == type): 
            allPlayerInfo.append(player)

    return allPlayerInfo