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
    if(i % 2 == 0):
        osszeg = osszeg + i

print(osszeg)

osszeg2 = vegertek
for i in range(kezdoertek, vegertek, 1):
    if(i % 2 == 1):
        osszeg2 = osszeg * i

print(osszeg2)