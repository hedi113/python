number: int = None
temp: str = None
isNumber = False

inputs = 0
szum = 0
while(szum < 100):
    print("Adja meg a számot: ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        number = int(temp)
    else:
        print("Nem számot adott meg!!!!!")
    
    if(number > 0):
        szum = szum + number
        inputs = inputs + 1
        print(f"Az eddigi összeg: {szum}, bevitelek száma: {inputs}")
    if(number > 100):
        print("A megadott szám önmagában meghaladja a 100-at.")
        break
    