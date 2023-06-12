from typing import *
from grade import Grade
import os
from io import open

def getGradesFromFile(fileName: str) -> List[Grade]:
    grades: List[Grade] = []
    grade: Grade = None

    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding='utf-8', mode='r') as file:
            for line in file:
                oneLine = line.strip()
                data = oneLine.split(" ")

                grade = Grade()
                grade.firstName = data[0]
                grade.surName = data[1]
                grade.division = data[2]
                grade.grade = int(data[3])

            
                grades.append(grade)
        return grades
    except FileNotFoundError as ex:
        print(f"{ex.filename}A fájl nem található!")
        return []
    

    
