from typing import *
from student import Student

def calculateAvarage(students: List[Student]) -> float:
    sum: float = 0

    for student in students:
        sum += student.avarage

    return sum / len(students)

def getBestStudent(students: List[Student]) -> Student:
    bestStudent: Student = students[0] #referencia ertek

    for index in range(1, len(students), 1):
        if(students[index].avarage > bestStudent.avarage):
            bestStudent = students[index]

    return bestStudent

def studentsAboveAverage(students: List[Student], classAverage: float) -> List[Student]:
    aboveAverage: List[Student] = []

    for student in students:
        if(student.avarage >= classAverage):
            aboveAverage.append(student)

    return aboveAverage