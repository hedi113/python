class Milk:

    def __init__(self, bestBefore: str, capacity: int, amount: int, manufacturer: str) -> None:
        self.bestBefore = bestBefore
        self.capacity = capacity
        self.amount = amount
        self.manufacturer = manufacturer

    def __str__(self) -> str:
        return f"\n\tMennyiség: {self.amount}\n\tKiszerelés: {self.capacity}l\n\tGyártó: {self.manufacturer}\n\tFogyasztható: {self.bestBefore}"
    