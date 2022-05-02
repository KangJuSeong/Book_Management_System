class User:

    def __init__(self, name: str, address: str, phone: str, uid: int, birth_date: str, manager: bool, email: str, password: str):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__uid = uid
        self.__birth_date = birth_date
        self.__manager = manager
        self.__email = email
        self.__password = password

    def getName(self) -> str:
        return self.__name

    def getAddress(self) -> str:
        return self.__address

    def getPhone(self) -> str:
        return self.__phone

    def getUid(self) -> int:
        return self.__uid

    def getBirthDate(self) -> str:
        return self.__birth_date

    def getEmail(self) -> str:
        return self.__email

    def getPassword(self) -> str:
        return self.__password

    def isManager(self) -> bool:
        return self.__manager

