def getNameFromConsole() -> str:
    name: str = None

    while(name == None or len(name) < 2):
        print("Adja meg a nevét: ", end="")
        name = input()

        if(len(name) < 2):
            print("Nem megfelelő a név!")

    return name.capitalize().strip()


def getAgeFromConsole() -> int:
    age: int = None
    isNumber: bool = False
    temp: str = None
    while(age == None):
        print("Adja meg a születési évszámát: ", end="")
        temp = input()
        isNumber = temp.isnumeric()

        if(isNumber):
            age = int(temp)
        else: 
            print("Nem évszámot adott meg!!!!")
    return age

def printWelcomeMessage(name: str, result: int) -> None:
    print(f"Üdvözlöm, {name}, maga most {result} éves!")