from .BookDBManager import BookDBManager
from .Book import _Book


class BookController(_Book):
    
    def __init__(self, book: _Book):
        self.book: _Book = book
        self.dbm: BookDBManager = BookDBManager()
        
    def getBook(self) -> _Book:
        return self.book

    def rentalBook(self) -> bool:
        if self.book.getRentaling():
            return False
        else:
            self.book.onRentaling()
            return True
        
    def returnBook(self) -> bool:
        if not self.book.getRentaling():
            return False
        else:
            self.book.offRentaling()
            return True

    def isRentaling(self) -> bool:
        return self.book.getRentaling()

    def getBookAttr(self) -> dict:
        data = {}
        for k, v in self.book.__dict__.items():
            getter = getattr(self.book, f"get{k[7].upper()}{k[8:]}")
            data[k[7:]] = getter()
        return data
