from typing import *
from io import open
import os
from model.student import Student

fileName:str = "data/adatok.txt"
basepath: str = os.path.dirname(os.path.abspath(__file__))
fileFullPath: str = os.path.join(basepath, fileName)

oneLine:str = None
data: List[str] = []
students: List[Student]=[]
student: Student = None

try:
    with open(fileFullPath,encoding="utf-8", mode="r") as file:
        for line in file:
            oneLine = line.strip() #Antalfai Martin	3,53
            data = oneLine.split('\t') #tabulátorral lesz elválasztva
            
            #data[0] = Antalfali Martin
            #data[1] = 3,53
            
            student = Student()
            student.name = data[0]
            student.average = float(data[1].replace(',', '.'))


            students.append(student)
except FileNotFoundError as ex:
    print(f"{ex.filename} nem található!")

for line in students:
    print(f"{line}")