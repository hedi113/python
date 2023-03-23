def getWordFromConsole() -> str:
    word: str = None
    while(word == None):
        print("Kérek egy szót: ", end="")
        word = str(input())

    return word

def findSameLetters() -> int:
    firstword: str = None
    secondword: str = None
    intersection = ""
    for x in firstword:
        if(secondword.find(x) > 0 and intersection.find(x) == -1):
            intersection += x
    return intersection

def printToConsole(sameLetter: int) -> None:
    print(f"Ennyi ugyanojan betű van a két szóban: {sameLetter}")
