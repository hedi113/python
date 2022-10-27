szam: int = None
eredmeny: float = None

print("Kérem a számot: ", end="")
szam = int(input())

eredmeny = szam % 5

if eredmeny == 0:
    print("A szám osztható 5-tel.")
else:
    print("A szám nem osztható 5-tel.")
