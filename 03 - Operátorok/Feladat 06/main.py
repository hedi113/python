szam1: int = None
szam2: int = None
szam3: int = None
eredmeny: float = None

print("Kérem az első számot: ", end="")
szam1 = int(input())

print("Kérem a második számot: ", end="")
szam2 = int(input())

print("Kérem a harmadik számot: ", end="")
szam3 = int(input())

eredmeny = (szam1 + 0.5) * (szam2 - 0.7) % szam3
print(f"Az osztás maradéka: {eredmeny:1.1f}")
