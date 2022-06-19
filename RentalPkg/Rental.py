class _Rental:
    
    def __init__(self, rid: int, bid: int, uid: int, rental: bool, date: str):
        self.__rid: int = rid
        self.__bid: int = bid
        self.__uid: int = uid
        self.__rental: bool = rental
        self.__date: str = date
        
    def getRid(self) -> int:
        return self.__rid
    
    def getBid(self) -> int:
        return self.__bid
    
    def getUid(self) -> int:
        return self.__uid
    
    def getRental(self) -> bool:
        return self.__rental
    
    def getDate(self) -> str:
        return self.__date
    
    def setRid(self, rid: int) -> None:
        self.__rid = rid
        
    def setBid(self, bid: int) -> None:
        self.__bid = bid
        
    def setUid(self, uid: int) -> None:
        self.__uid = uid
        
    def setRental(self, rental: bool) -> None:
        self.__rental = rental
