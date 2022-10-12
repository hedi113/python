from os import system

marka: str = None
modell: int = None
tipus: str = None
kobcenti: int = None

print("Kérem az autó márkáját: ")
marka = str(input())

print("Kérem az autó modelljét: ")
modell = int(input())

print("Kérem az autó típusát: ")
tipus = str(input())

print("Kérem a köbcenti értékét: ")
kobcenti = int(input())

print(f"Márka: {marka}\n Modell: {modell}\n Típus: {tipus}\n Köbcenti: {kobcenti}\n")