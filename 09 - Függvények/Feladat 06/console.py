def getNumberFromConsole() -> int:
    celsius: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None
    while(celsius == None):
        print("Adjon meg egy számot: ", end = "")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-","")
        isNumber = truncatedString.isnumeric()

        if(isNumber):
            number = int(temp)
        else: 
            print("Nem számot adott meg!")
    return celsius

def printToConsole()