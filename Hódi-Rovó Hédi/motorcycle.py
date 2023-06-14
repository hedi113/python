class Motorcycle:
    def __init__(self):
        super().__init__()

        self.manufacturer: str = None
        self.model: str = None
        self.productionYear: int = 0
        self.price: int = 0

    def __str__(self) -> str:
        return f"{self.manufacturer} - {self.model} - {self.productionYear} - {self.price}"
