from .RetnaDBlManager import RentalDBManager
from .Rental import _Rental


class RenatlController(_Rental):
    
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
