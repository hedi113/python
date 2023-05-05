class Ram:
    def __init__(self, manufacturer: str, price: int, capacity: int, productionYear: int):
        self.manufacturer = manufacturer
        self.price = price
        self.capacity = capacity
        self.productionYear = productionYear

    def __str__(self) -> str:
        return f"{self.manufacturer}, {self.price} Ft, {self.capacity} GB, {self.productionYear}"