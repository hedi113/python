szam: int = None

print("Kérem a számot: ", end="")
szam = int(input())

if szam > 10 and szam < 20:
    print("A szám a megadott tartalmon belül van.")
elif szam < -10 and szam > -20:
    print("A szám a megadott tartalmon belül van.")
else: 
    print("A szám nincs a megadott tartalmon belül.")