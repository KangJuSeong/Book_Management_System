from .User import _User
from DBPkg.DBManager import _DBManager
from util.IDManager import getID, upID


class UserDBManager(_DBManager, _User):
    
    def __init__(self):
        self.DB_PATH: str = 'DBPkg/csv/UserDB.csv'
        self.UID_PATH: str = 'DBPkg/txt/UserID.txt'
        
    def getUser(self, uid: int) -> _User:
        data = _DBManager._selectDB(db_path=self.DB_PATH, _id=uid)
        return _User(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

    def listUser(self, keyword=None) -> list:
        return _DBManager._selectDB(db_path=self.DB_PATH, keyword=keyword)
    
    def createUser(self, name: str, address: str, phone: str, manager: bool, email: str, password: str) -> int:
        uid: int = getID(self.UID_PATH)
        upID(self.UID_PATH)
        self.user = _User(uid, name, address, phone, manager, email, password)
        uid = _DBManager._insertDB(data=self.user, db_path=self.DB_PATH)
        return uid
    
    def updateUser(self, update_user: _User, uid: int) -> bool:
        return _DBManager._updateDB(data=update_user, db_path=self.DB_PATH, _id=uid)
    
    def deleteUser(self, uid: int) -> bool:
        return _DBManager._deleteDB(db_path=self.DB_PATH, _id=uid)
