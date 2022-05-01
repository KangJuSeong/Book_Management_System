class Book:
    def __init__(self, name: str, author: str, isbn: int, rentaling: bool, location: str):
        __self.name: str = name
        __self.author: str = author
        __self.isbn: int = isbn
        __self.rentaling: bool = rentaling
        __self.location: str = location

    def getName(self) -> str:
        return __self.name

    def getAuthor(self) -> str:
        return __self.author

    def getIsbn(self) -> int:
        return __self.isbn

    def getRentaling(self) -> bool:
        return __self.rentaling

    def getLocation(self) -> str:
        return __self.location

