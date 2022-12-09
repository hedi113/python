kezdoertek: int = None
vegertek: int = None

print("Kérem a kezdő értéket: ", end = "")
kezdoertek = int(input())
print("Kérem a végső értéket: ", end = "")
vegertek = int(input())

if(kezdoertek != 0):
    for i in range(kezdoertek, vegertek, +2):
        print(i)