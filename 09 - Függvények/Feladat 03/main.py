from console import *
from mathfunctions import *

name: str = getNameFromConsole()
age: int = getAgeFromConsole()
result: int = substractAge(age)
printWelcomeMessage(name, result)
