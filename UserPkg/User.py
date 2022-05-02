class _User:

    def __init__(self, name: str, address: str, phone: str, manager: bool, email: str, password: str):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__manager = manager
        self.__email = email
        self.__password = password

    def getName(self) -> str:
        return self.__name

    def getAddress(self) -> str:
        return self.__address

    def getPhone(self) -> str:
        return self.__phone

    def getEmail(self) -> str:
        return self.__email

    def getPassword(self) -> str:
        return self.__password

    def isManager(self) -> bool:
        return self.__manager

