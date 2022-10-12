from os import system

egyuttes: str = None
legjobbZene: str = None
hossz: int = None

print("Kérem az együttes nevét: ")
egyuttes = str(input())

print("Kérem a legjobb zeneszám címét: ")
legjobbZene = str(input())

print("Kérem a zene hosszát (perc): ")
hossz = int(input())

print(f"Az ön kedvenc együttesének {egyuttes} a legjobb zeneszáma {legjobbZene} melynek hossza {hossz} perc !")