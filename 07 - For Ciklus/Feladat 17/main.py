kezdoertek: int = None
vegertek: int = None
intervallum: int = None
db: int = None
atlag: float = None

print("Kérem a kezdő értéket: ", end = "")
kezdoertek = int(input())
print("Kérem a végső értéket: ", end = "")
vegertek = int(input())

intervallum = 0
db = 0
for i in range(kezdoertek, vegertek, 1):
    intervallum = intervallum + i
    db = db + 1

atlag = intervallum / db
print(atlag)