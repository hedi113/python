szam: int = None
eredmeny: float = None
eredmeny2: float = None

print("Kérem a számot: ", end="")
szam = int(input())

eredmeny = szam % 2

eredmeny2 = szam % 5

if  eredmeny == 0  and szam > 0:
    print("A szám pozitív és páros.")
elif  eredmeny == 0  and szam < 0:
    print("A szám negatív és páros.")
elif eredmeny2 == 0 and szam > 0:
    print("A szám pozitív és osztható 5-tel.")
elif eredmeny2 == 0 and szam < 0:
    print("A szám negatív és osztható 5-tel.")
elif eredmeny == 0:
    print("A szám osztható 2-vel.")
elif eredmeny2 == 0:
    print("A szám osztható 5-tel.")
elif szam > 0:
    print("A szám pozitív.")
elif szam < 0: 
    print("A szám negatív.")
else:
    print("Egyik állítás sem igaz a számra.")
