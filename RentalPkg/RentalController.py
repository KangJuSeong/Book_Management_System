from .RentalDBManager import RentalDBManager
from .Rental import _Rental


class RentalController(_Rental):
    
    def __init__(self, rental: _Rental):
        self.rental: _Rental = rental
        self.dbm: RentalDBManager = RentalDBManager()
        
    def getRental(self) -> _Rental:
        return self.rental
    
    def getRentalAttr(self) -> dict:
        data = {}
        for k, v in self.rental.__dict__.items():
            data[k[9:]] = v
        return data
    
    @staticmethod
    def getUserRentalList(uid) -> list:
        data = []
        for i, v in enumerate(RentalDBManager().listRental()):
            rental = RentalController(_Rental(v[0], v[1], v[2], v[3], v[4]))
            rental_attr = rental.getRentalAttr()
            if rental_attr['uid'] == uid:
                data.append(rental_attr)
        return data
    
    @staticmethod
    def getBookRentalList(bid) -> list:
        data = []
        for i, v in enumerate(RentalDBManager().listRental()):
            rental = RentalController(_Rental(v[0], v[1], v[2], v[3], v[4]))
            rental_attr = rental.getRentalAttr()
            if rental_attr['bid'] == bid:
                data.append(rental_attr)
        return data 
    
        
