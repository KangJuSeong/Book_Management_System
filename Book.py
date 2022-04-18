class Book:
    def __init__(self, name: str, author: str, isbn: int, rentaling: bool, location: str):
        self.name: str = name
        self.author: str = author
        self.isbn: int = isbn
        self.rentaling: bool = rentaling
        self.location: str = location

    def getName(self) -> str:
        return self.name

    def getAuthor(self) -> str:
        return self.author

    def getIsbn(self) -> int:
        return self.isbn

    def getRentaling(self) -> bool:
        return self.rentaling

    def getLocation(self) -> str:
        return self.location