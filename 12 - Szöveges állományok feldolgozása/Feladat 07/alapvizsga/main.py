from typing import *
from grade import *
from gradeIO import *
from services import *

fileName: str = "data/jegyek.txt"
grades: List[Grade] = getGradesFromFile(fileName)

allGrades = countGrades(grades)
printThingsToConsole(f"{allGrades} diák írt dolgozatot.")

result = sortExamResults(grades, 1)
printThingsToConsole(f"{result} diáknak nem sikerült az alapvizsgája.")

excellentExams = getExcellentExams(grades)
print(f"Jeles eredményt elért tanulók:\n")
printListToConsole(excellentExams)

average = calculateAvarage(grades)
printThingsToConsole(f"10.a osztály átlageredménye: {average:1.2f}")
