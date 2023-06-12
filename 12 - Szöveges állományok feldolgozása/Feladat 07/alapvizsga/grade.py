class Grade:
    def __init__(self):
        super().__init__()

        self.firstName: str = None
        self.surName: str = None
        self.division: str = None
        self.grade: int = 0

    def __str__(self) -> str:
        return f"{self.firstName} {self.surName}"
    