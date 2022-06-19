from UserPkg.UserDBManager import UserDBManager
from UserPkg.User import _User
from RentalPkg.RentalService import RentalServie


class UserService(_User):
    
    def __init__(self):
        self.udm = UserDBManager()
        self.rs = RentalServie()
                
    def login(self, email: str, password: str):
        user: list = self.udm.listUser(keyword=email)
        if user:
            db_password = user[0][-1]
            if password == db_password: return user[0][0]
            else: return False
        else: return False
        
    def signup(self, name: str, address: str, phone: str, manager: bool, email: str, pw: str):
        duplicate_email: list = self.udm.listUser(keyword=email)
        if duplicate_email: return -2 
        if not '@' in email: return -3
        return self.udm.createUser(name, address, phone, manager, email, pw)
    
    def getAttr(self, uid: int):
        user = self.udm.getUser(uid=uid)
        return {'uid': user.getUid(),
                'name': user.getName(),
                'address': user.getAddress(),
                'phone': user.getPhone(),
                'manager': user.getManager(),
                'email': user.getEmail()}
        
    def getUserList(self, keyword=None):
        return self.udm.listUser(keyword=keyword)
        