from cpu import CPU
from gpu import GPU
from motherboard import Motherboard
from ram import Ram
from computer import Computer

computerProcessor: CPU = CPU("Ryzen", 92000, 6, "2010")
computerGraphicsCard: GPU = GPU("GeForce", 157000, 6, 2009)
computerRam: Ram = Ram("G.SKILL", 72000, 32, 2013)
computerMotherboard: Motherboard = Motherboard("ASUS", 35000, "B450-PLUS", 2003)

computer: Computer = Computer(computerRam, computerProcessor, computerGraphicsCard, computerMotherboard)

print(computer)