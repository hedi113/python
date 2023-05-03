class Computer:
    def __init__(self):
        super.__init__()
    class Manufacture:
        def __init__(self):
            super.__init__()
            self.manufacture: str = None
    class Processor:
        def __init__(self):
            super.__init__()
            self.processor: str = None
    class VideoCard:
        def __init__(self):
            super.__init__()
            self.videoCard: str = None
    class HardDrive:
        def __init__(self):
            super.__init__()
            self.hardDrive: str = None
    class Motherboard:
        def __init__(self):
            super.__init__()
            self.motherboard: str = None
    def __str__(self) -> str:
        return f"{self.HardDrive}, {self.Manufacture}, {self.Motherboard}, {self.Processor}, {self.VideoCard}"