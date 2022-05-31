# -*- coding: utf-8 -*-
"""
Created on Mon May 30 03:13:56 2022

@author: piton
"""
from MainWindow import Ui_MainWindow
from ManualEntryManager import ManualEntryManager
from httpRequests import HttpRequest
from printTable import PrintTable
from PyQt5.QtWidgets import QMessageBox
from GraphWindow import Ui_GraphWindow
import Helper
from PyQt5 import QtCore,QtWidgets
from thr import UpdateTableThread,UpdateTimeThread
import pandas as pd

class MainManager(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.dataHolder = pd.DataFrame({})
        # self.updateTable()
        # self.__tableThread = UpdateTableThread(self.updateTable,stopFlag)
        # self.__tableThread.start()
        # self.__timeThread = UpdateTimeThread(self.updateTime,stopFlag)
        # self.__timeThread.start()
        
        self.entryUi = ManualEntryManager()
        
        
    def connectSignalsSlots(self):
        self.tableView.doubleClicked.connect(self.openGraphWindow)
        self.manualEntryButton.clicked.connect(self.openManualEntryWindow)
        
    def updateTime(self):
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        
    def updateTable(self):
        helper = Helper.Helper()
        print("hello there")
        dayToBegin = helper.getPreviousNthDay(10)
        today = helper.getDate()
        hr = HttpRequest()
        data = pd.DataFrame({})
        # dayToBegin = helper.getPreviousNthDay(cnt+1)
        data = hr.getEntriesByDateInterval(dayToBegin,today)
      
        if data.empty:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("No records.")
            msg.setInformativeText('No records found in past 10 days.')
            msg.setWindowTitle("No records.")
            msg.adjustSize()                
            msg.exec_()       
            return
        if data.equals(self.dataHolder):
            return
        else:
            # print(dataHolder)
            self.dataHolder = pd.concat([data,self.dataHolder]).drop_duplicates().reset_index(drop=True)
            data.sort_values(by=['date','time'], ascending=[False,False],inplace=True)
            data.reset_index(drop=True, inplace=True)
            data.columns = map(str.upper, data.columns) 
            toPrint = PrintTable(data)
            self.tableView.setModel(toPrint)
             
    def openManualEntryWindow(self):
        global manualEntryWindow
        manualEntryWindow = QtWidgets.QMainWindow()        
        self.entryUi.show() 
        
    def openGraphWindow(self,signal):
        
        global GraphWindow
        GraphWindow = QtWidgets.QMainWindow()
        self.graphUi = Ui_GraphWindow()
        self._tc = signal.sibling(signal.row(),4).data()
        self.graphUi.setupUi(GraphWindow,self._tc)        
        self.graphUi.updateInformation(self._tc)
        GraphWindow.show()        
        # GraphWindow.exec_()