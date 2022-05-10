from RentalPkg.RentalController import RenatlController
from UserPkg.UserDBManager import UserDBManager
from BookPkg.BookDBManager import BookDBManager
from BookPkg.BookController import BookController
from RentalPkg.RentalDBlManager import RentalDBManager
import unittest
import time


class TestRentalManager(unittest.TestCase):
        
    def test_create(self):
        um = UserDBManager()
        bm = BookDBManager()
        rm = RentalDBManager()
        uid = um.createUser('TEST', 'TEST', 'TEST', True, 'TEST', 'TEST')
        bid = bm.createBook('TEST', 'TEST', 1234, False, 'TEST')
        rid = rm.createRental(bid, uid)
        result = [True, {'rid': rid, 'bid': bid, 'uid': uid, 'rental': True, 'date': time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))}]
        test_result = [BookController(BookDBManager().getBook(bid)).isRentaling(), RenatlController(RentalDBManager().getRental(rid)).getRentalAttr()]
        self.assertEqual(result, test_result)
        rm.deleteRental(rid)
        bm.deleteBook(bid)
        um.deleteUser(uid)
        
    def test_delete(self):
        um = UserDBManager()
        bm = BookDBManager()
        rm = RentalDBManager()
        uid = um.createUser('TEST', 'TEST', 'TEST', True, 'TEST', 'TEST')
        bid = bm.createBook('TEST', 'TEST', 1234, False, 'TEST')
        rid = rm.createRental(bid, uid)
        test_result = [rm.deleteRental(rid), BookController(bm.getBook(bid)).isRentaling()]
        result = [True, False]
        self.assertEqual(result, test_result)
        bm.deleteBook(bid)
        um.deleteUser(uid)
        
        

if __name__ == '__main__':
    unittest.main()
