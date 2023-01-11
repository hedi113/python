kezdoertek: int = None
vegertek: int = None
pszamokosszege: int = None
paratszamokosszege: int = None
pdb: int = None
patlag: float = None

print("Kérem a kezdő értéket: ", end = "")
kezdoertek = int(input())
print("Kérem a végső értéket: ", end = "")
vegertek = int(input())

pszamokosszege = 0
paratszamokosszege = 0
pdb = 0
paratdb = 0
for i in range(kezdoertek, vegertek, 1):
    if(pszamokosszege % 2 == 0):
        pszamokosszege = pszamokosszege + i
    else:
        paratszamokosszege = paratszamokosszege + i

patlag = pszamokosszege + paratszamokosszege/2

print(f"A páros és páratlan számok összegének átlaga: {patlag}")
