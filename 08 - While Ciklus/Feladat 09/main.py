number: int = None
isNumber: bool = False
temp: str = ""

while(len(temp) < 3 or number == None):
    print("Adjon meg egy három jegyű számot: ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        number = int(temp)
    else: 
        print("Nem számot adott meg!")

if(number % 7 == 0):
    print(f"{number} osztható 7-tel.")
else:
    print(f"{number} nem osztható 7-tel.")
