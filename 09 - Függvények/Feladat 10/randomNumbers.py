import random

def getRnd1() -> int:
    rnd: int = random.randint(0, 9)
    return rnd

def getRnd2() -> int:
    rnd: int = random.randint(40, 50)
    return rnd

def generateRndBetween(a: int, b: int) -> int:
    rnd: int = random.randint(a, b)
    return rnd