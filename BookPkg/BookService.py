from BookPkg.BookDBManager import BookDBManager
from BookPkg.Book import _Book

from RentalPkg.RentalService import RentalServie
from RentalPkg.RentalDBManager import RentalDBManager

class BookService(_Book):
    
    def __init__(self):
        self.bm = BookDBManager()
        
    def getBookList(self, keyword=None):
        return self.bm.listBook(keyword=keyword)
    
    def getBookAttr(self, bid: int):
        book = self.bm.getBook(bid=bid)
        return {'bid': book.getBid(),
                'name': book.getName(),
                'author': book.getAuthor(),
                'isbn': book.getIsbn(),
                'rentaling': book.getRentaling(),
                'location': book.getLocation()}
        
    def deleteBook(self, bid):
        rental_list = RentalServie().getBookRentalList(bid)
        for rental in rental_list:
            RentalDBManager().deleteRental(rental)
        return self.bm.deleteBook(bid)
    
    def createBook(self, name, author, isbn, rental, location):
        self.bm.createBook(name, author, isbn, rental, location)