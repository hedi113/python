name: str = "hodi rovo hedi"
myName: str = None
isItMyName: bool = False

while(myName != name):
    print("Kérem a nevét: ", end="")
    myName = input()
    isItMyName = myName.lower().strip().replace("-", "")

    if(isItMyName):
        name = str(myName)
        print("Üdvözlöm!")
    else:
        print("Nem a nevét adta meg!")


