szam: int = None

print("Adja meg a vizsgálandó számot: ", end="")
szam = int(input())

if szam > -30 and szam < 40:
    print("A szám a megadott érték között van.")
else:
    ("A szám nincs a megadott tartományban.")