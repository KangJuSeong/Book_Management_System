from .Book import _Book
from DBPkg.DBManager import _DBManager


class BookManager(_DBManager, _Book):

    def __init__(self):
        self.book = None
        self.DB_PATH = 'DBPkg/csv/BookDB.csv'
        self.BID_PATH = 'DBPkg/txt/BookID.txt'

    def listBook(self, keyword=None):
        rows = _DBManager._selectDB(db_path=self.DB_PATH, keyword=keyword)
        return rows

    def createBook(self, name: str, author: str, isbn: int, rentaling: bool, location: str):
        self.book = _Book(name, author, isbn, rentaling, location)
        bid = self.getBID()
        _DBManager._insertDB(data=self.book, db_path=self.DB_PATH, _id=bid)

    def updateBook(self, name: str, author: str, isbn: int, rentaling: bool, location: str, bid: int):
        self.book = _Book(name, author, isbn, rentaling, location)
        return _DBManager._updateDB(data=self.book, db_path=self.DB_PATH, _id=bid)

    def deleteBook(self, bid: int):
        return _DBManager._deleteDB(db_path=self.DB_PATH, _id=bid)
        
 
    def getBID(self):
        bid = 0
        with open(self.BID_PATH, 'r') as f:
            bid = int(f.readline())
        with open(self.BID_PATH, 'w') as f:
            f.write(str(bid+1))
        return bid
