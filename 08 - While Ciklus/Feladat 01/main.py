number: float = None
temp: str = None
isNumber: bool = False

while(number == None or (number < 0 or number > 9)):
    print("Adjon meg egy számot: ", end = "")
    temp = input()
    isNumber = isinstance(temp, (int, float))

    if(isNumber):
        number = float(temp)
    else: 
        print("Nem számot adott meg!")