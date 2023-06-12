def hianyzasok(hianyzasokSzama: int, nev: str) -> None:

    if(hianyzasokSzama >= 1 and hianyzasokSzama <= 4):
        print(f"{nev}: figyelmeztetés")
    elif(hianyzasokSzama >= 5 and hianyzasokSzama <= 10):
        print(f"{nev}: osztályfőnöki megrovás")
    elif(hianyzasokSzama >= 11 and hianyzasokSzama <= 30):
        print(f"{nev}: igazgatói megrovás")
    elif(hianyzasokSzama > 30):
        print(f"{nev}: elbocsájtás az iskolából")
    else:
        print(f"{nev}: nem értélmezhető")