from UserPkg.UserDBManager import UserDBManager



class UserService:
    
    def __init__(self):
        self.udm = UserDBManager()
        
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