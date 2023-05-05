class GPU:
    def __init__(self, manufacturer: str, price: int, vram: int, productionYear: int):
        self.manufacturer = manufacturer
        self.price = price
        self.vram = vram
        self.productionYear = productionYear

    def __str__(self) -> str:
        return f"{self.manufacturer}, {self.price} Ft, {self.vram} GB, {self.productionYear}"