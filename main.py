from signal import signal
import sys 
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from UserPkg.UserDBManager import UserDBManager
from UserPkg.UserController import UserController

from BookPkg.BookDBManager import BookDBManager
from BookPkg.BookController import BookController


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
        self.user = UserController(UserDBManager().getUser(uid))

        self.user_name_label.setText(f"{self.user.getUserAttr()['name']} 님, 안녕하세요!")
        self.renderBookList()
        self.book_list.itemClicked.connect(self.clickedItem)
        self.search_btn.clicked.connect(self.searchBookList)
    
    def renderBookList(self, keyword=None):
        self.book_list.clear()
        if keyword: data = self.bm.listBook(keyword=keyword)
        else: data = self.bm.listBook()
        for i, v in enumerate(data):
            self.book_list.addItem(f"{v[0]} {v[1]} - {v[2]}")
     
    def clickedItem(self):
        bid = int(self.book_list.currentItem().text().split(' ')[0])
        self.detailBookInfo(BookController(self.bm.getBook(bid)).getBookAttr())       
    
    def detailBookInfo(self, book_attr):
        self.book_name_label.setText(f"책 이름 : {book_attr['name']}")
        self.book_author_label.setText(f"저자 : {book_attr['author']}")
        self.book_isbn_label.setText(f"ISBN : {book_attr['isbn']}")
        if book_attr['rentaling']:
            self.book_rental_label.setText(f"대여 상태 : 대여 중")
        else:
            self.book_rental_label.setText(f"대여 상태 : 대여 가능")
        self.book_location_label.setText(f"위치 : {book_attr['location']}")
        
    def searchBookList(self):
        keyword = self.search_edit.text()
        self.renderBookList(keyword=keyword)
            

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