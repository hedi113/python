from services import *

hianyzasokSzama: int = 0
nev: str = None

while(nev == None or hianyzasokSzama == 0):
        print("Adja meg a tanuló nevét: ", end="")
        nev = input()
        if(nev == ''):
                break
        print("Adja meg a tanuló igazolatlan hiányzásainak számát: ", end="")
        hianyzasokSzama = int(input())

        hianyzasok(hianyzasokSzama, nev)
        nev: str = None
    




