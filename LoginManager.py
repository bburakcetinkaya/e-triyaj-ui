# -*- coding: utf-8 -*-
"""
Created on Tue May 31 02:46:21 2022

@author: piton
"""

from LoginWindow import Ui_LoginWindow
from WaitingLabel import WaitingLabel
from MainManager import MainManager
from GraphManager import GraphManager
from httpRequests import HttpRequest
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import Qt,QTimer,QPoint,QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from Resize import SideGrip
import time
import json
import pandas as pd

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
        # self.enterClicked = QtGui.QKeyEvent().key(0x01000004)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordNewUser_lineEdit.setEchoMode((QtWidgets.QLineEdit.Password))
        self.passwordNewUser_lineEdit2.setEchoMode((QtWidgets.QLineEdit.Password))
        self.connectSignalSlots()
        
    def connectSignalSlots(self):
        self.exitButton.clicked.connect(lambda: self.close())
        self.pushButton.clicked.connect(self.requestLogin)
        self.signUp_Button.clicked.connect(lambda: {self.stackedWidget.setCurrentIndex(1)})
        self.exitButton_newUser.clicked.connect(lambda: {self.stackedWidget.setCurrentIndex(0)})
#         self.sizegrip = QtWidgets.QSizeGrip(Ui_LoginWindow)
# 		self.gridLayout.addWidget(self.sizegrip,1,0,QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight)
# 		flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
# 		Ui_LoginWindow.setWindowFlags(flags)

    
   
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
        
        if self.colorFlag:
            self.R+=1
            self.alpha +=1
            self.B-=1
        else: 
            self.R-=1
            self.B+=1
            self.alpha -=1
        
        self.label_2.setStyleSheet("QLabel { color : rgb(%s,120,%s,%s); }" % (str(self.R),str(self.B),str(self.alpha)));
        # self.heartLogo.fill(QtCore.Qt.black)
        # print(self.G," ",self.B)
        if self.R == 255:
            self.colorFlag = False
        if self.R == 120:
            self.colorFlag = True
            
        # if self.B == 0:
        #     self.colorFlag = False
        # if self.B == 255:
        #     self.colorFlag = True
        
        
    def requestLogin(self):
       
        self.clickFlag = False
        self.pushButton.setEnabled(False)
        # self.pushButton.setC
        self.blockSignals(True)

        
        self.__waitingLabel = WaitingLabel()
        self.__name = self.id_lineEdit.text()
        self.__password = self.password_lineEdit.text()
        try:
            response = self.__rq.requestLogin(self.__name,self.__password)
        except:
            self.label.setText("Failed to connect server.")
            self.label.setStyleSheet("#label{\n"
    "color: \"red\";\n"
    "    font: 8pt \"8514oem\";\n"
    "}")
            return
        else:
            data = response.json()
        
        # data = pd.DataFrame(self.__response)
        print(data)
        # print(self.__response.raw)
        
        # self.__response.status_code
        if response.status_code == 200:
            self.__waitingLabel.show()
            self.label.setText("Welcome")
            name = data["name"]
            surname = data["surname"]
            tc = data["tc"]
            if data["role"] == "ROLE_ADMIN":
                
                self.close()
                time.sleep(1)
                self.newWindow = MainManager(name,surname,tc)
                self.newWindow.show()
            if data["role"] == "ROLE_DOCTOR":
                
                self.close()
                time.sleep(1)
                self.newWindow = MainManager(name,surname,tc)
                self.newWindow.show()
            if data["role"] == "ROLE_PATIENT":
                
                self.close()
                time.sleep(1)
                self.newWindow = GraphManager(data["tc"])
                # self.graphUi.updateInformation()
                self.newWindow.show()
        elif response.status_code == 404:
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
        self.pushButton.blockSignals(False)
        self.pushButton.setEnabled(True)
        self.__waitingLabel.close()            