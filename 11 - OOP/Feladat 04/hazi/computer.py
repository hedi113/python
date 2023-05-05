from cpu import CPU
from gpu import GPU
from motherboard import Motherboard
from ram import Ram


class Computer:

    def __init__(self, ram: Ram, cpu: CPU, gpu: GPU, motherboard: Motherboard):
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu
        self.motherboard = motherboard
    
    def __str__(self):
        return f"RAM: {self.ram}\nCPU: {self.cpu}\nGPU: {self.gpu}\nMotherboard: {self.motherboard}"




