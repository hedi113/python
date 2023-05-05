class CPU:
    def __init__(self, manufacturer: str, price: int, coreCounter: int, productionYear: int):
        self.manufacturer = manufacturer
        self.price = price
        self.coreCounter = coreCounter
        self.productionYear = productionYear

    def __str__(self) -> str:
        return f"{self.manufacturer}, {self.price} Ft, {self.coreCounter} db, {self.productionYear}"