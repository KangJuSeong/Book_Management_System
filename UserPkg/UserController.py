from .UserDBManager import UserDBManager
from .User import _User


class UserController(_User):
    
    def __init__(self, user: _User):
        self.user: _User = user
        self.dbm: UserDBManager = UserDBManager()
    
    def getUserAttr(self) -> dict:
        data = {}
        for k, v in self.user.__dict__.items():
            data[k[7:]] = v
        return data
    
    def isManager(self) -> bool:
        return self.user.isManager()

    @staticmethod
    def login(email: str, password: str) -> int:
        user: list = UserDBManager().listUser(keyword=email)
        if user:
            db_password = user[0][-1]
            if password == db_password:
                print('Login Success')
                return user[0][0]
            else:
                print('No Match Password')
                return False
        else:
            print('Not Exist Email')
            return False