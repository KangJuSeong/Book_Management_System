from BookPkg.BookDBManager import BookDBManager
from BookPkg.BookController import BookController
import unittest


class TestBookManager(unittest.TestCase):

    def test_create(self):
        bm = BookDBManager()
        bid = bm.createBook('insert_test_book', 'insert_test_author', 12345, True, 'insert_TEST-123')
        test_case = {'bid':bid, 'name': 'insert_test_book', 'author': 'insert_test_author', 'isbn': 12345, 'rentaling':True, 'location': 'insert_TEST-123'}
        bc = BookController(bm.getBook(bid))
        self.assertEqual(test_case, bc.getBookAttr())
        bm.deleteBook(bid=bid)

    def test_rental(self):
        bdm = BookDBManager()
        bid = bdm.createBook('test_book', 'test_author', 12345, False, 'TEST-123')
        bc = BookController(bdm.getBook(bid))
        bc.rentalBook()
        flag = bdm.updateBook(bc.getBook(), bid)
        bc = BookController(bdm.getBook(bid))
        self.assertEqual([flag, bc.isRentaling()], [True, True])
        bdm.deleteBook(bid)

    def test_return(self):
        bdm = BookDBManager()
        bid = bdm.createBook('test_book', 'test_author', 12345, True, 'TEST-123')
        bc = BookController(bdm.getBook(bid))
        bc.returnBook()
        flag = bdm.updateBook(bc.getBook(), bid)
        bc = BookController(bdm.getBook(bid))
        self.assertEqual([flag, bc.isRentaling()], [True, False])
        bdm.deleteBook(bid)

    def test_delete(self):
        bm = BookDBManager()
        bid = bm.createBook('delete_test_book', 'delete_test_author', 12345, True, 'delete_TEST-123')
        flag = bm.deleteBook(bid=bid)
        self.assertEqual(flag, True)


if __name__ == '__main__':
    unittest.main()
