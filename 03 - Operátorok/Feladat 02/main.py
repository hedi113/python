szam1: int = None
szam2: int = None
szam2: int = None
eredmeny: int = None

print("Kérem az első számot: ", end="")
szam1 = int(input())

print("Kérem a második számot: ", end="")
szam2 = int(input())

print("Kérem a harmadik számot: ", end="")
szam3 = int(input())

eredmeny = szam1 + szam2 - szam3
print(f"A végeredmyény: {eredmeny}") 