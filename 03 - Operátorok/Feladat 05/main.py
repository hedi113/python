szam1: int = None
szam2: int = None
szam3: int = None
szam4: int = None
eredmeny: float = None

print("Kérem az első számot: ", end="")
szam1 = int(input())

print("Kérem a második számot: ", end="")
szam2 = int(input())

print("Kérem a harmadik számot: ", end="")
szam3 = int(input())

print("Kérem a negyedik számot: ", end="")
szam4 = int(input())

eredmeny = (szam1 + szam2) / (szam3 - szam4)
print(f"A végeredmény: {eredmeny}")
