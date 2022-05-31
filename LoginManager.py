# -*- coding: utf-8 -*-
"""
Created on Tue May 31 02:46:21 2022

@author: piton
"""

from LoginWindow import Ui_LoginWindow
from MainManager import MainManager
from httpRequests import HttpRequest
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
class LoginManager(QtWidgets.QMainWindow,Ui_LoginWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__rq = HttpRequest()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        
        self.exitButton.clicked.connect(lambda: self.close())
        self.pushButton.clicked.connect(self.requestLogin)
        self.signUp_Button.clicked.connect(lambda: {self.stackedWidget.setCurrentIndex(1)})
        self.exitButton_newUser.clicked.connect(lambda: {self.stackedWidget.setCurrentIndex(0)})
    
    def requestLogin(self):
        self.__name = self.id_lineEdit.text()
        self.__password = self.password_lineEdit.text()
        self.__response = self.__rq.requestLogin(self.__name,self.__password)
        # self.__response.status_code
        if self.__response.status_code == 200:
            self.close()
            
            self.newWindow = MainManager()
            self.newWindow.show()
        elif self.__response.status_code == 404:
            self.label.setText("Wrong user name or password.")
            self.label.setStyleSheet("#label{\n"
    "color: \"red\";\n"
    "    font: 8pt \"8514oem\";\n"
    "}")
        else:
            self.label.setText("Wrong user name or password.")
        self.label.setStyleSheet("#label{\n"
"color: \"red\";\n"
"    font: 8pt \"8514oem\";\n"
"}")
            
            
        print(self.__response.status_code)
        print("id: ",self.__name,"  password: ",self.__password)