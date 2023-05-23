from typing import *
from model.student import Student
from fileIO import studentIO
from service import *

students: List[Student] = studentIO()

print("Az osztály tanulói: ")
for student in students:
    print(student)

countOfClass: int = len(students)
print(f"\n\n Az osztálynak {countOfClass} tanuloja van.\n\n")

classAvarage: float = calculateAverage(students)
print(f"Az osztály átlaga: {classAvarage:1.2f}")

bestStudent: Student = getBestStudent(students)
print(f"A legjobb tanuló: {bestStudent}")



