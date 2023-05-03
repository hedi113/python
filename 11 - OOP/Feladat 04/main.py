from computer import Computer

component1: Computer.HardDrive = Computer()
component2: Computer.Manufacture = Computer()
component3: Computer.Motherboard = Computer()
component4: Computer.VideoCard = Computer()
component5: Computer.Processor = Computer()

component1.hardDrive = "Toshiba P300"
component2.manufacture = "ASUS"
component3.motherboard = "ASUS Prime B550M-a"
component4.videoCard = "ASUS GeForce Dual V2 RTX"
component5.processor = "AMD Ryzen 5 5600 6-Core"

print(f"{component1} {component2} {component3} {component4} {component5}")
