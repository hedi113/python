szam: int = None
eredmeny: float = None
eredmeny2: float = None

print("Kérem a számot: ", end="")
szam = int(input())

eredmeny = szam % 2

eredmeny2 = szam % 3

if (eredmeny == 0 and eredmeny2 ==0):
    print("ZIZI")
elif (eredmeny == 0):
    print("BIZ")
elif (eredmeny2 == 0):
    print("BAZ")
else: 
    print("A szám sem 3-mal sem 2-vel sem osztható.")