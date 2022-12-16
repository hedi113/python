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

osszeg2 = 0
for i in range(kezdoertek, vegertek, 1):
    if(i % 2 == 1):
        osszeg2 = osszeg2 + i

if(osszeg > osszeg2):
    print("A páros számok összege a nagyobb.")
elif(osszeg2 > osszeg):
    print("A páratlan számok összege a nagyobb.")