# -*- coding: utf-8 -*-
"""
Created on Mon May 30 03:13:56 2022

@author: piton
"""
from MainWindow import Ui_MainWindow
from ManualEntryManager import ManualEntryManager
import LoginManager
from httpRequests import HttpRequest
from printTable import PrintTable
from PyQt5.QtWidgets import QMessageBox
from GraphManager import GraphManager
import Helper
from PyQt5 import QtCore,QtWidgets

from thr import UpdateThread
import pandas as pd
import threading
import time

class MainManager(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,role,name,surname,tc,showOnlyMyPatientsButton=True,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.dataHolder = pd.DataFrame({})
        self.startThreads()
        self.onlyMyPatients_button.setVisible(showOnlyMyPatientsButton)
        self.onlyMyPatients_button.setCheckable(True)
        
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.showFullScreen()
        self.__tc = tc
        self.__role = role
       
        # self.__name = name
        # self.__surname = surname
        self.nameSurname_label.setText(name+" "+surname)
        
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        self.updateTable()        
        self.connectSignalsSlots()
       
    def connectSignalsSlots(self):
        self.tableView.doubleClicked.connect(self.openGraphWindow)
        self.manualEntryButton.clicked.connect(self.openManualEntryWindow)
        self.exitButton.clicked.connect(lambda: self.close())
        self.logout_button.clicked.connect(self.logout)
        self.onlyMyPatients_button.clicked.connect(self.onlyMyPatients_button_isChecked)
        # main.app.aboutToQuit.connect(self.closeEvent)
    def closeEvent(self,event):
        self.stopTableUpdateFlag.set()
        self.stopTimeUpdateFlag.set()
	
    def startThreads(self):
        self.stopTableUpdateFlag = threading.Event()
        self.stopTimeUpdateFlag = threading.Event()
        
        self.tableThread = UpdateThread(self.updateTable,self.stopTableUpdateFlag,5)
        self.timeThread = UpdateThread(self.updateTime,self.stopTimeUpdateFlag,1)
        
        self.timeThread.start()
        time.sleep(1)
        self.tableThread.start()
        
    def onlyMyPatients_button_isChecked(self):
        if self.onlyMyPatients_button.isChecked():
            self.onlyMyPatients_button.setStyleSheet("QPushButton {\n"
    "    background-color:  rgb(0,220,32);\n"
    "    border-style: outset;\n"
    "    border-width: 2px;\n"
    "    border-radius: 10px;\n"
    "    border-color: rgb(0, 0, 120);\n"
    "    font: bold 14px;\n"
    "    color: black;\n"
    "    min-width: 10em;\n"
    "    padding: 6px;\n"
    "}\n"
    "QPushButton:pressed {\n"
    "    background-color: rgb(0, 0, 150);\n"
    "    border-style: inset;\n"
    "}")
        else:
            self.onlyMyPatients_button.setStyleSheet("QPushButton {\n"
    "    background-color:  rgb(255,255,255);\n"
    "    border-style: outset;\n"
    "    border-width: 2px;\n"
    "    border-radius: 10px;\n"
    "    border-color: rgb(0, 0, 120);\n"
    "    font: bold 14px;\n"
    "    color: black;\n"
    "    min-width: 10em;\n"
    "    padding: 6px;\n"
    "}\n"
    "QPushButton:pressed {\n"
    "    background-color: rgb(0, 0, 150);\n"
    "    border-style: inset;\n"
    "}")
        
    def logout(self):
        
        self.window = LoginManager.LoginManager()
        self.window.show()
        self.close()
    def updateTime(self):
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        
    def updateTable(self):
        print("Table updating...")
        helper = Helper.Helper()
        dayToBegin = helper.getPreviousNthDay(10)
        today = helper.getDate()
        hr = HttpRequest()
        data = pd.DataFrame({})
        data = hr.getEntriesByDateInterval(dayToBegin,today,self.__tc,self.__role)
        
        if data.empty:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("No records.")
            msg.setInformativeText('No records found in past 10 days.')
            msg.setWindowTitle("No records.")
            msg.adjustSize()                
            msg.exec_()       
            return
        elif data.equals(self.dataHolder):
            return
        else:         
            self.dataHolder = pd.concat([data,self.dataHolder]).drop_duplicates().reset_index(drop=True)
            toPrint = PrintTable(data)
            self.tableView.setModel(toPrint)
            self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            # horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
        
    def openManualEntryWindow(self): 
        self.entryUi = ManualEntryManager()
        self.entryUi.show()       
        
    def openGraphWindow(self,signal):        
             
        self.__tc = signal.sibling(signal.row(),4).data()  
        self.graphUi = GraphManager(self.__tc,self.__tc,self.__role) 
        # self.graphUi.updateInformation()
        # self.graphUi.setTc()
        # self.graphUi.updateInformation()
        # self.graphUi.updateInformation(self.__tc)
        self.graphUi.show()        
        # GraphWindow.exec_()