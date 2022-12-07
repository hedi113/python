import math

hossz: int = None
szelesseg: int = None
valasztas: str = None
eredmeny: float = None

hossz = int(input("Kérem a téglalap hosszát: "))
szelesseg = int(input("Kérem a téglalap szélességét: "))

print("Mit szeretne kiszámolni:\nt - terület\nk - kerület\na - átló")
valasztas = str(input()).lower().strip()

match valasztas:
    case "t":
        eredmeny = hossz * szelesseg
    case "k":
        eredmeny = (hossz + szelesseg)*2
    case "a":
        eredmeny = math.sqrt(hossz**2 + szelesseg**2)
    case _:
        ("A műveletet nem lehet elvégezni.")

if(valasztas != None):
    print(f"A választott művelet végeredménye: {eredmeny:1.0f}")