class Auto:
    def __init__(self):
        super().__init__()

        self.auto: str = None
        self.mpg: float = 0
        self.cylinder: int = 0
        self.torque: float = 0
        self.horsePower: float = 0
        self.weight: int = 0
        self.speed: float = 0
        self.publicationYear: int = 0
        self.origin: str = None

    def __str__(self) -> str:
        return f"{self.auto} - {self.mpg} - {self.cylinder} - {self.torque} - {self.horsePower} - {self.weight} - {self.speed} - {self.publicationYear} - {self.origin}"