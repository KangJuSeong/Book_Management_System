from RentalPkg.RentalDBManager import RentalDBManager
from BookPkg.BookDBManager import BookDBManager
from RentalPkg.Rental import _Rental


class RentalServie(_Rental):
    
    def __init__(self):
        self.rm = RentalDBManager()
        self.bm = BookDBManager()
        
    def getUserRentalList(self, uid: int) -> list:
        data = []
        for i, v in enumerate(self.rm.listRental()):
            rental_attr = {'rid': v[0],
                           'bid': v[1],
                           'uid': v[2],
                           'rental': v[3],
                           'date': v[4]}
            if rental_attr['uid'] == uid:
                data.append(rental_attr)
        return data
   
    def getBookRentalList(self, bid):
        data = []
        for i, v in enumerate(self.rm.listRental()):
            if v[1] == bid:
                data.append(v[0])
        return data
    
    def getRentalList(self):
        return self.rm.listRental()
    
    def getRentalAttr(self, rid):
        rental = self.rm.getRental(rid)
        return {'rid': rental.getRid(),
                'bid': rental.getBid(),
                'uid': rental.getUid(),
                'rental': rental.getRental(),
                'date': rental.getDate()}
        
    def rentalBook(self, uid, bid):
        book = self.bm.getBook(bid)
        if book.getRentaling():
            return -1
        else:
            book.onRentaling()
            self.bm.updateBook(book, bid)
            return self.rm.createRental(bid, uid)
        
    def returnBook(self, rid):
        book = self.bm.getBook(self.rm.getRental(rid).getBid())
        book.offRentaling()
        self.bm.updateBook(book, book.getBid())
        return self.rm.deleteRental(rid)