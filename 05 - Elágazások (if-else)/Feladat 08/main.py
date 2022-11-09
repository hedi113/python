szam: int = None
eredmeny: float = None
eredmeny2: float = None

print("Kérem a számot: ", end="")
szam = int(input())

eredmeny = szam % 4
eredmeny2 = szam % 6

if eredmeny2 ==0 and eredmeny ==0:
    print("A szám osztható 4-gyel és 6-tal is.")
elif eredmeny == 0:
    print("A szám csak 4-gyel osztható.")
elif eredmeny2 == 0:
    print("A szám csak 6-tal osztható.")
else:
    print("A szám nem osztható sem 4-gyel sem 6-tal.")