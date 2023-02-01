myName: str = ""

while(len(myName) < 2):
    print("Kérem a nevét: ", end="")
    myName = str(input())

print(f"Üdvözlöm! {myName}")


