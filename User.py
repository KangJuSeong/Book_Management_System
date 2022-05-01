class User:

    def __init__(self, name: str, address: str, phone: str, uid: int, birth_date: str, manager: bool, email: str, password: str):
        __self.name = name
        __self.address = address
        __self.phone = phone
        __self.uid = uid
        __self.birth_date = birth_date
        __self.manager = manager
        __self.email = email
        __self.password = password

    def getName(self) -> str:
        return __self.name

    def getAddress(self) -> str:
        return __self.address

    def getPhone(self) -> str:
        return __self.phone

    def getUid(self) -> int:
        return __self.uid

    def getBirthDate(self) -> str:
        return __self.birth_date

    def getEmail(self) -> str:
        return __self.email

    def getPassword(self) -> str:
        return __self.password

    def isManager(self) -> bool:
        return __self.manager

