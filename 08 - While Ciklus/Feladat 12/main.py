megtakaritas: int = None
temp: str = None
isNumber: bool = False

while(megtakaritas == None or megtakaritas < 0):
    print("Kérem a megtakarított összeget: ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        megtakaritas = int(temp)
    else:
        print("Nem pénzösszeget adott meg!")

month = 0
kamat = 0
vegosszeg = 100000


for i in range(megtakaritas, 100000, 1000):
    kamat = megtakaritas * 0.02
    kamatosszeg = i + kamat
    
    if(kamatosszeg):
        month = month + 1
    
    if(i + kamat == vegosszeg):
        print(f"A megtakarított összeg {month} hónap alatt érte el a 100 000 Ft értéket.")

#while a for helyett!!!