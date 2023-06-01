from book import Book
from typing import *
from bookIO import *

def writeToConsole(books: List[Book]) -> None:
    for book in books:
        print(book)


def getFilteredBooks(books: List[Book], theme: str) -> List[Book]:
    allFilteredBooks: List[Book] = []

    for book in books:
        if(book.theme == theme):
            allFilteredBooks.append(book)
        
    return allFilteredBooks

def PBYears(books: List[Book], start: int, end: int) -> List[Book]:
    bookPBYear: List[Book] = []

    for book in books:
        if(book.publishYear >= start and book.publishYear < end):
            bookPBYear.append(book)
        
    return bookPBYear

def sortBooksByPageNumberDescending(books: List[Book]) -> None: #csokkeno sorrend
    booksCount: int = len(books)
    temp: int = None

    for i in range(0, booksCount -1, 1):
        for j in range(i + 1, booksCount, 1):
            if(books[j].pageNumber > books[i].pageNumber): #ha novekvo sorrendet szeretnenk, csak a kacsacsor iranyat kell megvaltoztatni
                
                temp = books[i]
                books[j] = books[j]
                books[j] = temp

