class Student:
    def __init__(self):
        super().__init__()

        self.name: str = None
        self.avarage: float = 0

    def __str__(self) -> str:
        return f"{self.name} : {self.avarage}"