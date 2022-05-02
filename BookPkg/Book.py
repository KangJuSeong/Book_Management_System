class _Book:
    def __init__(self, name: str, author: str, isbn: int, rentaling: bool, location: str):
        self.__name: str = name
        self.__author: str = author
        self.__isbn: int = isbn
        self.__rentaling: bool = rentaling
        self.__location: str = location

    def getName(self) -> str:
        return self.__name

    def getAuthor(self) -> str:
        return self.__author

    def getIsbn(self) -> int:
        return self.__isbn

    def getRentaling(self) -> bool:
        return self.__rentaling

    def getLocation(self) -> str:
        return self.__location
