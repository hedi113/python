szam1: int = None
szam2: int = None
szam3: int = None

print("Kérem az első számot: ", end="")
szam1 = int(input())

print("Kérem a második számot: ", end="")
szam2 = int(input())

print("Kérem a harmadik számot: ", end="")
szam3 = int(input())

if (szam1 > szam2 and szam3):
    if (szam2 > szam3):
        print(f"{szam1},")
