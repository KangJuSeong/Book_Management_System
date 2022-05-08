from BookPkg.BookManager import BookManager
import unittest


class TestBookManager(unittest.TestCase):

    def test_create(self):
        bm = BookManager()
        bid = bm.createBook('insert_test_book', 'insert_test_author', 12345, True, 'insert_TEST-123')
        test_case = [bid, 'insert_test_book', 'insert_test_author', 12345, True, 'insert_TEST-123']
        self.assertEqual(bm.getBook(bid=bid), test_case)
        bm.deleteBook(bid=bid)

    def test_update(self):
        bm = BookManager()
        bid = bm.createBook('update_test_book', 'update_test_author', 12345, True, 'update_TEST-123')
        flag = bm.updateBook('test_book_update', 'test_author_update', 44444, False, 'TEST-123_update', bid=bid)
        result = bm.getBook(bid=bid)
        result.append(flag)
        test_case = [bid, 'test_book_update', 'test_author_update', 44444, False, 'TEST-123_update', True] 
        self.assertEqual(result, test_case)
        bm.deleteBook(bid=bid)

    def test_delete(self):
        bm = BookManager()
        bid = bm.createBook('delete_test_book', 'delete_test_author', 12345, True, 'delete_TEST-123')
        flag = bm.deleteBook(bid=bid)
        self.assertEqual(flag, True)


if __name__ == '__main__':
    unittest.main()
