from UserPkg.UserDBManager import UserManager
from BookPkg.BookDBManager import BookManager
from RentalPkg.RetnaDBlManager import RentalManager
import unittest
import time


class TestRentalManager(unittest.TestCase):
        
    def test_create(self):
        um = UserManager()
        bm = BookManager()
        rm = RentalManager()
        uid = um.createUser('TEST', 'TEST', 'TEST', True, 'TEST', 'TEST')
        bid = bm.createBook('TEST', 'TEST', 1234, False, 'TEST')
        rid = rm.createRental(bid, uid)
        result = [True, [rid, bid, uid, True, time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))]]
        test_result = [bm.getBook(bid)[4], rm.getRental(rid)]
        self.assertEqual(result, test_result)
        rm.deleteRental(rid)
        bm.deleteBook(bid)
        um.deleteUser(uid)
        

if __name__ == '__main__':
    unittest.main()
