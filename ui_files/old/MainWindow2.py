# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from ManualEntryWindow import *
from httpRequests import *
from printTable import *
from PyQt5.QtWidgets import QMessageBox
from GraphWindow import *
from Helper import *
from PyQt5 import QtCore, QtGui, QtWidgets
from thr import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1304, 700)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("gridline-color: rgb(0, 0, 100);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.headerHorizontalLayout = QtWidgets.QHBoxLayout()
        self.headerHorizontalLayout.setObjectName("headerHorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.headerHorizontalLayout.addItem(spacerItem)
        self.eTriageLogo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eTriageLogo.sizePolicy().hasHeightForWidth())
        self.eTriageLogo.setSizePolicy(sizePolicy)
        self.eTriageLogo.setMaximumSize(QtCore.QSize(341, 81))
        self.eTriageLogo.setStyleSheet("background-color: transparent;")
        self.eTriageLogo.setText("")
        self.eTriageLogo.setTextFormat(QtCore.Qt.AutoText)
        self.eTriageLogo.setPixmap(QtGui.QPixmap("../logo/e-triage.png"))
        self.eTriageLogo.setScaledContents(True)
        self.eTriageLogo.setWordWrap(True)
        self.eTriageLogo.setObjectName("eTriageLogo")
        self.headerHorizontalLayout.addWidget(self.eTriageLogo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headerHorizontalLayout.addItem(spacerItem1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setEnabled(True)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setAutoFillBackground(False)
        self.dateTimeEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.dateTimeEdit.setFrame(False)
        self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setKeyboardTracking(False)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.headerHorizontalLayout.addWidget(self.dateTimeEdit, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.headerHorizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.headerHorizontalLayout, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("color: rgb(85, 85, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.tableHorizontalLayout = QtWidgets.QHBoxLayout()
        self.tableHorizontalLayout.setObjectName("tableHorizontalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.tableHorizontalLayout.addWidget(self.tableView)
        self.tableView.verticalHeader().hide()
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.entryTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.doubleClicked.connect(self.openGraphWindow)
        
        self.gridLayout.addLayout(self.tableHorizontalLayout, 4, 0, 1, 1)
        self.searchHorizontalLayout = QtWidgets.QHBoxLayout()
        self.searchHorizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.searchHorizontalLayout.setObjectName("searchHorizontalLayout")
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy)
        self.searchLineEdit.setMinimumSize(QtCore.QSize(206, 0))
        self.searchLineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.searchLineEdit.setStyleSheet("QLineEdit {\n"
"    background-color:  rgb(255,255,255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120);\n"
"    font: bold 14px;\n"
"    color: grey;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QLineEdit::hasFocus\n"
"{\n"
"color:black;\n"
"}")
        self.searchLineEdit.setText("")
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.searchHorizontalLayout.addWidget(self.searchLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.searchHorizontalLayout.addItem(spacerItem3)
        self.manualEntryButton = QtWidgets.QPushButton(self.centralwidget)
        self.manualEntryButton.setStyleSheet("QPushButton {\n"
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
        self.manualEntryButton.setObjectName("manualEntryButton")
        self.searchHorizontalLayout.addWidget(self.manualEntryButton, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.manualEntryButton.clicked.connect(self.openManualEntryWindow)
        self.gridLayout.addLayout(self.searchHorizontalLayout, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setStyleSheet("color: rgb(85, 85, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 50)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1304, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "E-Triyaj"))
        self.searchLineEdit.setPlaceholderText(_translate("MainWindow", "Search."))
        self.manualEntryButton.setText(_translate("MainWindow", "Manual Entry"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save Table"))
    
    def updateTable(self):
        stopFlag.set()
        helper = Helper()
        dayToBegin = helper.getPreviousNthDay(1)
        today = helper.getDate()
        hr = HttpRequest()
        data = pd.DataFrame({})    
        cnt = 1
        while data.empty:  
            
            dayToBegin = helper.getPreviousNthDay(cnt+1)
            data = hr.getEntriesByDateInterval(dayToBegin,today)
            print(dayToBegin,"    ",today)
            cnt += 1 
            if cnt == 10:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("No records.")
                msg.setInformativeText('No records found in past 10 days.')
                msg.setWindowTitle("No records.")
                msg.adjustSize()                
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
        

