import random

paros: int = None
paratlan: int = None
tempparos: str = None
tempparatlan: str = None
isNumber: bool = False

while(paros == None or (paros % 2 == 1)):
    print("Adjon meg egy páros számot: ", end = "")
    tempparos = input()
    isNumber = tempparos.isnumeric()

    if(isNumber):
        paros = int(tempparos)
    else:
        ("Nem páros számot adott meg!")

while(paratlan == None or (paratlan < paros)):
    print("Adjon meg egy az előzőtől nagyobb páratlan számot: ", end="")
    tempparatlan = input()
    isNumber = tempparatlan.isnumeric()

    if(isNumber):
        paratlan = int(tempparatlan)
    else:
        print("Nem a feltételeknek megfelelő számot adott meg!")


rnd: int = random.randint(paros, paratlan)

if((paros - rnd)>(paratlan - rnd)):
    print(f"A random szám ({rnd}) {paros}-hoz van közelebb.")