from ast import keyword
from UserPkg.UserService import UserService
from RentalPkg.RentalService import RentalServie

class UserController:
    
    def __init__(self, uid=None) -> None:
        self.us = UserService()
        self.rs = RentalServie()
        self.uid = uid
    
    def login(self, email: str, password: str) -> int:
        return self.us.login(email, password)
        
    def signup(self, name: str, address: str, phone: str, manager: bool, email: str, pw: str):
        return self.us.signup(name, address, phone, manager, email, pw)
        
    def getUserAttr(self):
        return self.us.getAttr(self.uid)
    
    def getUserRentalList(self):
        return self.rs.getUserRentalList(uid=self.uid)
   
    def rentalBook(self, bid):
        return self.rs.rentalBook(self.uid, bid)
    
    def returnBook(self, rid):
        return self.rs.returnBook(rid)
    
    def getUserList(self, keyword=None):
        return self.us.getUserList(keyword=keyword)
    
    def getManagerCode(self):
        with open("DBPkg/txt/ManagerCode.txt") as f:
            code = f.readline()
            return code
    