text: str = "alma"
text2: str = "álmatlan"
count: int = text.count("a")
count2: int = text.count("l")
count3: int = text.count("m")
count4: int = text2.count("a")
count5: int = text2.count("l")
count6: int = text2.count("m")

def printToConsole(result: int) -> int:
    print(result)