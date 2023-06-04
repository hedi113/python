class Film:

    def __init__(self):
        super().__init__()

        self.name: str = None
        self.genre: str = None
        self.distributor: str = None
        self.viewerRating: int = 0
        self.payOff: float = 0
        self.rottenTomatoes: int = 0
        self.income: float = 0
        self.releaseYear: int = 0

    def __str__(self) -> str:
        return f"{self.name} - {self.genre} - {self.distributor} - {self.viewerRating} - {self.payOff} - {self.rottenTomatoes} - {self.income} - {self.releaseYear}"
    