megtakaritas: int = None
temp: str = None
isNumber: bool = False
honap: int = 0

while(megtakaritas == None or megtakaritas < 0 or megtakaritas > 100000):
    print("Kérem a megtakarított összeget (kisebb mint 100 000 Ft): ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        megtakaritas = int(temp)
    else:
        print("Nem pénzösszeget adott meg!")
    
    


while(megtakaritas < 100000):
    megtakaritas = megtakaritas * 1.02
    honap = honap + 1


print(f"A megtakarított összeg {honap} hónap alatt érte el a 100 000 Ft értéket.")



#while a for helyett!!!