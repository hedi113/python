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

def printEURtoConsole(eur: int) -> None:
    print(f"A megadott összeg értéke euróban: {eur}")

def printUSDtoConsole(usd: int) -> None:
    print(f"A megadott összeg értéke dollárban: {usd}")

def printJPYtoConsole(jpy: int) -> None:
    print(f"A megadott összeg japán yenben: {jpy}")

def printCHFtoConsole(chf: int) -> None:
    print(f"A megadott összeg svájci frankban: {chf}")
