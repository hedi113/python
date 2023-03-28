def getNameFromConsole() -> str:
    name: str = None
    while(name == None or len(name) < 2):
        print("Adja meg a nevét: ", end="")
        name = input()
    return name

def getHoursFromConsole() -> int:
    hours: int = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None
    while(hours == None or (hours < 0) or (hours > 100)):
        print("Adja meg, hogy hány órát dolgozott ezen a héten: ", end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric

        if(isNumber):
            hours = int(temp)
        else:
            print("Nem számot adott megy, vagy a dolgozott órák száma meghaladja a 100-at.")
        return hours

def howMuchPayment(hours: int) -> int:
    payment: int = None
    if(hours == 40 or hours < 40):
        payment = hours * 1000
    if(hours > 40):
        payment = (hours - 40) * 1500 + 40 * 1000 
    return payment

def printNameAndPayment(name: str, payment: int, hours: int) -> None:
    print(f"{name} e heti keresete: {payment} \nMunkaidő: {hours} óra")
