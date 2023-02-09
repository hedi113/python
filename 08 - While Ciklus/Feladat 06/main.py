age: int = 0
temp: str = None
isNumber: bool = False

while(age <= 0 or age > 99):
    print("Adja meg az életkorát (0-99): ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        age = int(temp)
    else: 
        print("Nem egy életkort adott meg!")

if(age >= 0 and age <=6):
    print("Korosztály: gyerek")
elif(age >=7 and age <= 18):
    print("Korosztály: iskolás")
elif(age >=19 and age <= 65):
    print("Korosztály: dolgozó")
elif(age >=65 and age <= 99):
    print("Korosztály: nyugdíjas")
    
    