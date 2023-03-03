from mathfunctions import *
from console import *

x: float = None
y: float = None
result: float = None

x = getNumberFromConsole()
y = getNumberFromConsole()

result = sumOfTwoNumbers(x, y)
printToConsole(x, y, result, "+")