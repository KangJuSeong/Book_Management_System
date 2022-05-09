from .BookDBManager import BookDBManager
from .Book import _Book


class BookController(_Book):
    
    def __init__(self, book: _Book):
        self.book: _Book = book
        self.dbm: BookDBManager = BookDBManager()
        
    def getBook(self) -> _Book:
        return self.book

    def rentalBook(self) -> None:
        self.book.onRentaling()
        
    def returnBook(self) -> None:
        self.book.offRentaling()
 
    def isRentaling(self) -> bool:
        return self.book.getRentaling()

    def getBookAttr(self) -> dict:
        data = {}
        for k, v in self.book.__dict__.items():
            data[k[7:]] = v
        return data
            
