def getNameFromConsole() -> str:
    name: str = None

    while(name == None or len(name) < 2):
        print("Adja meg a nevét: ", end="")
        name = input()

        if(len(name) < 2):
            print("Nem megfelelő a név!")

    return name.capitalize().strip()

def printWelcomeMessage(name: str) -> None:
    print(f"Üdvözlöm, {name}!")
