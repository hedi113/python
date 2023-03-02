name: str = None
birthdate: int = None
currentDate: int = 2023


print("Név: ", end="")
name = str(input())

print("Születési dátum: ", end="")
birthdate = int(input())

def yourName(name: str) -> None:
    return name
def subtract(birthdate: int, currentDate) -> int:
    return currentDate-birthdate
age = subtract(birthdate,currentDate)
name = yourName(name)
print(f"{name} ön az idén {age} éves.")