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
        return _DBManager._selectDB(db_path=self.DB_PATH, keyword=keyword)
    
    def createUser(self, name: str, address: str, phone: str, manager: bool, email: str, password: str) -> int:
        duplicate_email: list = self.listUser(keyword=email)
        if duplicate_email:
            print("Duplicate User Email")
            return False
        uid: int = getID(self.UID_PATH)
        upID(self.UID_PATH)
        self.user = _User(uid, name, address, phone, manager, email, password)
        uid = _DBManager._insertDB(data=self.user, db_path=self.DB_PATH)
        return uid
    
    def updateUser(self, name: str, address: str, phone: str, manager: bool, email: str, password: str, uid: int) -> bool:
        self.user = _User(uid, name, address, phone, manager, email, password)
        return _DBManager._updateDB(data=self.user, db_path=self.DB_PATH, _id=uid)
    
    def deleteUser(self, uid: int) -> bool:
        return _DBManager._deleteDB(db_path=self.DB_PATH, _id=uid)

    def login(self, email: str, password: str) -> bool:
        user: list = self.listUser(keyword=email)
        if user:
            db_password = user[0][-1]
            if password == db_password:
                print('Login Success')
                return True
            else:
                print('No Match Password')
                return False
        else:
            print('Not Exist Email')
            return False
