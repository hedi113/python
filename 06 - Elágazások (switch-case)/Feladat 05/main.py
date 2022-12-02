r1: int = None
r2: int = None
kotes: str = None
r1 = int(input("Kérem az R1 értékét: "))
r2 = int(input("Kérem az R2 értékét: "))
kotes = str(input("Kérem a kötés típusát: "))

match kotes:
    case "p"| "P":
        eredmeny = (r1+r2)/(r1*r2)
        print(f"A soros kötés ellenállása: {eredmeny}")
    case "s"| "S":
        eredmeny2 = r1 + r2
        print(f"A soros kötés ellenállása: {eredmeny2}")
    case _:
        print("A művelet nem végezhető el.")