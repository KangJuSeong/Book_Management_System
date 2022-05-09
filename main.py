import sys 
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from UserPkg.UserDBManager import UserDBManager
from UserPkg.UserController import UserController


class LoginScreen(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("/Users/gangjuseong/Desktop/study/3-1/객분설/OOAD_Project/UI/LoginScreen.ui", self)
        self.udbm = UserDBManager()
        
        self._id = ""
        self._pw = ""
        
        self.id_edit.textChanged.connect(self.changeTextId)
        self.pw_edit.textChanged.connect(self.changeTextPw)
        self.login_btn.clicked.connect(self.clickLogin)
        
        self.signup_btn.clicked.connect(self.openSignUpWindow)
        
    def changeTextId(self):
        self._id = self.id_edit.text()
    
    def changeTextPw(self):
        self._pw = self.pw_edit.text()
        
    def clickLogin(self):
        if UserController.login(self._id, self._pw):
            print('success')
        else:
            print('fail')

    def openSignUpWindow(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        

class SignUpScreen(QMainWindow):
    
    def __init__(self):
        super().__init__()
        loadUi("/Users/gangjuseong/Desktop/study/3-1/객분설/OOAD_Project/UI/SignUpScreen.ui", self)
        
        self.back_btn.clicked.connect(self.openLoginWindow)
    
    def openLoginWindow(self):
        widget.setCurrentIndex(widget.currentIndex()-1)


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