import datetime

class Book:
    def __init__(self):
        super().__init__()
        self.writerFirstName: str = None
        self.writerSurName: str = None
        self.writerBirthday: datetime = None
        self.bookTitle: str = None
        self.ISBN: str = None
        self.publisher: str = None
        self.publishYear: int = 0
        self.bookPrice: float = 0
        self.theme: str = None
        self.pageNumber: int = 0
        self.writerHonorarium: float = 0

    def __str__(self) -> str:
        return f"{self.writerFirstName} {self.writerSurName} - {self.bookTitle} [{self.publishYear}]"