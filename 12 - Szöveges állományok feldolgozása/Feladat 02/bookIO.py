from book import Book
from typing import *
import os
from io import open

def readBooksFromFile(fileName: str) -> List[Book]:
    books: List[Book] = []

    fileName:str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open("data/adatok.txt",encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip() 
                data = oneLine.split('\t') 

        return books
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []
