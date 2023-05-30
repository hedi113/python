from book import Book
from typing import *
from bookIO import *

def writeToConsole(books: List[Book]) -> None:
    for book in books:
        print(book)


def typeInformatycs(books: List[Book]) -> List[Book]:
    allInfBooks: List[Book] = []

    for book in books:
        if(book.theme == "informatika"):
            allInfBooks.append(book)
        
    return allInfBooks

def PBYears(books: List[Book]) -> List[Book]:
    bookPBYear: List[Book] = []

    for book in books:
        if(book.publishYear >= 1900 and book.publishYear < 2000):
            bookPBYear.append(book)
        
    return bookPBYear

def pages(books: List[Book]) -> List[Book]:
    sortedList: List[Book] = []

    for book in books:
        if(book.pageNumber):
            sortedList.append(book)
            sortedList = sorted(book.pageNumber, reverse=True)


    return sortedList

