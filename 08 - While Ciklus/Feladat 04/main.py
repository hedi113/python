number: int = None

inputs = 0
szum = 0
while(szum < 100):
    print("Adja meg a számot: ", end="")
    number = int(input())
    if(number > 0):
        szum = szum + number
        inputs = inputs + 1
        print(f"Az eddigi összeg: {szum}, bevitelek száma: {inputs}")
    if(number > 100):
        print("A megadott szám önmagában meghaladja a 100-at.")
        break
