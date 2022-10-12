from os import system

megjelenesiEv: int = None
rendezoNeve: str = None
filmcim: str = None
foszereploNeve: str = None

print("Kérem a megjelenési évet: ")
megjelenesiEv = int(input())

print("Kérem a rendező nevét: ")
rendezoNeve = str(input())

print("Kérem a film címét: ")
filmcim = str(input())

print("Kérem a főszereplő nevét: ")
foszereploNeve = str(input())

print(f"{megjelenesiEv}-ban {rendezoNeve} rendezésében megjelent a/az {filmcim} című film {foszereploNeve} főszereplésével!")