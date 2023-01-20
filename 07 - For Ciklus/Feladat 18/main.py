kezdoertek: int = None
vegertek: int = None
osszeg: int = None
osszeg2: int = None

print("Kérem a kezdő értéket: ", end = "")
kezdoertek = int(input())
print("Kérem a végső értéket: ", end = "")
vegertek = int(input())

osszeg = 0
for i in range(kezdoertek, vegertek, 2):
    if(vegertek % 2 == 1):
        osszeg = osszeg + i -(i + 1)
        osszeg2 = osszeg + vegertek
    if(kezdoertek % 2 == 0 and vegertek % 2 == 1):
        osszeg = osszeg + i -(i + 1)
        


    else:
        osszeg = osszeg + i -(i + 1)
    
if(osszeg2 != None):
    print(osszeg2)
else:
    print(osszeg)