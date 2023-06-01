class Player:

    def __init__(self):
        super().__init__()
        
        self.name: str = None
        self.height: int = 0
        self.post: str = None
        self.nationality: str = None
        self.team: str = None
        self.country: str = None

    def __str__(self) -> str:
        return f"{self.name} - {self.height} : {self.post} : {self.team} : {self.nationality} : {self.country}"
    