def hianyzasok(hianyzasokSzama: int) -> str:

    if(hianyzasokSzama >= 1 and hianyzasokSzama <= 4):
        return "figyelmeztetés"
    elif(hianyzasokSzama >= 5 and hianyzasokSzama <= 10):
        return "osztályfőnöki megrovás"
    elif(hianyzasokSzama >= 11 and hianyzasokSzama <= 30):
        return "igazgatói megrovás"
    elif(hianyzasokSzama > 30):
        return "elbocsájtás az iskolából"
    else:
        return "nem értélmezhető"