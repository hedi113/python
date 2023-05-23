import os
from typing import *
from io import open
from student import Student


def importStudents() -> List[Student]:
    fileName:str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    oneLine:str = None
    data:List[str] = []
    students:List[Student]=[]
    student: Student = None

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip() #Antalfai Martin	3,53
                data = oneLine.split('\t') #tabulátorral elválasztva
                
                #data[0] = Antalfai Martin
                #data[1] = 3,53

                student = Student()
                student.name = data[0]
                student.avarage = float(data[1].replace(',', '.'))

                students.append(student)
        
        return students
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []

def writeStudentsInFile(students: List[Student], fileName: str) -> None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open (fileFullPath, encoding='utf-8', mode="w") as file:
            for student in students:
                file.write(f"{student} : {student.avarage}\n")
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem talalhato!")

