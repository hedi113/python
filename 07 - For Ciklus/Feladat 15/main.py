kezdoertek: int = None
vegertek: int = None
db: int = None

print("Kérem a kezdő értéket: ", end = "")
kezdoertek = int(input())
print("Kérem a végső értéket: ", end = "")
vegertek = int(input())

db = 0
for i in range(kezdoertek, vegertek, 1):
    if(i % 2 == 1 and i % 3 == 0):
            db = db + 1

print(db)
