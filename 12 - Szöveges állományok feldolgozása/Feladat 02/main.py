from book import Book
from typing import *
from bookIO import *
from services import *

fileName:str = "data/adatok.txt"
books: List[Book] = readBooksFromFile(fileName)

#Írjuk ki a képernyőre az össz adatot
writeToConsole(books)

#Keressük ki az informatika témajú könyveket és mentsük el őket az informatika.txt állömányba
allFilteredBooks: List[Book] = getFilteredBooks(books, "informatika")
writeBooksInFile(allFilteredBooks, "informatika.txt")
#Az 1900.txt állományba mentsük el azokat a könyveket amelyek az 1900-as években íródtak
bookPBYear: List[Book] = PBYears(books, 1900, 2000)
writeBooksInFile(bookPBYear, "1900.txt")
#Rendezzük az adatokat a könyvek oldalainak száma szerint csökkenő sorrendbe és a sorbarakott.txt állományba mentsük el.
sortBooksByPageNumberDescending(books)
writeBooksInFile(books, "sorbarakott.txt") 