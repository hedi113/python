kezdoertek: int = None
vegertek: int = None
osszeg: int = None

print("Kérem a kezdő értéket: ", end = "")
kezdoertek = int(input())
print("Kérem a végső értéket: ", end = "")
vegertek = int(input())

osszeg = vegertek
for i in range(kezdoertek, vegertek):
        osszeg = osszeg * i
        print(osszeg)