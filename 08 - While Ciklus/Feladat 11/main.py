import random

paros: int = None
paratlan: int = None
tempparos: str = None
tempparatlan: str = None
isNumber: bool = False
atlag: float = 0

while(paros == None or (paros % 2 == 1)):
    print("Adjon meg egy páros számot: ", end = "")
    tempparos = input()
    isNumber = tempparos.isnumeric()

    if(isNumber):
        paros = int(tempparos)
    else:
        ("Nem páros számot adott meg!")

while(paratlan == None or (paratlan < paros) or paratlan % 2 == 0):
    print("Adjon meg egy az előzőtől nagyobb páratlan számot: ", end="")
    tempparatlan = input()
    isNumber = tempparatlan.isnumeric()

    if(isNumber):
        paratlan = int(tempparatlan)
    else:
        print("Nem a feltételeknek megfelelő számot adott meg!")


rnd: int = random.randint(paros, paratlan)

if((paratlan - paros) < rnd):
    print(f"A random szám ({rnd}) {paros}-tól/től van messzebb.")
else:
    print(f"A random szám ({rnd}) {paratlan}-tól/től van messzebb.")


db = 0
db2 = 0
for i in range(paros, paratlan, 1):
    db = db + 1
    atlag = (atlag + i) / db
    if(i % 4 == 0):
        db2 = db2 + 1
print(f"A számok közti átlag: {atlag}")
print(f"A 4-gyel osztható számok (db): {db2}", end="")


