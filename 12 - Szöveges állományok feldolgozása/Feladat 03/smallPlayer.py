class SmallPlayer:

    def __init__(self):
        super().__init__()

        self.name: str = None
        self.height: int = 0
        self.heightDifference: float = 0

    def __str__(self) -> str:
        return f"{self.name} - {self.height} - {self.heightDifference}"