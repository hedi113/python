numOne: int = None
numTwo: int = None
operation: int = None
sum: int = None
difference: int = None
product: int = None
result: float = None

print("Adja meg az értékét az első számnak!")
numOne = int(input())
print("Adja meg az értékét a második számnak!")
numTwo = int(input())

print("Válasszon műveletet!")
print(" 1 - Összeadás \n 2 - Kivonás \n 3 - Szorzás \n 4 - Osztás")

operation = int(input())

def add(numOne: int, numTwo: int) -> int:
    return numOne+numTwo

def subtract(numOne: int, numTwo: int) -> int:
    return numOne-numTwo

def multiply(numOne: int, numTwo: int) -> int:
    return numOne*numTwo

def divide(numOne: float, numTwo: float) -> float:
    return numOne/numTwo

match operation:
    case 1:
        sum=add(numOne,numTwo)
        print(f"A két szám összege: {sum}")
    case 2:
        difference=subtract(numOne,numTwo)
        print(f"A két szám különsége: {difference}")
    case 3:
        product=multiply(numOne,numTwo)
        print(f"A két szám szorzata: {product}")
    case 4:
        result=divide(numOne,numTwo)
        print(f"A két szám osztási eredménye: {result}")
