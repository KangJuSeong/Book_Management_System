from .User import _User
from DBPkg.DBManager import _DBManager
from util.IDManager import getID, upID


class UserManager(_DBManager, _User):
    
    def __init__(self):
        self.user: _User = None  # type: ignore
        self.DB_PATH: str = 'DBPkg/csv/UserDB.csv'
        self.UID_PATH: str = 'DBPkg/txt/UserID.txt'
        
    def getUser(self, uid: int) -> list:
        return _DBManager._selectDB(db_path=self.DB_PATH, _id=uid)

    def listUser(self, keyword=None) -> list:
        rows: list = _DBManager._selectDB(db_path=self.DB_PATH, keyword=keyword)
        return rows
    
    def createUser(self, name: str, address: str, phone: str, manager: bool, email: str, password: str) -> int:
        duplicate_email: list = self.listUser(keyword=email)
        if duplicate_email:
            print("Duplicate User Email")
            return False
        self.user = _User(name, address, phone, manager, email, password)
        uid: int = getID(self.UID_PATH)
        upID(self.UID_PATH)
        udi = _DBManager._insertDB(data=self.user, db_path=self.DB_PATH, _id=uid)
        return uid
    
    def updateUser(self, name: str, address: str, phone: str, manager: bool, email: str, password: str, uid: int) -> bool:
        return True
    
    def deleteUser(self, uid: int) -> bool:
        return True
 