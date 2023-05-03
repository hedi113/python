class Motorcycle:
    def __init__(self):
        super().__init__()
        self.manufacture: str = None
        self.type: str = None
        self.model: str = None
        self.fuelConsumption: float = 0
        self.productionYear: int = 0
        self.horsePower: int = 0
        self.cylinders: int = 0
        self.torgue: int = 0
    
    #magic methods
    def __str__(self) -> str:
        return f"{self.manufacture} {self.model} ({self.productionYear})"
