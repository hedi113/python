szam: int = None

print("Adja meg a vizsgálandó számot: ", end="")
szam = int(input())

if szam > 0:
    print("A szám pozitív.")
elif szam == 0:
    print("A szám sem pozitív, sem negatív (tehát 0).")
else:
    print("A szám kisebb mint 0.")
