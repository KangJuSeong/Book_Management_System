from PyQt5.QtWidgets import *


def messageBox(window, text):
    QMessageBox.about(window, '알림', text)
