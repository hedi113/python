name: str = "hodi rovo hedi"
myName: str = None

while(myName != name):
    print("Kérem a nevét: ", end="")
    myName = input()


    if(name == str(myName)):
        print("Üdvözlöm!")
    else:
        print("Nem a nevét adta meg!")


