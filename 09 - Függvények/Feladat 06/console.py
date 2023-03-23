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
            celsius = int(temp)
        else: 
            print("Nem számot adott meg!")
    return celsius
def getChoiceFromConsole() -> int:
    choice: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None
    while(choice == None):
        print("Válasszon egy számot:\n1 - Kelvin\n2 - Farenheit")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-","")
        isNumber = truncatedString.isnumeric()

        if(isNumber):
            choice = int(temp)
        else: 
            print("Nem számot adott meg!")
    return choice

def printResult(kelvin: int) -> None:
    print(f"A megadott érték Kelvinben: {kelvin}")

def printResult2(fahrenheit: int) -> None:
    print(f"A megadott érték Fahrenheitben: {fahrenheit}")

