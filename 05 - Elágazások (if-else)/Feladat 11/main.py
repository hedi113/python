szam: int = None

print("Kérem a számot: ", end="")
szam = int(input())

if (szam % 2 == 0):
    print("A szám páros.")
else:
    print("A szám nem páros.")

if (szam == 0):
    print(" A szám sem pozitív sem negatív.")
elif (szam > 0):
    print("A szám pozitív.")
else:
    print("A szám negatív.")

if (szam % 5 == 0):
    print("A szám osztható 5-tel.")
else:
    print("A szám nem osztható 5-tel.")