megtakaritas: int = None
temp: str = None
isNumber: bool = False

while(megtakaritas == None or megtakaritas < 0 or megtakaritas > 100000):
    print("Kérem a megtakarított összeget (kisebb mint 100 000 Ft): ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        megtakaritas = int(temp)
    else:
        print("Nem pénzösszeget adott meg, vagy az már eleve meghaladja a 100 000 Ft-ot!")
    
    
month = 0
kamat = megtakaritas * 0.02
vegosszeg = 100000
megtakaritkamat = megtakaritas + kamat
veges = 0


while(megtakaritas < 100000):
    megtakaritas = megtakaritas + kamat
    if(megtakaritas):
        month = month + 1


print(f"A megtakarított összeg {month} hónap alatt érte el a 100 000 Ft értéket.")



#while a for helyett!!!