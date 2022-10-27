szam: int = None

print("Adja meg a vizsgálandó számot: ", end="")
szam = int(input())

if szam > 0 or szam==0:
    print("A szám pozitív.")
elif szam < 0:
    print("A szám negatív.")
