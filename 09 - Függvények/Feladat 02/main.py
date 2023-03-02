name: str = None


print("Kérem a nevét: ", end="")
name = str(input())

def something(name: str) -> None:
    print(f"Üdvözlöm, {name}!")

something(f"{name}")
