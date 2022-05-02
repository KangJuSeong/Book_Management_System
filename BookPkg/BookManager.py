from .Book import _Book
from DBPkg.DBManager import _DBManager
from util.IDManager import getID, upID


class BookManager(_DBManager, _Book):

    def __init__(self):
        self.book: _Book = None  # type: ignore
        self.DB_PATH: str = 'DBPkg/csv/BookDB.csv'
        self.BID_PATH: str = 'DBPkg/txt/BookID.txt'

    def listBook(self, keyword=None) -> list:
        rows: list = _DBManager._selectDB(db_path=self.DB_PATH, keyword=keyword)
        return rows

    def createBook(self, name: str, author: str, isbn: int, rentaling: bool, location: str):
        self.book = _Book(name, author, isbn, rentaling, location)
        bid: int = getID(self.BID_PATH)
        upID(self.BID_PATH)
        _DBManager._insertDB(data=self.book, db_path=self.DB_PATH, _id=bid)

    def updateBook(self, name: str, author: str, isbn: int, rentaling: bool, location: str, bid: int) -> bool:
        self.book = _Book(name, author, isbn, rentaling, location)
        return _DBManager._updateDB(data=self.book, db_path=self.DB_PATH, _id=bid)

    def deleteBook(self, bid: int) -> bool:
        return _DBManager._deleteDB(db_path=self.DB_PATH, _id=bid)
