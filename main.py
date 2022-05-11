import sys 
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from UserPkg.UserDBManager import UserDBManager
from UserPkg.UserController import UserController

from BookPkg.BookDBManager import BookDBManager
from BookPkg.BookController import BookController

from RentalPkg.RentalDBManager import RentalDBManager
from RentalPkg.RentalController import RentalController


def messageBox(window, text):
    QMessageBox.about(window, '알림', text)


class LoginScreen(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("/Users/gangjuseong/Desktop/study/3-1/객분설/OOAD_Project/UI/LoginScreen.ui", self)
        self.udbm = UserDBManager()
        
        self.email = ""
        self.pw = ""
        self.uid = 0

        self.pw_edit.setEchoMode(QLineEdit.Password)

        self.email_edit.textChanged.connect(self.changeTextEmail)
        self.pw_edit.textChanged.connect(self.changeTextPw)
        self.login_btn.clicked.connect(self.clickLogin)
        
        self.signup_btn.clicked.connect(self.openSignUpWindow)
        
    def changeTextEmail(self):
        self.email = self.email_edit.text()
    
    def changeTextPw(self):
        self.pw = self.pw_edit.text()
        
    def clickLogin(self):
        self.uid = UserController.login(self.email, self.pw)
        if self.uid:
            self.openMainWindow()
        else:
            messageBox(self, '이메일 또는 비밀번호가 올바르지 않습니다.')
        self.email_edit.clear()
        self.pw_edit.clear()

    def openSignUpWindow(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def openMainWindow(self):
        widget.close()
        mw = MainScreen(self.uid)
        mw.exec_()


class SignUpScreen(QDialog):
    
    def __init__(self):
        super().__init__()
        loadUi("/Users/gangjuseong/Desktop/study/3-1/객분설/OOAD_Project/UI/SignUpScreen.ui", self)
        
        self.email = ''
        self.pw = ''
        self.name = ''
        self.phone = ''
        self.address = ''
        self.manager = ''
        self.manager_code = ''
        
        self.pw_edit.setEchoMode(QLineEdit.Password)
        
        self.email_edit.textChanged.connect(self.changeTextEmail)
        self.pw_edit.textChanged.connect(self.changeTextPw) 
        self.name_edit.textChanged.connect(self.changeTextName)
        self.phone_edit.textChanged.connect(self.changeTextPhone)
        self.address_edit.textChanged.connect(self.changeTextAddress)
        self.manager_code_edit.textChanged.connect(self.changeTextManagerCode)
        
        self.manager_radio_btn.clicked.connect(self.changeManagerOn)
        self.user_radio_btn.clicked.connect(self.changeManagerOff)
        self.signup_btn.clicked.connect(self.clickSignUp)
        self.back_btn.clicked.connect(self.openLoginWindow)
    
    def changeTextEmail(self):
        self.email = self.email_edit.text()
    
    def changeTextPw(self):
        self.pw = self.pw_edit.text()

    def changeTextName(self):
        self.name = self.name_edit.text()
        
    def changeTextPhone(self):
        self.phone = self.phone_edit.text()
        
    def changeTextAddress(self):
        self.address = self.address_edit.text()
        
    def changeTextManagerCode(self):
        self.manager_code = self.manager_code_edit.text()
    
    def changeManagerOn(self):
        self.manager = True
    
    def changeManagerOff(self):
        self.manager = False
    
    def clickSignUp(self):
        if self.email == '' or self.pw == '' or self.name == '' or self.phone == '' or self.address == '':
            messageBox(self, '정보를 모두 입력해주세요.')
            return
        uid = -1
        if self.manager == '':
            messageBox(self, "관리자 및 사용자를 선택해주세요.")
        else:
            if self.manager:
                if self.manager_code == UserController.getManagerCode():
                    uid = UserDBManager().createUser(self.name, self.address, self.phone, self.manager, self.email, self.pw)  # type: ignore
                else:
                    messageBox(self, "관리자 코드가 잘못되었습니다.")
            else:
                uid = UserDBManager().createUser(self.name, self.address, self.phone, self.manager, self.email, self.pw)  # type: ignore
        if uid == -1: return
        elif uid == 'Duplicate':
            messageBox(self, "중복된 이메일 입니다.")
        elif uid == 'NotEmailFormat':
            messageBox(self, "이메일 형식이 올바르지 않습니다.")
        else:
            messageBox(self, "회원가입 성공")
            self.openLoginWindow()
       
    def openLoginWindow(self):
        self.email_edit.clear()
        self.pw_edit.clear()
        self.name_edit.clear()
        self.phone_edit.clear()
        self.address_edit.clear()
        self.manager_code_edit.clear()
        widget.setCurrentIndex(widget.currentIndex()-1)
    

class MainScreen(QDialog):
    def __init__(self, uid):
        super().__init__()
        loadUi("/Users/gangjuseong/Desktop/study/3-1/객분설/OOAD_Project/UI/MainScreen.ui", self)
        self.uid = uid
        messageBox(self, '로그인 성공')
        self.bm = BookDBManager()
        self.rm = RentalDBManager()
        self.um = UserDBManager()
        self.user = UserController(UserDBManager().getUser(uid))

        self.current_user_name_label.setText(f"{self.user.getUserAttr()['name']} 님, 안녕하세요!")
        self.renderBookList()
        self.renderRentalList()
    
        self.book_list.itemClicked.connect(self.clickedBookItem)
        self.rental_list.itemClicked.connect(self.clickedRentalItem)
        self.user_list.itemClicked.connect(self.clickedUserItem)
        self.no_return_list.itemClicked.connect(self.clikcedNoReturnItem)
    
        self.search_btn.clicked.connect(self.clickedSearchBtn)
        self.rental_btn.clicked.connect(self.clickedRentalBtn)
        self.return_btn.clicked.connect(self.clickedReturnBtn)
        self.delete_btn.clicked.connect(self.clickedDeleteBtn)
        self.insert_btn.clicked.connect(self.clickedInsertBtn)
        self.user_search_btn.clicked.connect(self.clickedSearchUserBtn)
        self.no_return_search_btn.clicked.connect(self.clickedSearchRentalBtn)
    
    def renderBookList(self, keyword=None):
        self.book_list.clear()
        if keyword: data = self.bm.listBook(keyword=keyword)
        else: data = self.bm.listBook()
        for i, v in enumerate(data):
            self.book_list.addItem(f"{v[0]} {v[1]} - {v[2]} - {v[3]}")

    def renderRentalList(self):
        self.rental_list.clear()
        for i, v in enumerate(RentalController.getUserRentalList(self.user.getUserAttr()['uid'])):
            bc = BookController(BookDBManager().getBook(v['bid']))
            self.rental_list.addItem(f"{v['rid']} {bc.getBookAttr()['name']} - {bc.getBookAttr()['author']} - {bc.getBookAttr()['isbn']} / {v['date']}")

    def clickedBookItem(self):
        bid = int(self.book_list.currentItem().text().split(' ')[0])
        self.detailBookInfo(bid)

    def clickedRentalItem(self):
        rid = int(self.rental_list.currentItem().text().split(' ')[0])
        rc = RentalController(RentalDBManager().getRental(rid))
        bid = rc.getRentalAttr()['bid']
        self.detailBookInfo(bid)
    
    def clickedUserItem(self):
        uid = int(self.user_list.currentItem().text().split(' ')[0])
        self.detailUserInfo(uid)
        
    def clikcedNoReturnItem(self):
        rid = int(self.no_return_list.currentItem().text().split(' ')[0])
        self.detailRentalInfo(rid)
    
    def clickedRentalBtn(self):
        bid = int(self.book_list.currentItem().text().split(' ')[0])
        rid = self.rm.createRental(bid, self.user.getUserAttr()['uid'])
        if rid == -1:
            messageBox(self, '이미 대여중인 도서입니다.')
            return
        self.renderRentalList()
        messageBox(self, '도서 대여 처리 되었습니다.')
        
    def clickedReturnBtn(self):
        rid = int(self.rental_list.currentItem().text().split(' ')[0])
        flag = self.rm.deleteRental(rid)
        if flag:
            self.renderRentalList()
            messageBox(self, '도서 반납 처리 되었습니다.')
        else:
            messageBox(self, '도서 반납에 실패했습니다.')
    
    def clickedSearchBtn(self):
        keyword = self.search_edit.text()
        self.renderBookList(keyword=keyword)
        self.search_edit.setText('')
        
    def clickedDeleteBtn(self):
        if self.user.isManager():
            bid = int(self.book_list.currentItem().text().split(' ')[0])
            self.bm.deleteBook(bid)
            self.renderBookList()
            self.renderRentalList()
        else:
            messageBox(self, "관리자만 이용 가능합니다.")

    def clickedInsertBtn(self):
        if self.user.isManager():
            name = self.book_name_edit.text()
            author = self.book_author_edit.text()
            isbn = self.book_isbn_edit.text()
            location = self.book_location_edit.text()
            if name == '' or author == '' or isbn == '' or location == '':
                messageBox(self, "빈칸을 모두 채워주세요")
                return
            self.bm.createBook(name, author, isbn, False, location)
            self.renderBookList()
        else:
            messageBox(self, "관리자만 이용 가능합니다.")
            self.book_name_edit.clear()
            self.book_author_edit.clear() 
            self.book_isbn_edit.clear()
            self.book_location_edit.clear()
    
    def clickedSearchUserBtn(self):
        self.user_list.clear()
        if self.user.isManager():
            keyword = self.user_edit.text()
            user_list = UserDBManager().listUser(keyword=keyword)
            for i, v in enumerate(user_list):
                self.user_list.addItem(f"{v[0]} {v[1]} - {v[5]} - {v[3]}")
        else:
            messageBox(self, "관리자만 이용 가능합니다.")
        self.user_edit.setText('')
        
    def clickedSearchRentalBtn(self):
        self.no_return_list.clear()
        if self.user.isManager():
            keyword = self.no_return_edit.text()
            bid_list = [i[0] for i in self.bm.listBook(keyword=keyword)]
            uid_list = [i[0] for i in self.um.listUser(keyword=keyword)]
            rid_list = [i[0] for i in self.rm.listRental()]
            for i, rid in enumerate(rid_list):
                rental = RentalController(self.rm.getRental(rid)).getRentalAttr()
                for i, bid in enumerate(bid_list):
                    if rental['bid'] == bid:
                        book_name = BookController(self.bm.getBook(bid)).getBookAttr()['name']
                        user_name = UserController(self.um.getUser(rental['uid'])).getUserAttr()['name']
                        self.no_return_list.addItem(f"{rental['rid']} {book_name} - {user_name} {rental['date']}")
                for i, uid in enumerate(uid_list):
                    if rental['uid'] == uid:
                        book_name = BookController(self.bm.getBook(rental['bid'])).getBookAttr()['name']
                        user_name = UserController(self.um.getUser(uid)).getUserAttr()['name']
                        self.no_return_list.addItem(f"{rental['rid']} {book_name} - {user_name} {rental['date']}")
        else:
            messageBox(self, "관리자만 이용 가능합니다.")
        self.no_return_edit.setText('')

    def detailBookInfo(self, bid):
        book_attr = BookController(self.bm.getBook(bid)).getBookAttr()
        self.book_name_label.setText(f"책 이름 : {book_attr['name']}")
        self.book_author_label.setText(f"저자 : {book_attr['author']}")
        self.book_isbn_label.setText(f"ISBN : {book_attr['isbn']}")
        if book_attr['rentaling']:
            self.book_rental_label.setText(f"대여 상태 : 대여 중")
        else:
            self.book_rental_label.setText(f"대여 상태 : 대여 가능")
        self.book_location_label.setText(f"위치 : {book_attr['location']}")
        
    def detailUserInfo(self, uid):
        user_attr = UserController(self.um.getUser(uid)).getUserAttr()
        self.user_name_label.setText(f"이름 : {user_attr['name']}")
        self.user_email_label.setText(f"이메일 : {user_attr['email']}")
        self.user_phone_label.setText(f"번호 : {user_attr['phone']}")
        self.user_address_label.setText(f"주소 : {user_attr['address']}")
        
    def detailRentalInfo(self, rid):
        rental = RentalController(self.rm.getRental(rid)).getRentalAttr()
        book = BookController(self.bm.getBook(rental['bid'])).getBookAttr()
        user = UserController(self.um.getUser(rental['uid'])).getUserAttr()
        self.no_return_book_name_label.setText(f"책 이름 : {book['name']}")
        self.no_return_date_label.setText(f"대여 날짜 : {rental['date']}")
        self.no_return_user_label.setText(f"대여자 : {user['name']}")
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    LoginWindow = LoginScreen()
    SignUpWindow = SignUpScreen()
    widget.addWidget(LoginWindow)
    widget.addWidget(SignUpWindow)
    widget.setFixedHeight(500)
    widget.setFixedWidth(850)
    widget.show()
    app.exec_()