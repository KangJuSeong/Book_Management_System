class Rental:
    
    def __init__(self, rid: int, bid: int, uid: int, rental: bool, date: str):
        self.rid: int = rid
        self.bid: int = bid
        self.uid: int = uid
        self.rental: bool = rental
        self.date: str = date
        