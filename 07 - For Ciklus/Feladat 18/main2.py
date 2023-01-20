kezdoertek: int = None
vegertek: int = None
osszeg: int = None
osszeg2: int = None

print("Kérem a kezdő értéket: ", end = "")
kezdoertek = int(input())
print("Kérem a végső értéket: ", end = "")
vegertek = int(input())

osszeg = 0
for i in range(kezdoertek, vegertek, 1):
    osszeg = osszeg + i - (i+1)

print(osszeg)