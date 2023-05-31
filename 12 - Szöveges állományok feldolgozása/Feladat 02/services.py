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
