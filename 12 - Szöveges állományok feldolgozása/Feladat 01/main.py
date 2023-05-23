from typing import *
from student import Student
from studentIO import importStudents, writeStudentsInFile
from services import *

students: List[Student] = importStudents()

#1 - Írjuk ki minden diák adatát a képernyőre!
print("Az osztaly tanuloi:")
for student in students:
    print(student)

#2 - Hány diák jár az osztályba?
countOfClass: int = len(students)
print(f"\n\nAz osztalynak {countOfClass} tanulojja van.\n\n")

#3 - Mennyi az osztály átlaga?
classAvarage: float = calculateAvarage(students)
print(f"Az osztaly atlaga: {classAvarage:1.2f}")

#4 - Keressük a legtöbb pontot elért érettségizőt és írjuk ki az adatait a képernyőre.
bestStudent: Student = getBestStudent(students)
print(f"A legjobb tanulo: {bestStudent}")

#5 - atlagfelett.txt allományba keressük ki azon tanulókat kiknek pontjai meghaladják az átlagot!
aboveAvarage: List[Student] = studentsAboveAverage(students, classAvarage)
writeStudentsInFile(aboveAvarage, "atlagfelett.txt")
#6 - Van e kitünő tanulónk?

"""
7 - Hány elégtelen, elégséges, jó, jeles és kitünő tanuló van az osztályban?
    Értékhatárok:
 - elégtelen, ha: 0.00 - 1.99
 - elégséges, ha: 2.00 - 2.99
 - jó, ha: 3.00 - 3.99
 - jeles, ha: 4.00 - 4.99
 - kitünő, ha: 5.00
 """