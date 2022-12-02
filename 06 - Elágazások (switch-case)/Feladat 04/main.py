szam1: int = None
szam2: int = None
muvelet: str = None
eredmeny: float = None

print("Kérem a két számot és a műveletet: ")
szam1 = int(input())
szam2 = int(input())
muvelet = str(input()).strip()

match muvelet:
    case "+":
        eredmeny = szam1 + szam2
    case "*":
        eredmeny = szam1 * szam2
    case "-":
        eredmeny = szam1 - szam2
    case "/":
        eredmeny = szam1 / szam2
    case _:
        print("A megadott művelet nem végezhető el.")

if(eredmeny != None):
    print(f"{szam1} {muvelet} {szam2} = {eredmeny}")