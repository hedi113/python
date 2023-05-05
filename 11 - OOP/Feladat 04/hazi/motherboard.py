class Motherboard:
    def __init__(self, manufacturer: str, price: int, model: str, productionYear: int):
        self.manufacturer = manufacturer
        self.price = price
        self.model = model
        self.productionYear = productionYear

    def __str__(self) -> str:
        return f"{self.manufacturer}, {self.price} Ft, {self.model}, {self.productionYear}"