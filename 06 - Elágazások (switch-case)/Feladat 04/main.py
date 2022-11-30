szam1: int = None
szam2: int = None
muvelet: str = None

print("Kérem a két számot és a műveletet: ")
szam1 = int(input())
szam2 = int(input())
muvelet = str(input())

match muvelet:
    case "+":
        eredmeny = szam1 + szam2
        print(f"A két szám összege: {eredmeny}")
    case "*":
        eredmeny2 = szam1 * szam2
        print(f"A két szám szorzatának eredménye: {eredmeny2}")
    case "-":
        eredmeny3 = szam1 - szam2
        print(f"A két szám külömbsége: {eredmeny3}")
    case "/":
        eredmeny4 = szam1 / szam2
        print(f"A két szám hányadosa: {eredmeny4}")
    case _:
        print("A megadott művelet nem végezhető el.")