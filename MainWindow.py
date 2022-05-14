# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from ManualEntryWindow import *
from httpRequests import *
from printTable import *
from PyQt5.QtWidgets import QMessageBox
from GraphWindow import *
from Helper import *
from PyQt5 import QtCore, QtGui, QtWidgets
from thr import *
stopFlag = Event()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")        
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        # self.mainFrame.setStyleSheet("background-color: #b00b69;")
        self.mainFrame.setGeometry(QtCore.QRect(10, 40, 981, 521))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mainFrame.setObjectName("mainFrame")
        
        self.tabWidget = QtWidgets.QTabWidget(self.mainFrame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 951, 501))        
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        
        self.lastEntries = QtWidgets.QWidget()
        self.lastEntries.setAccessibleName("")
        self.lastEntries.setObjectName("lastEntries")
        
        self.entryTable = QtWidgets.QTableView(self.lastEntries)
        self.entryTable.setGeometry(QtCore.QRect(10, 20, 941, 451))
        self.entryTable.verticalHeader().hide()
        self.entryTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.entryTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.entryTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entryTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.entryTable.setObjectName("entryTable")
        self.entryTable.doubleClicked.connect(self.openGraphWindow) 
        # self.entryTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        # self.entryTable.resizeColumnsToContents()
        self.tabWidget.addTab(self.lastEntries, "")
        
        self.seeEntriesTab = QtWidgets.QWidget()
        self.seeEntriesTab.setObjectName("seeEntriesTab")
        
        self.tabWidget.addTab(self.seeEntriesTab, "")
        
        self.dateTime = QtWidgets.QDateTimeEdit(self.mainFrame)
        self.dateTime.setGeometry(QtCore.QRect(843, 10, 121, 31))
        self.dateTime.setReadOnly(True)
        # self.dateTime.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTime.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTime.setCalendarPopup(True)
        self.dateTime.setObjectName("dateTime")
        
        self.manualEntryButton = QtWidgets.QPushButton(self.mainFrame)
        self.manualEntryButton.setGeometry(QtCore.QRect(744, 10, 81, 31))
        self.manualEntryButton.setObjectName("manualEntryButton")
        self.manualEntryButton.clicked.connect(self.openManualEntryWindow)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 21))
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)  
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        thread = UpdateTableThread(self.updateTable,stopFlag)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
       
    def updateTable(self):
        helper = Helper()
        hr = HttpRequest()
        data = hr.getEntriesByDateInterval(helper.getYesterday(),helper.getDate())
        if data.empty:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Fail")
            msg.setInformativeText('Failed to find records.')
            msg.setWindowTitle("Fail")
            msg.exec_()
            return
        toPrint = PrintTable(data)
        self.entryTable.setModel(toPrint)
        
    def openManualEntryWindow(self):

        manualEntryWindow = QtWidgets.QMainWindow()
        ui = Ui_manualEntryWindow()
        ui.setupUi(manualEntryWindow)
        manualEntryWindow.show()
        
        manualEntryWindow.exec_()
        
    def openGraphWindow(self,signal):
        GraphWindow = QtWidgets.QMainWindow()
        ui = Ui_GraphWindow()
        ui.setupUi(GraphWindow)
        self._tc = signal.sibling(signal.row(),4).data()
        ui.updateInformation(self._tc)
        GraphWindow.show()
        
        GraphWindow.exec_()
        
        

        
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "E-Triyaj"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lastEntries), _translate("MainWindow", "Last Entries"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.seeEntriesTab), _translate("MainWindow", "????"))
        self.dateTime.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy hh:mm"))
        self.manualEntryButton.setText(_translate("MainWindow", "Manual Entry"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">E-Triyaj Ui</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
