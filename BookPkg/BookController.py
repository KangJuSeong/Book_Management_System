from ast import keyword
from BookPkg.BookService import BookService


class BookController:
    
    def __init__(self, bid=None):
        self.bs = BookService()
        self.bid = bid
       
    def getBookList(self, keyword=None):
        return self.bs.getBookList(keyword=keyword)
    
    def getBookAttr(self):
        return self.bs.getBookAttr(self.bid)
    
    def deleteBook(self):
        return self.bs.deleteBook(self.bid)
    
    def createBook(self, name, author, isbn, rental, location):
        return self.bs.createBook(name, author, isbn, rental, location)
