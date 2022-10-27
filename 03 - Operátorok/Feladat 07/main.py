szam: int = None
eredmeny: float = None

print("Kérem a számot: ", end="")
szam = int(input())

eredmeny = szam % 6 and szam % 4

if eredmeny == 0:
    print("A szám osztható 4-gyel és 6-tal is.")