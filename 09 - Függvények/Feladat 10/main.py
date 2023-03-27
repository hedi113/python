from console import *
from randomNumbers import *

rnd1 = getRnd1()
rnd2 = getRnd2()
rnd3 = generateRndBetween(rnd1, rnd2)

guess = getGuessFromConsole(rnd3)
amount = howManyTries(0, guess, rnd3)
