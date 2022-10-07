from os import system

name: str = None

print("Kérem adja meg a nevét: ")
name = str(input())

system('cls')

print(f"Üdvözlöm {name}!")