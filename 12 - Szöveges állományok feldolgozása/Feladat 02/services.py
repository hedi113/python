from book import Book
from typing import *

def writeToConsole(books: List[Book]) -> None:
    for book in books:
        print(book)