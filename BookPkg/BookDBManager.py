# from RentalPkg.RentalController import RentalController
from .Book import _Book
from DBPkg.DBManager import _DBManager
from util.IDManager import getID, upID


class BookDBManager(_DBManager, _Book):

    def __init__(self):
        self.DB_PATH: str = 'DBPkg/csv/BookDB.csv'
        self.BID_PATH: str = 'DBPkg/txt/BookID.txt'

    def getBook(self, bid: int) -> _Book:
        data = _DBManager._selectDB(db_path=self.DB_PATH, _id=bid)
        return _Book(data[0], data[1], data[2], data[3], data[4], data[5])
        
    def listBook(self, keyword=None) -> list:
        return _DBManager._selectDB(db_path=self.DB_PATH, keyword=keyword)

    def createBook(self, name: str, author: str, isbn: int, rentaling: bool, location: str) -> int:
        bid: int = getID(self.BID_PATH)
        upID(self.BID_PATH)
        bid = _DBManager._insertDB(data=_Book(bid, name, author, isbn, rentaling, location), db_path=self.DB_PATH)
        return bid

    def updateBook(self, update_book: _Book, bid: int) -> bool:
        return _DBManager._updateDB(data=update_book, db_path=self.DB_PATH, _id=bid)

    def deleteBook(self, bid: int) -> bool:
        from RentalPkg.RentalDBManager import RentalDBManager
        from RentalPkg.RentalController import RentalController
    
        rental = RentalController.getBookRentalList(bid)[0]
        if len(rental):
            RentalDBManager().deleteRental(rental['rid'])
        return _DBManager._deleteDB(db_path=self.DB_PATH, _id=bid)
