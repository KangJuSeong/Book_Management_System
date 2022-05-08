from .Rental import _Rental
from DBPkg.DBManager import _DBManager
from util.IDManager import getID, upID
import time


class RentalManager(_DBManager, _Rental):
    
    def __init__(self):
        self.rental: _Rental = None # type: ignore
        self.DB_PATH: str = 'DBPkg/csv/Rental.csv'
        self.RID_PATH: str = 'DBPkg/txt/RentalID.txt'
    
    def getRental(self, rid: int) -> list:
        return _DBManager._selectDB(db_path=self.DB_PATH, _id=rid)
    
    def listRental(self, keyword=None) -> list:
        return _DBManager._selectDB(db_path=self.DB_PATH, keyword=keyword)
    
    def createRental(self, bid: int, uid: int) -> int:
        rental_date: str = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
        rid: int = getID(self.RID_PATH)
        upID(self.RID_PATH)
        self.rental = _Rental(rid, bid, uid, True, rental_date)
        rid = _DBManager._insertDB(data=self.rental, db_path=self.DB_PATH)
        return rid
        