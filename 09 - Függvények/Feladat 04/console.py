def printInColor() -> str:
    name: str = None
    
    while(name == None or len(name) < 2):
        print("Adja meg a nevét: ", end="")
        name = input()

        if(len(name) < 2):
            print("Nem megfelelő a név!")

    if(len(name) >= 2):
        match len(name):
            case 2:
                print("Üdvözlöm,\033[95m {}\033[00m!" .format(name))
            case 3:
                print("Üdvözlöm,\033[97m {}\033[00m!" .format(name))
            case 4:
                print("Üdvözlöm,\033[96m {}\033[00m!" .format(name))
            case 5:
                print("Üdvözlöm,\033[94m {}\033[00m!" .format(name))
            case 6:
                print("Üdvözlöm,\033[93m {}\033[00m!" .format(name))
            case _:
                print("Üdvözlöm,\033[96m {}\033[00m!" .format(name))
    
    return name.capitalize().strip()    

def finalPrint(name: str) -> None:
    print(f"Üdvözlöm, {name}!")