from .Rental import _Rental
from DBPkg.DBManager import _DBManager
from util.IDManager import getID, upID
import time


class RentalDBManager(_DBManager, _Rental):
    
    def __init__(self):
        self.DB_PATH: str = 'DBPkg/csv/RentalDB.csv'
        self.RID_PATH: str = 'DBPkg/txt/RentalID.txt'
    
    def getRental(self, rid: int) -> _Rental:
        data = _DBManager._selectDB(db_path=self.DB_PATH, _id=rid)
        return _Rental(data[0], data[1], data[2], data[3], data[4])
    
    def listRental(self, keyword=None) -> list:
        return _DBManager._selectDB(db_path=self.DB_PATH, keyword=keyword)
    
    def createRental(self, bid: int, uid: int) -> int:
        rental_date: str = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
        rid: int = getID(self.RID_PATH)
        upID(self.RID_PATH)
        rid = _DBManager._insertDB(data=_Rental(rid, bid, uid, True, rental_date), db_path=self.DB_PATH)
        return rid
    
    def deleteRental(self, rid: int) -> bool:
        return _DBManager._deleteDB(db_path=self.DB_PATH, _id=rid)
