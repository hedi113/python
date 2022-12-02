r1: int = None
r2: int = None
kotes: str = None
eredmeny: float = None
r1 = int(input("Kérem az R1 értékét: "))
r2 = int(input("Kérem az R2 értékét: "))
kotes = str(input("Kérem a kötés típusát: "))

match kotes:
    case "p"| "P":
        eredmeny = (r1+r2)/(r1*r2)
    case "s"| "S":
        eredmeny = r1 + r2
    case _:
        print("A művelet nem végezhető el.")

if(eredmeny != None):
    print(f"A {kotes} kötés értéke: {eredmeny}")