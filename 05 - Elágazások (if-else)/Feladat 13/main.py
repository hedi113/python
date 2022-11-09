szam: int = None

print("Kérem a számot: ", end="")
szam = int(input())

if szam >= 0 and szam <= 9:
    print("A szám egyjegyű.")
elif szam >= 10 and szam <= 99:
    print("A szám kétjegyű.")
elif szam >= 100 and szam <= 999:
    print("A szám háromjegyű.")
else:
    print("A szám már 4 vagy több jegyű.")
