kezdoertek: int = None
vegertek: int = None

print("Kérem a kezdő értéket: ", end = "")
kezdoertek = int(input())
print("Kérem a végső értéket: ", end = "")
vegertek = int(input())

if(kezdoertek > vegertek):
    for i in range(kezdoertek, vegertek, -1):
        print(i)
elif(vegertek > kezdoertek):
    for i in range(vegertek, kezdoertek, -1):
        print(i)
