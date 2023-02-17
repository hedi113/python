number: int = None
isNumber: bool = None
temp: str = None

while(number == None):
    print("Adjon meg egy számot a kínálatból: 1, 2, 3 -> ", end="")
    temp = input()
    isNumber = temp.isnumeric()

    if(isNumber):
        number = int(temp)
    else: 
        print("Nem számot adott meg!!!!")

match number:
    case 1:
        print("Az első üdítőt választotta.")
    case 2:
        print("A második üdítőt választotta.")
    case 3:
        print("A harmadik üdítőt választotta.")
    case "_":
        print("A megadott szám nem szerepel a listán!")
    