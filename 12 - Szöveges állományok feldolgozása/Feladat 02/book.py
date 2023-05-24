import datetime

class Book:
    def __init__(self) -> None:
        super.__init__()
        self.writersFirstName: str = None
        self.writersSurName: str = None
        self.writerBirthday: datetime = datetime()
        self.bookTitle: str = None
        self.ISBN: str = None
        self.publisher: str = None
        self.publishYear: int = 0
        self.bookPrice: float = 0
        self.theme: str = None
        self.pageNumber: int = 0
        self.writerHonorarium: float = 0

    def __init__(self) -> str:
        return f"{self.writersFirstName} - {self.writersSurName} - {self.bookTitle} - {self.publishYear}" 