from console import *
from mathfunctions import *

a = getNumberFromConsole()
b = getChoiceFromConsole()
chfResult = convertToCHF(a)
jpyResult = convertToJPY(a)
usdResult = convertToUSD(a)
chfToEur = convertCHFtoEUR(chfResult)
jpyToEur = convertJPYtoEUR(jpyResult)
usdToEur = convertUSDtoEUR(usdResult)

if(b == 1):
    printUSDtoConsole(usdResult)
    printEURtoConsole(usdToEur)
elif(b == 2):
    printJPYtoConsole(jpyResult)
    printEURtoConsole(jpyToEur)
else:
    printCHFtoConsole(chfResult)
    printEURtoConsole(chfToEur)
