number: float = None
temp: str = None
isNumber: bool = False
truncatedString: str = None

while(number == None or (number < 0 or number > 9)):
    print("Adjon meg egy számot: ", end = "")
    temp = input()
    truncatedString = temp.replace(".", "").replace("-","")
    isNumber = truncatedString.isnumeric()

    if(isNumber):
        number = float(temp)
        print(temp)
    else: 
        print("Nem számot adott meg!")