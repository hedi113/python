import random

rnd: int = random.randint(0 , 9)
number: int = None
isNumber: bool = False
temp: str = None
db = 0

while (number != rnd and db < 5):
    print("Adjon meg egy számot 0 és 9 között: ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        number = int(temp)
    else: 
        print("Nem számot adott meg!!!!")

    
    if(number == rnd):
        print(f"A random generált szám az {rnd} volt. Gratulálok!")

    else: 
        db = db + 1



