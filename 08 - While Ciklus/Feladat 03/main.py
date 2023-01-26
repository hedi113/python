import random

rnd: int = random.randint(0 , 9)
number: int = None
db = 0

while (number != rnd):
    print("Adjon meg egy számot 0 és 9 között: ", end="")
    number = input()

    
    if(number == rnd):
        print(f"A random generált szám az {rnd} volt. Gratulálok!")

    else: 
        db = db + 1

    if(db == 5):
        print("Kifutott a próbálkozási lehetőségekből!")
        break



