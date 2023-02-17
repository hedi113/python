number: int = 0
final: int = 0
temp: str = None
isNumber: bool = False

szum = 0
steps = 0

while(final < 100):
    print("Adja meg a határértéket (min.: 100): ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        final = int(temp)
    else:
        print("Nem számot adott meg!!")

while(szum < final):
    print("Adjon meg egy számot: ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        number = int(temp)
    else: 
        print("Nem számot adott meg!!")

    if(number > 0):
        szum = szum + number
        steps = steps + 1
        print(f"A jelenlegi összeg: {szum}")
    if(szum >= final):
        print(f"Ennyi lépésben érte el a határértéket ({final}): {steps}")   




