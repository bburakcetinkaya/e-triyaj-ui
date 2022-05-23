# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene
import matplotlib.pyplot as plt
from httpRequests import *
from Helper import *
from PyQt5.QtWidgets import QMessageBox
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime
import numpy as np
import pyqtgraph as pg
from printTable import *
from ManualEntryWindow import *
dataHolderPatient = pd.DataFrame({})


class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow,windowName):
        calendarWidgetStart = QtWidgets.QCalendarWidget()
        calendarWidgetStart.setStyleSheet(
                            # "QCalendarWidget QMenu  { alternate-background-color: rgb(128, 128, 128); }"
                            "QCalendarWidget QToolButton"
                            "{\n"
                            "color:black;\n"
                            "}\n"
                            # "QCalendarWidget QToolButton::hover\n"
                            # "{\n"
                            # "background-color : cyan;\n"
                            # "}\n"
                            # "QCalendarWidget QToolButton::pressed\n"
                            # "{\n"
                            # "background-color : blue;\n"
                            # "}\n"
                            )
        calendarWidgetEnd = QtWidgets.QCalendarWidget()
        calendarWidgetEnd.setStyleSheet(
                            # "QCalendarWidget QMenu  { alternate-background-color: rgb(128, 128, 128); }"
                            "QCalendarWidget QToolButton"
                            "{\n"
                            "color:black;\n"
                            "}\n"
                            # "QCalendarWidget QToolButton::hover\n"
                            # "{\n"
                            # "background-color : cyan;\n"
                            # "}\n"
                            # "QCalendarWidget QToolButton::pressed\n"
                            # "{\n"
                            # "background-color : blue;\n"
                            # "}\n"
                            )
        self._windowName = windowName
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.resize(1031, 631)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GraphWindow.sizePolicy().hasHeightForWidth())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GraphWindow.setWindowIcon(icon)
        GraphWindow.setSizePolicy(sizePolicy)
        GraphWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayoutWidget = QtWidgets.QWidget(GraphWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(11, 11, 1011, 611))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.nameEdit.setStyleSheet("QLineEdit {\n"
"    background-color:  rgb(255,255,255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120);\n"
"    font: bold 14px;\n"
"    color: black;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"}")
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.surnameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.surnameLabel.setObjectName("surnameLabel")
        self.horizontalLayout.addWidget(self.surnameLabel)
        self.surnameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.surnameEdit.setStyleSheet("QLineEdit {\n"
"    background-color:  rgb(255,255,255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120);\n"
"    font: bold 14px;\n"
"    color: black;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"}")
        self.surnameEdit.setReadOnly(True)
        self.surnameEdit.setObjectName("surnameEdit")
        self.horizontalLayout.addWidget(self.surnameEdit)
        self.tcLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.tcLabel.setObjectName("tcLabel")
        self.horizontalLayout.addWidget(self.tcLabel)
        self.tcEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tcEdit.setStyleSheet("QLineEdit {\n"
"    background-color:  rgb(255,255,255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120);\n"
"    font: bold 14px;\n"
"    color: black;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"}")
        self.tcEdit.setReadOnly(True)
        self.tcEdit.setObjectName("tcEdit")
        self.horizontalLayout.addWidget(self.tcEdit)
        self.ageLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ageLabel.setObjectName("ageLabel")
        self.horizontalLayout.addWidget(self.ageLabel)
        self.ageEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ageEdit.setStyleSheet("QLineEdit {\n"
"    background-color:  rgb(255,255,255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120);\n"
"    font: bold 14px;\n"
"    color: black;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"}")
        self.ageEdit.setReadOnly(True)
        self.ageEdit.setObjectName("ageEdit")
        self.horizontalLayout.addWidget(self.ageEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.manualEntryButton = QtWidgets.QPushButton(self.gridLayoutWidget)
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
        self.manualEntryButton.clicked.connect(self.onManualEntry)
        self.horizontalLayout.addWidget(self.manualEntryButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startDateLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.startDateLabel.setObjectName("startDateLabel")
        self.horizontalLayout_2.addWidget(self.startDateLabel)
        self.startDateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.startDateEdit.setStyleSheet("QDateEdit {\n"
"    background-color:  rgb(255,255,255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120);\n"
"    font: bold 14px;\n"
"    color: black;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"}\n"
"QDateEdit::drop-down \n"
"{\n"
"    border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"}\n"
"QDateEdit::down-arrow {\n"
"    image: url(../logo/down_arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}")
        self.startDateEdit.setAccelerated(True)
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setObjectName("startDateEdit")
        self.startDateEdit.setDate(QtCore.QDate.currentDate())
        self.startDateEdit.setCalendarWidget(calendarWidgetStart)
        self.horizontalLayout_2.addWidget(self.startDateEdit)
        self.editDateLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.editDateLabel.setObjectName("editDateLabel")
        self.horizontalLayout_2.addWidget(self.editDateLabel)
        self.endDateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.endDateEdit.setStyleSheet("QDateEdit {\n"
"    background-color:  rgb(255,255,255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120);\n"
"    font: bold 14px;\n"
"    color: black;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"}\n"
"QDateEdit::drop-down \n"
"{\n"
"    border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"}\n"
"QDateEdit::down-arrow {\n"
"    image: url(../logo/down_arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}")
        self.endDateEdit.setAccelerated(True)
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setObjectName("endDateEdit")
        self.endDateEdit.setDate(QtCore.QDate.currentDate())
        self.endDateEdit.setCalendarWidget(calendarWidgetEnd)
        self.horizontalLayout_2.addWidget(self.endDateEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.graphTab = QtWidgets.QWidget()
        self.graphTab.setObjectName("graphTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.graphTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.graphTab)
        self.graphicsView.setStyleSheet("QScrollBar:vertical {           \n"
"                            border: 1px solid #999999;\n"
"                           background:white;\n"
"                            width:10px;    \n"
"                            margin: 0px 0px 0px 0px;\n"
"                        }\n"
"                       QScrollBar::handle:vertical {\n"
"                            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0 rgb(0,0,120), stop: 0.5 rgb(0,0,120), stop:1 rgb(0,0,120));\n"
"                            min-height: 0px;\n"
"                        }\n"
"                        QScrollBar::add-line:vertical {\n"
"                           background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0 rgb(0,0,120), stop: 0.5 rgb(0,0,120),  stop:1 rgb(0,0,120));\n"
"                            height: 0px;\n"
"                          subcontrol-position: bottom;\n"
"                            subcontrol-origin: margin;\n"
"                        }\n"
"                        QScrollBar::sub-line:vertical {\n"
"                            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0  rgb(0,0,120), stop: 0.5 rgb(0,0,120),  stop:1 rgb(0,0,120));\n"
"                            height: 0 px;\n"
"                          subcontrol-position: top;\n"
"                            subcontrol-origin: margin;\n"
"                        }\n"
"QScrollBar:horizontal {           \n"
"                            border: 1px solid #999999;\n"
"                           background:white;\n"
"                            width:10px;    \n"
"                            margin: 0px 0px 0px 0px;\n"
"                        }\n"
"                       QScrollBar::handle:horizontal {\n"
"                            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0 rgb(0,0,120), stop: 0.5 rgb(0,0,120), stop:1 rgb(0,0,120));\n"
"                            min-height: 0px;\n"
"                        }\n"
"                        QScrollBar::add-line:horizontal {\n"
"                           background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0 rgb(0,0,120), stop: 0.5 rgb(0,0,120),  stop:1 rgb(0,0,120));\n"
"                            height: 0px;\n"
"                          subcontrol-position: bottom;\n"
"                            subcontrol-origin: margin;\n"
"                        }\n"
"                        QScrollBar::sub-line:horizontal {\n"
"                            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0  rgb(0,0,120), stop: 0.5 rgb(0,0,120),  stop:1 rgb(0,0,120));\n"
"                            height: 0 px;\n"
"                          subcontrol-position: top;\n"
"                            subcontrol-origin: margin;\n"
"                        }")
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.graphTab, "")
        self.tableTab = QtWidgets.QWidget()
        self.tableTab.setObjectName("tableTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tableTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableView = QtWidgets.QTableView(self.tableTab)
        self.tableView.setStyleSheet("QScrollBar:vertical {           \n"
"                            border: 1px solid #999999;\n"
"                           background:white;\n"
"                            width:10px;    \n"
"                            margin: 0px 0px 0px 0px;\n"
"                        }\n"
"                       QScrollBar::handle:vertical {\n"
"                            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0 rgb(0,0,120), stop: 0.5 rgb(0,0,120), stop:1 rgb(0,0,120));\n"
"                            min-height: 0px;\n"
"                        }\n"
"                        QScrollBar::add-line:vertical {\n"
"                           background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0 rgb(0,0,120), stop: 0.5 rgb(0,0,120),  stop:1 rgb(0,0,120));\n"
"                            height: 0px;\n"
"                          subcontrol-position: bottom;\n"
"                            subcontrol-origin: margin;\n"
"                        }\n"
"                        QScrollBar::sub-line:vertical {\n"
"                            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0  rgb(0,0,120), stop: 0.5 rgb(0,0,120),  stop:1 rgb(0,0,120));\n"
"                            height: 0 px;\n"
"                          subcontrol-position: top;\n"
"                            subcontrol-origin: margin;\n"
"                        }\n"
"QScrollBar:horizontal {           \n"
"                            border: 1px solid #999999;\n"
"                           background:white;\n"
"                            width:10px;    \n"
"                            margin: 0px 0px 0px 0px;\n"
"                        }\n"
"                       QScrollBar::handle:horizontal {\n"
"                            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0 rgb(0,0,120), stop: 0.5 rgb(0,0,120), stop:1 rgb(0,0,120));\n"
"                            min-height: 0px;\n"
"                        }\n"
"                        QScrollBar::add-line:horizontal {\n"
"                           background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0 rgb(0,0,120), stop: 0.5 rgb(0,0,120),  stop:1 rgb(0,0,120));\n"
"                            height: 0px;\n"
"                          subcontrol-position: bottom;\n"
"                            subcontrol-origin: margin;\n"
"                        }\n"
"                        QScrollBar::sub-line:horizontal {\n"
"                            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                            stop: 0  rgb(0,0,120), stop: 0.5 rgb(0,0,120),  stop:1 rgb(0,0,120));\n"
"                            height: 0 px;\n"
"                          subcontrol-position: top;\n"
"                            subcontrol-origin: margin;\n"
"                        }")
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setObjectName("tableView")
        self.gridLayout_4.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tableTab, "")
        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 50)

        self.retranslateUi(GraphWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)
        
        self.startDateEdit.dateChanged.connect(self.updateInformationByDate)
        self.endDateEdit.dateChanged.connect(self.updateInformationByDate)


    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", self._windowName))
        self.nameLabel.setText(_translate("GraphWindow", "Name:"))
        self.surnameLabel.setText(_translate("GraphWindow", "Surname:"))
        self.tcLabel.setText(_translate("GraphWindow", "T.C. No:"))
        self.ageLabel.setText(_translate("GraphWindow", "Age:"))
        self.manualEntryButton.setText(_translate("GraphWindow", "Manual Entry"))
        self.startDateLabel.setText(_translate("GraphWindow", "Start Date:"))
        self.startDateEdit.setDisplayFormat(_translate("GraphWindow", "d/M/yyyy"))
        self.editDateLabel.setText(_translate("GraphWindow", "End Date:"))
        self.endDateEdit.setDisplayFormat(_translate("GraphWindow", "d/M/yyyy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphTab), _translate("GraphWindow", "Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tableTab), _translate("GraphWindow", "Table"))

    def onManualEntry(self):
        # global manualEntryWindow
        self.manualEntryWindow = QtWidgets.QMainWindow()
        self.ui = Ui_manualEntryWindow()
        self.ui.setupUi(self.manualEntryWindow)
        self.ui.ageEdit.setText(self.ageEdit.text())
        self.ui.ageEdit.setReadOnly(True)
        self.ui.nameEdit.setText(self.nameEdit.text())
        self.ui.nameEdit.setReadOnly(True)
        self.ui.surnameEdit.setText(self.surnameEdit.text())
        self.ui.surnameEdit.setReadOnly(True)
        self.ui.tcEdit.setText(self.tcEdit.text())
        self.ui.tcEdit.setReadOnly(True)
        # print(self.gender)
        if self.gender[0] == "MALE":
            self.ui.genderComboBox.setCurrentIndex(1)    
        if self.gender[0] == "FEMALE":        
            self.ui.genderComboBox.setCurrentIndex(2)
        self.ui.genderComboBox.setEnabled(False)

        self.manualEntryWindow.show()
        if self.ui.closing():
            self.manualEntryWindow.close()
        # self.manualEntryWindow.closeEvent(self.updateInformation(self.tcEdit.text()))
        
    def printTable(self,data):

        toPrint = PrintTable(data)
        self.tableView.setModel(toPrint)
        
    
    def updateInformationByDate(self,tc):
        global dataHolderPatient
        self.endDateEdit.setMinimumDate(self.startDateEdit.date())
        self.startDateEdit.setMaximumDate(self.endDateEdit.date())
        self.endDateEdit.setMaximumDate(datetime.today())
        tc = self.tcEdit.text()
        startDate = self.startDateEdit.date().toString(QtCore.Qt.ISODate)
        endDate = self.endDateEdit.date().toString(QtCore.Qt.ISODate)
        hr = HttpRequest()
        df = hr.getEntriesByDateIntervalAndTc(startDate,endDate,tc)
        
        if df.empty:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText('No records found!')
            msg.setWindowTitle("Error")
            msg.exec_()
            self.endDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
            self.startDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())            
        elif df.equals(dataHolderPatient):
            return
        else:
            self.printTable(df)
            self.printGraph(df)
            
        
    def updateInformation(self,tc):
        hr = HttpRequest()
        helper = Helper()
        
        df = hr.getEntriesByTc(tc)   
        self.printGraph(df)
        self.printTable(df)
     
   
        
        
    def printGraph(self,df):
        self.nameEdit.setText(str(df.at[0,"NAME"]))
        self.surnameEdit.setText(str(df.at[0,"SURNAME"]))
        self.tcEdit.setText(str(df.at[0,"TC"]))
        self.ageEdit.setText(str(df.at[0,"AGE"]))
        self.spO2 = np.array(df["SP02"])
        self.heartRate = np.array(df["HEARTRATE"])
        self.temperature = np.array(df[ "TEMPERATURE"])
        self.bloodPressure = [np.array(df["DIASTOLICBP"]),np.array(df["SYSTOLICBP"])]
        self.timeInterval = np.array(df["TIME"])
        self.gender = np.array(df["GENDER"])

        self.plotWdgt = pg.PlotWidget()

        self.red =  pg.mkPen(color=(255, 0, 0), width=2)
        self.green = pg.mkPen(color=(0, 255, 0), width=2)
        self.blue = pg.mkPen(color=(0, 0, 255), width=2)
        self.lightBlue = pg.mkPen(color=(173,216,230), width=2)
        self.purple = pg.mkPen(color=(106, 13, 173), width=2)
      
        self.redMarker = pg.mkBrush(color=(255, 0, 0))
        self.greenMarker = pg.mkBrush(color=(0, 255, 0))
        self.blueMarker = pg.mkBrush(color=(0, 0, 255))
        self.lightBlueMarker = pg.mkBrush(color=(173,216,230))
        self.purpleMarker = pg.mkBrush(color=(106, 13, 173))
        
        
        self.plotWdgt.setBackground('w')
        self.legend = self.plotWdgt.addLegend(pen = 'k')
        self.legend.setBrush('grey')
        # self.legend.pen()
        self.plotWdgt.showGrid(x=True, y=True)
        
        self.plotWdgt.enableAutoRange(axis='x')
        self.plotWdgt.enableAutoRange(axis='y')
        self.plotWdgt.setAutoVisible(x=True,y=True)
        
        self.spo2_graph = self.plotWdgt.plot(self.spO2,pen=self.red,symbol='o', symbolBrush=self.redMarker ,name="spO2")      
        self.heartRate_graph = self.plotWdgt.plot(self.heartRate,pen=self.green,symbol='o', symbolBrush=self.greenMarker,name="heartRate")
        self.temperature_graph = self.plotWdgt.plot(self.temperature,pen=self.purple,symbol='o', symbolBrush=self.purpleMarker,name="temperature")
        self.diastolic_graph = self.plotWdgt.plot(self.bloodPressure[0],pen=self.lightBlue,symbol='o', symbolBrush=self.lightBlueMarker,name="diastolicBP")
        self.systolic_graph = self.plotWdgt.plot(self.bloodPressure[1],pen=self.blue,symbol='o', symbolBrush=self.blueMarker,name="systolicBP")
        # self.plotWdgt.setYRange(-5, 180)
        # self.plotWdgt.setXRange(0, 20, padding=0)
        # self.plotWdgt.setYRange(0, 180, padding=0)
        self.scene = QGraphicsScene()
        # view->setSceneRect(0,0,view->frameSize().width(),view->frameSize().height());
        # self.scene.set
        # self.scene.setSceneRect(15,80,(770-15)/(450-15),(450-15)/(770-15))
        # 0, 0, self.painter.sceneRect().width() - self.view.frameWidth() * 2, 
        #     self.painter.sceneRect().height())
       # QtCore.QRect(15, 80, 770, 385))   
       # width+2*yourGraphicsView->frameWidth(), height+2*yourGraphicsView->frameWidth())
        self.scene.addWidget(self.plotWdgt)
        # self.scene.set
        # self.scene.setF
        self.graphicsView.setScene(self.scene)
        # self.graphicsView.setSizeAdjustPolicy()
        # self.graphicsView.fitInView(self.scene)
        # self.scene.s
        # width = 770-15
        # height = 385-15
        # xcenter = width/2
        # ycenter = height/2        
        # self.scene.setSceneRect(0,0,width+xcenter,height+ycenter)
        # self.graphicsView.setSceneRect(0,0,200,200)
        
        
        
        
    
    # def spO2GraphDisplay(self,state):
    #     if ~state:
    #         self.plotWdgt.removeItem(self.spo2_graph)
    #     if state:
    #         self.spo2_graph = self.plotWdgt.plot(self.spO2,pen=self.red,symbol='o', symbolBrush=self.redMarker,name="spO2")      
    
    # def heartRateGraphDisplay(self,state):
    #     if ~state:
    #         self.plotWdgt.removeItem(self.heartRate_graph)
    #     if state:
    #         self.heartRate_graph = self.plotWdgt.plot(self.heartRate, pen=self.green,symbol='o', symbolBrush=self.greenMarker,name="heartRate")
            
    # def temperatureGraphDisplay(self,state):
    #     if ~state:
    #         self.plotWdgt.removeItem(self.temperature_graph)
    #     if state:
    #         self.temperature_graph = self.plotWdgt.plot(self.temperature, pen=self.purple, symbol='o', symbolBrush=self.purpleMarker,name="temperature")
    # def bpGraphDisplay(self,state):
    #     if ~state:             
    #          self.plotWdgt.removeItem(self.diastolic_graph)
    #          self.plotWdgt.removeItem(self.systolic_graph)
    #     if state:
    #          self.diastolic_graph = self.plotWdgt.plot(self.bloodPressure[0],pen=self.lightBlue,symbol='o', symbolBrush=self.lightBlueMarker,name="diastolicBP")
    #          self.systolic_graph = self.plotWdgt.plot(self.bloodPressure[1],pen=self.blue,symbol='o', symbolBrush=self.blueMarker,name="systolicBP")     
    
        
        # self.graphicsView.plot(spO2)