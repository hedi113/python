szam1: int = None
szam2: int = None

print("Kérem az első számot: ", end="")
szam1 = int(input())

print("Kérem a második számot: ", end="")
szam2 = int(input())

if szam1 > szam2:
    print("Az első szám a nagyobb.")
elif szam2 > szam1:
    print("A második szám a nagyobb.")