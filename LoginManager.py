# -*- coding: utf-8 -*-
"""
Created on Tue May 31 02:46:21 2022

@author: piton
"""

from LoginWindow import Ui_LoginWindow
from WaitingLabel import WaitingLabel
import MainManager
from GraphManager import GraphManager
from httpRequests import HttpRequest
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt,QTimer,QPoint
import time

class LoginManager(QtWidgets.QMainWindow,Ui_LoginWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__rq = HttpRequest()
        self.timer = QTimer()
        self.timer.start(13)
        self.colorFlag = True
        self.timer.timeout.connect(self.logoColorChange)
        self.R = 120
        self.B = 255
        self.alpha = 40
        self.clickFlag = True

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signUp_password1.setEchoMode((QtWidgets.QLineEdit.Password))
        self.signUp_password2.setEchoMode((QtWidgets.QLineEdit.Password))
        self.connectSignalSlots()
        
    def connectSignalSlots(self):
        self.exitButton.clicked.connect(lambda: self.close())
        self.pushButton.clicked.connect(self.requestLogin)
        self.signUp_Button.clicked.connect(lambda: {self.stackedWidget.setCurrentIndex(1)})
        self.exitButton_newUser.clicked.connect(lambda: {self.stackedWidget.setCurrentIndex(0)})
        self.signUp_signupButton.clicked.connect(lambda: {self.createNewUser(role="ROLE_PATIENT")})
        
    def createNewUser(self,role="ROLE_PATIENT"):
        pass1 = str(self.signUp_password1.text())
        pass2 = str(self.signUp_password2.text())
        print(pass1 , "  " ,pass2)
        if not (pass1 == pass2):
            self.status_label.setText("Passwords does not match!")
            self.status_label.setStyleSheet("#status_label{\n"
    "color: \"red\";\n"
    "    font: 8pt \"8514oem\";\n"
    "}")
            return
        tc = int(self.signUp_TC.text())
        name = str(self.signUp_Name.text())
        surname = str(self.signUp_Surname.text())
        password = pass1
        hr = HttpRequest()
        print(tc," ",name," ",surname," ",password," ",role)
        status = hr.postNewUser(tc,name,surname,password,role)
        if status == 200:
            self.status_label.setText("User created successfully.")
            self.status_label.setStyleSheet("#status_label{\n"
    "color: \"green\";\n"
    "    font: 8pt \"8514oem\";\n"
    "}")
        elif status == -1:
            self.status_label.setText("Failed to connect to the server!")
            self.status_label.setStyleSheet("#status_label{\n"
    "color: \"red\";\n"
    "    font: 8pt \"8514oem\";\n"
    "}")
        else:
            self.status_label.setText("Something gone wrong!")
            self.status_label.setStyleSheet("#status_label{\n"
    "color: \"red\";\n"
    "    font: 8pt \"8514oem\";\n"
    "}")        
        

    
   
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.requestLogin()
    def logoColorChange(self):
        self.label_2.setStyleSheet("QLabel { color : rgb(%s,120,%s,%s); }" % (str(self.R),str(self.B),str(self.alpha)));

        if self.colorFlag:
            self.R+=1
            self.alpha +=1
            self.B-=1
        else: 
            self.R-=1
            self.B+=1
            self.alpha -=1
            
        if self.R == 255:
            self.colorFlag = False
        if self.R == 120:
            self.colorFlag = True
        
    def requestLogin(self):
        self.clickFlag = False
        self.blockSignals(True)
        
        self.__waitingLabel = WaitingLabel()
        self.__name = self.id_lineEdit.text()
        self.__password = self.password_lineEdit.text()
        
        status,response = self.__rq.requestLogin(self.__name,self.__password)
        if response == -1:    
            self.label.setText("Failed to connect server.")
            self.label.setStyleSheet("#label{\n"
    "color: \"red\";\n"
    "    font: 8pt \"8514oem\";\n"
    "}")            
            return        

        if status == 200:
            data = response.json()
            self.__waitingLabel.show()
            time.sleep(2)
            self.close()
            
            self.label.setText("Welcome")
            name = data["name"]
            surname = data["surname"]
            tc = data["tc"]
            role = data["role"]
            
            if role == "ROLE_ADMIN":
                self.newWindow = MainManager.MainManager(role,name,surname,tc,showOnlyMyPatientsButton=False)
                self.newWindow.show()
                
            if role == "ROLE_DOCTOR":
                print(role," ",name," ",surname," ",tc)
                self.newWindow = MainManager.MainManager(role,name,surname,tc)
                self.newWindow.show()
                
            if role == "ROLE_PATIENT":
                self.newWindow = GraphManager(tc,tc,thread="True")
                self.newWindow.show()
                
        elif status == 404:
            self.label.setText("Wrong user name or password.")
            self.label.setStyleSheet("#label{\n"
    "color: \"red\";\n"
    "    font: 8pt \"8514oem\";\n"
    "}")
        else:
            self.label.setText("Something gone wrong!")
            self.label.setStyleSheet("#label{\n"
    "color: \"red\";\n"
    "    font: 8pt \"8514oem\";\n"
    "}")
        print(status)
        self.pushButton.blockSignals(False)
        self.pushButton.setEnabled(True)
        self.__waitingLabel.close()            
