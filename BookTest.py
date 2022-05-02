from BookPkg.BookManager import BookManager


if __name__ == '__main__':
    bm = BookManager()
    bm.createBook('새로운도서123', 'hello', 32423, False, 'B-123')
    # print(bm.listBook(keyword='피카소'))
    # print(bm.deleteBook(0))
    # print(bm.updateBook('기존 도서', '강주성', 232323, False, 'C-19', bid=10))
