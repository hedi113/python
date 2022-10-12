from os import system

nev: str = None
gomb: str = None

print("Kérem a nevét: ")
nev = str(input())

print("Nyomjon le egy gombot  a billentyűzeten!")
gomb = str(input())

print(f"Ön, {nev}, a {gomb} billentyűt nyomta meg.")
