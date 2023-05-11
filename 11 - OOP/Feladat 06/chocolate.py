class Chocolate:

    def __init__(self, bestBefore: str, weight: int, amount: int, manufacturer: str) -> None:
        self.bestBefore = bestBefore
        self.weight = weight
        self.amount = amount
        self.manufacturer = manufacturer

    def __str__(self):
        return f"\n\tMennyiség: {self.amount}\n\tSúly: {self.weight}g\n\tGyártó: {self.manufacturer}\n\tFogyasztható: {self.bestBefore}"
    