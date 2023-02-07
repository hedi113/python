number: int = None
isNumber: bool = None
temp: str = ""
divideSzum5 = 0
divide11Db = 0


while(len(temp) > 2 or number == None):
    print("Adjon meg egy kétjegyű pozitív számot: ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        number = int(temp)
    else: 
        print("Nem pozitív számot adott meg!!!!")



