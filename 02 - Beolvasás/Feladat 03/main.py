from os import system
from tkinter.messagebox import NO

nev: str = None
magassag: float = None

print("Kérem adja meg a nevét: ")
nev = str(input())

print("Kérem adja meg a magasságát (méter): ")
magassag = float(input())

system('cls')

print(f"{nev}, az ön magassága {magassag}m")