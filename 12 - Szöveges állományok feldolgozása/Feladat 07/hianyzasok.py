from services import *

hianyzasokSzama: int = 0
nev: str = None

while(nev == None or hianyzasokSzama == 0):
        print("Adja meg a tanuló nevét: ", end="")
        nev = input()
        if(nev == ''):
                break
        print(f"Adja meg {nev} igazolatlan hiányzásainak számát: ", end="")
        hianyzasokSzama = int(input())

        hianyzasok = hianyzasok(hianyzasokSzama)
        print(f"{nev}: {hianyzasok}")
        nev: str = None
    




