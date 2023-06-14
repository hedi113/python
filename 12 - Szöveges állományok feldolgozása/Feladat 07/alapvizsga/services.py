from typing import *
from grade import *
from gradeIO import *

def printThingsToConsole(thing: str):
    print(thing)

def printListToConsole(grades: List[Grade]):
    for grade in grades:
        print(grade)

def countGrades(grades: List[Grade]) -> int:
    allGrades: int = len(grades)

    return allGrades

def sortExamResults(grades: List[Grade], sortBy: int) -> int:
    sortExams: List[Grade] = []

    for grade in grades:
        if(grade.grade == sortBy):
            sortExams.append(grade)
    
    result: int = len(sortExams)
    return result

def getExcellentExams(grades : List[Grade]) -> List[Grade]:
    excellentExams: List[Grade] = []

    for grade in grades:
        if(grade.grade == 5):
            excellentExams.append(grade)
    return(excellentExams)

def calculateAvarage(grades: List[Grade]) -> float:
    avarage: float = 0
    sumOfGrades: float = 0

    for grade in grades:
        sumOfGrades += grade.grade
    avarage = sumOfGrades / len(grades)

    return avarage
