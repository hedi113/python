from mathfunctions import *
from console import *

b = getNumberFromConsole()
x = getChoiceFromConsole()
kelvin = convertToKelvin(b)
fahrenheit = convertToFahrenheit(b)

if(x == 1):
    printResult(kelvin)
if(x == 2):
    printResult2(fahrenheit)
