from book import Book
from typing import *
from bookIO import readBooksFromFile
from services import *

fileName:str = "data/adatok.txt"
books: List[Book] = readBooksFromFile(fileName)

#Írjuk ki a képernyőre az össz adatot
writeToConsole(books)