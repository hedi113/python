class LegoSet:

        def __init__(self) -> None:
            super().__init__()
            self.pieces: int = 0
            self.buidTime: str = None
            self.number: int = 0
            self.name: str = None
            self.ageGroup: str = None

        def __str__(self) -> str:
              return f"A szett azonosítója: {self.number}\n Neve: {self.name}\n Darabszám: {self.pieces}\n Építésre szükséges min. idő: {self.buidTime}\n Korosztály: {self.ageGroup}"