number: int = 0
final: int = 0

szum = 0
steps = 0

while(final < 100):
    print("Adja meg a határértéket (min.: 100): ", end="")
    final = int(input())

while(szum < final):
    print("Adjon meg egy számot: ", end="")
    number = int(input())

    if(number > 0):
        szum = szum + number
        steps = steps + 1
        print(f"A jelenlegi összeg: {szum}")
    if(szum >= final):
        print(f"Ennyi lépésben érte el a határértéket({final}): {steps}")   




