def getNumberFromConsole() -> int:
    forint: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None
    while(forint == None):
        print("Adjon meg egy összeget forintban: ", end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if(isNumber):
            forint = int(temp)
        else:
            print("Nem pénzösszeget adott meg!!")
    return forint

def getChoiceFromConsole() -> int:
    choice: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None
    while(choice == None or (choice > 3 or choice < 0)):
        print("Válasszon a megadott pénznemek közül: \n 1. USD \n 2. JPY \n 3. CHF")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()
        
        if(isNumber):
            choice = int(temp)
        else:
            print("Nem számot adott meg!!")
    return choice

def printEURtoConsole(eur: int) -> None:
    print(f"Ezen összeg értéke euróban: {eur}")

def printUSDtoConsole(usd: int) -> None:
    print(f"A megadott összeg értéke dollárban: {usd}")

def printJPYtoConsole(jpy: int) -> None:
    print(f"A megadott összeg japán yenben: {jpy}")

def printCHFtoConsole(chf: int) -> None:
    print(f"A megadott összeg svájci frankban: {chf}")


