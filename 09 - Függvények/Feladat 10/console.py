def getGuessFromConsole(rnd: int, amount: int = 0) -> int:
    guess: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None
    while(guess == None or guess != rnd):
        print("Adjon meg egy számot: ", end="")
        temp = input()
        truncatedString = temp.replace("-", "").replace(".", "")
        isNumber = truncatedString.isnumeric()
        if(isNumber):
            guess = int(temp)
            amount = amount + 1
        else:
            print("Nem számot adott meg!!")
        
        if(guess < rnd):
            print("A tipp kisebb mint a gondolt szám.")
        elif(guess > rnd):
            print("A tipp nagyobb mint a gondolt szám.")
    return amount

def printResults(amount: int) -> None:
        print(f"Gratulálok! {amount} próbálkozásból találta ki a számot.")

    
