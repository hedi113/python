from os import system

szuletesiEv: int = None
nev: str = None

print("Kérem adja meg a nevét: ")
nev = str(input())
print("Kérem adja meg a születési évszámát: ")
szuletesiEv = int(input())

system('cls')

print(f"{nev}, ön {szuletesiEv} született!")


