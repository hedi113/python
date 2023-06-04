class City:
    def __init__(self):
        super().__init__()

        self.name: str = None
        self.type: str = None
        self.countyName: str = None
        self.jaras: str = None
        self.microRegion: str = None
        self.population: int = 0
        self.area: int = 0

    def __str__(self) -> str:
        return f"{self.name} - {self.type} - {self.countyName} - {self.jaras} - {self.microRegion} - {self.population} - {self.area}"