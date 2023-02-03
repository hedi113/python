smaller: int = None
larger: int = None
isNumber: bool = False
temp: str = None

while(smaller == None):
    print("Adja meg az első számot: ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        smaller = int(temp)
    else: 
        print("Nem számot adott meg!")

while(larger == None or larger < smaller):
    print("Adja meg a második számot (az előzőnél legyen nagyobb): ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        larger = int(temp)
    else: 
        print("Nem számot adott meg!")



for i in range(larger, smaller, -1):
    print(i)
