import math

hossz: int = None
szelesseg: int = None
valasztas: str = None

hossz = int(input("Kérem a téglalap hosszát: "))
szelesseg = int(input("Kérem a téglalap szélességét: "))

print("Mit szeretne kiszámolni:\nt - terület\nk - kerület\na - átló")
valasztas = str(input())

match valasztas:
    case "t":
        eredmeny = hossz * szelesseg
        print(f"A téglalap területe: {eredmeny}")
    case "k":
        eredmeny2 = (hossz + szelesseg)*2
        print(f"A téglalap kerülete: {eredmeny2}")
    case "a":
        eredmeny3 = hossz**2 + szelesseg**2
        gyok = math.sqrt(eredmeny3)
        print(f"A téglalap átlója: {gyok:1.1f}")
    case _:
        ("A műveletet nem lehet elvégezni.")
