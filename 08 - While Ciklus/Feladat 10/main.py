number: int = None
isNumber: bool = None
temp: str = ""
divideSzum5 = 0
divide11Db = 0


while(len(temp) > 2 or number == None):
    print("Adjon meg egy kétjegyű pozitív számot: ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        number = int(temp)
    else: 
        print("Nem pozitív számot adott meg!!!!")

print("Páros számok: ")
for i in range(0, number, 1):
    if(i % 2 == 0):
        print(i)
    if(i % 5 == 0):
        divideSzum5 = divideSzum5 + i
    if(i % 11 == 0):
        divide11Db = divide11Db + 1

print("5-tel osztható számok összege: ", end="")
print(divideSzum5)
print("11-el osztható számok (db): ", end="")
print(divide11Db)

print("7-tel osztva 3-at maradékul adó számok: ")
for i in range(0, number, 1):
    if(i % 7 == 3):
        print(i)