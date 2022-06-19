from UserPkg.UserService import UserService


class UserController:
    
    def __init__(self, uid=None) -> None:
        self.us = UserService()
        self.uid = uid
    
    def login(self, email: str, password: str) -> int:
        return self.us.login(email, password)
        
    def signup(self, name: str, address: str, phone: str, manager: bool, email: str, pw: str):
        return self.us.signup(name, address, phone, manager, email, pw)
        
    def getManagerCode(self):
        with open("DBPkg/txt/ManagerCode.txt") as f:
            code = f.readline()
            return code
    