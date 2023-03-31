from console import *
from randomNumbers import *


rnd1 = getRnd(0, 9)
rnd2 = getRnd(40, 50)
rnd3 = getRnd(rnd1, rnd2)

amount = getGuessFromConsole(rnd3)
printResults(amount)
