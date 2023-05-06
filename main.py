import sys
import os
from util.messageBox import messageBox
from util.my_requests import MyRequests
from util.IDManager import getManagerCode

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from domain.User import User
from domain.Book import Book
from domain.Rental import Rental




class LoginScreen(QDialog):

    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/UI/LoginScreen.ui", self)
        self.req = MyRequests()
        self.email = ""
        self.pw = ""

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
        body = {
            "email": self.email,
            "password": self.pw
        }
        status, res, data = self.req.reqPost("user/login", body)
        if status == 200 and res.get('status') == "OK":
            self.uid = data.get('id')
            self.openMainWindow()
        else:
            messageBox(self, res.get('msg'))
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
        loadUi(os.getcwd() + "/UI/SignUpScreen.ui", self)
        
        self.email = ''
        self.pw = ''
        self.name = ''
        self.phone = ''
        self.address = ''
        self.manager = ''
        self.manager_code = ''
        self.req = MyRequests()
        
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
        body = dict()
        status = 0
        res = dict()
        if self.email == '' or self.pw == '' or self.name == '' or self.phone == '' or self.address == '':
            messageBox(self, '정보를 모두 입력해주세요.')
            return
        if self.manager == '':
            messageBox(self, "관리자 및 사용자를 선택해주세요.")
        else:
            if self.manager:
                if self.manager_code == getManagerCode():
                    body = {
                        "name": self.name, 
                        "address": self.address, 
                        "phone": self.phone, 
                        "role": "MANAGER",
                        "email": self.email,
                        "password": self.pw
                    }
                    status, res, data = self.req.reqPost("user/signup", body)
                else:
                    messageBox(self, "관리자 코드가 잘못되었습니다.")
            else:
                body = {
                        "name": self.name, 
                        "address": self.address, 
                        "phone": self.phone, 
                        "role": "USER",
                        "email": self.email,
                        "password": self.pw
                    }
                status, res, data = self.req.reqPost("user/signup", body)
        if res.get('status') == 'OK':
            messageBox(self, "회원가입 성공")
            self.openLoginWindow()
        else:
            messageBox(self, "회원가입 실패")
            self.email_edit.clear()
            self.pw_edit.clear()
            self.name_edit.clear()
            self.phone_edit.clear()
            self.address_edit.clear()
            self.manager_code_edit.clear()
       
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
        loadUi(os.getcwd() + "/UI/MainScreen.ui", self)
        self.req = MyRequests()
        status, res, data = self.req.reqGet(f"user/{uid}")
        self.user = User(
            data.get('id'),
            data.get('name'),
            data.get('address'),
            data.get('phone'),
            data.get('role'),
            data.get('email'))
        
        self.current_user_name_label.setText(f"Welcome {self.user.name}!")
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
        if keyword != None:
            status, res, data = self.req.reqGet(f"book/search?keyword={keyword}")
        else:
            status, res, data = self.req.reqGet("book/list")
        for book in data:
            self.book_list.addItem(f"{book['id']} - {book['name']} - {book['author']} - {book['isbn']}")

    def renderRentalList(self):
        self.rental_list.clear()
        status, res, data = self.req.reqGet(f"rental/list/{self.user.uid}")
        for i, v in enumerate(data):
            book = v.get('book')
            self.rental_list.addItem(f"{v['id']} {book['name']} - {book['author']} - {book['isbn']} / {v['createdAt']}")

    def clickedBookItem(self):
        bid = int(self.book_list.currentItem().text().split(' ')[0])
        status, res, data = self.req.reqGet(f"book/{bid}")
        self.book_name_label.setText(f"책 이름 : {data['name']}")
        self.book_author_label.setText(f"저자 : {data['author']}")
        self.book_isbn_label.setText(f"ISBN : {data['isbn']}")
        if data['isRental']:
            self.book_rental_label.setText(f"대여 상태 : 대여 중")
        else:
            self.book_rental_label.setText(f"대여 상태 : 대여 가능")
        self.book_location_label.setText(f"위치 : {data['location']}")
        
    def clickedSearchBtn(self):
        keyword = self.search_edit.text()
        self.renderBookList(keyword=keyword)
        self.search_edit.setText('')

    def clickedRentalItem(self):
        rid = int(self.rental_list.currentItem().text().split(' ')[0])
        status, res, data = self.req.reqGet(f"rental/{rid}")
        data = data['book']
        self.book_name_label.setText(f"책 이름 : {data['name']}")
        self.book_author_label.setText(f"저자 : {data['author']}")
        self.book_isbn_label.setText(f"ISBN : {data['isbn']}")
        if data['isRental']:
            self.book_rental_label.setText(f"대여 상태 : 대여 중")
        else:
            self.book_rental_label.setText(f"대여 상태 : 대여 가능")
        self.book_location_label.setText(f"위치 : {data['location']}")
        
    def clickedRentalBtn(self):
        bid = int(self.book_list.currentItem().text().split(' ')[0])
        body = {
            "bookId": bid,
            "userId": self.user.uid
        }
        status, res, data = self.req.reqPost("rental", body)
        if res.get('status') == 'BAD_REQUEST':
            messageBox(self, '이미 대여중인 도서입니다.')
            return
        self.renderRentalList()
        messageBox(self, '도서 대여 처리 되었습니다.')
        
    def clickedReturnBtn(self):
        rid = int(self.rental_list.currentItem().text().split(' ')[0])
        status, res, data = self.req.reqPut(f"rental/{rid}")
        if res.get('status') == 'OK':
            self.renderRentalList()
            messageBox(self, '도서 반납이 완료되었습니다.')
            self.renderRentalList()
        else:
            messageBox(self, '이미 반납된 도서입니다.')

    # Magaer 기능 #
    def clickedInsertBtn(self):
        if self.user.role == 'MANAGER':
            name = self.book_name_edit.text()
            author = self.book_author_edit.text()
            isbn = self.book_isbn_edit.text()
            location = self.book_location_edit.text()
            if name == '' or author == '' or isbn == '' or location == '':
                messageBox(self, "빈칸을 모두 채워주세요")
                return
            body = {
                "name": name,
                "author": author,
                "isbn": isbn,
                "isRental": False,
                "location": location
            }
            status, res, data = self.req.reqPost("book", body)
            if res.get('status') == 'OK':
                self.renderBookList()
        else:
            messageBox(self, "관리자만 이용 가능합니다.")
        self.book_name_edit.clear()
        self.book_author_edit.clear() 
        self.book_isbn_edit.clear()
        self.book_location_edit.clear()

    def clickedDeleteBtn(self):
        if self.user.role == 'MANAGER':
            bid = int(self.book_list.currentItem().text().split(' ')[0])
            status, res, data = self.req.reqDel(f"book/{bid}")
            self.renderBookList()
            self.renderRentalList()
        else:
            messageBox(self, "관리자만 이용 가능합니다.")
    
    def clickedSearchUserBtn(self):
        self.user_list.clear()
        if self.user.role == 'MANAGER':
            keyword = self.user_edit.text()
            status, res, data = self.req.reqGet(f"user/search?keyword={keyword}")
            print(data)
            for i, v in enumerate(data):
                self.user_list.addItem(f"{v['id']} {v['name']} - {v['email']} - {v['phone']}")
        else:
            messageBox(self, "관리자만 이용 가능합니다.")
        self.user_edit.setText('')
        
    def clickedUserItem(self):
        uid = int(self.user_list.currentItem().text().split(' ')[0])
        status, res, data = self.req.reqGet(f"user/{uid}")
        self.user_name_label.setText(f"이름 : {data['name']}")
        self.user_email_label.setText(f"이메일 : {data['email']}")
        self.user_phone_label.setText(f"번호 : {data['phone']}")
        self.user_address_label.setText(f"주소 : {data['address']}")
        
    def clikcedNoReturnItem(self):
        rid = int(self.no_return_list.currentItem().text().split(' ')[0])
        # rental = RentalController(rid).getRentalAttr()
        # book = BookController(rental['bid']).getBookAttr()
        # user = UserController(rental['uid']).getUserAttr()
        # self.no_return_book_name_label.setText(f"책 이름 : {book['name']}")
        # self.no_return_date_label.setText(f"대여 날짜 : {rental['date']}")
        # self.no_return_user_label.setText(f"대여자 : {user['name']}")
        
    def clickedSearchRentalBtn(self):
        # self.no_return_list.clear()
        # if self.user.role == 'MANAGER':
        #     keyword = self.no_return_edit.text()
        #     rid_list = [i for i in RentalController().getRentalList()]
        #     if keyword == '':
        #         for i, v in enumerate(rid_list):
        #             book_name = BookController(v[1]).getBookAttr()['name']
        #             user_name = UserController(v[2]).getUserAttr()['name']
        #             self.no_return_list.addItem(f"{v[0]} {book_name} - {user_name} / {v[3]}")
        #     else:
        #         bid_list = [i[0] for i in BookController().getBookList(keyword=keyword)]
        #         uid_list = [i[0] for i in UserController().getUserList(keyword=keyword)]
        #         for i, v in enumerate(rid_list):
        #             rental = RentalController(v[0]).getRentalAttr()
        #             for i, bid in enumerate(bid_list):
        #                 if rental['bid'] == bid:
        #                     book_name = BookController(bid).getBookAttr()['name']
        #                     user_name = UserController(rental['uid']).getUserAttr()['name']
        #                     self.no_return_list.addItem(f"{rental['rid']} {book_name} - {user_name} / {rental['date']}")
        #             for i, uid in enumerate(uid_list):
        #                 if rental['uid'] == uid:
        #                     book_name = BookController(rental['bid']).getBookAttr()['name']
        #                     user_name = UserController(uid).getUserAttr()['name']
        #                     self.no_return_list.addItem(f"{rental['rid']} {book_name} - {user_name} / {rental['date']}")
        # else:
        #     messageBox(self, "관리자만 이용 가능합니다.")
        self.no_return_edit.setText('')
 

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