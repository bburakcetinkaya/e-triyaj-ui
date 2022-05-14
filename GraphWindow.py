# -*- coding: utf-8 -*-

# GraphWindow implementation generated from reading ui file 'graphWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


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

class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.resize(800, 600)
        self.graphicsView = QtWidgets.QGraphicsView(GraphWindow)
        self.graphicsView.setGeometry(QtCore.QRect(15, 80, 770, 505))
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        # self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.graphicsView.setContentsMargins(0,0,0,0)
        self.graphicsView.setObjectName("graphicsView")

        self.startDateLabel = QtWidgets.QLabel(GraphWindow)
        self.startDateLabel.setGeometry(QtCore.QRect(40, 50, 55, 22))
        self.startDateLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.startDateLabel.setObjectName("startDateLabel")
        
        self.startDateEdit = QtWidgets.QDateEdit(GraphWindow)
        self.startDateEdit.setGeometry(QtCore.QRect(100, 50, 80, 22))
        self.startDateEdit.setAccelerated(True)
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setDisplayFormat("dd.MM.yyyy")
        self.startDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.startDateEdit.setObjectName("startDateEdit")
        self.startDateEdit.dateChanged.connect(self.updateGraph)
        
        self.endDateLabel = QtWidgets.QLabel(GraphWindow)
        self.endDateLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.endDateLabel.setGeometry(QtCore.QRect(190, 50, 55, 22))
        self.endDateLabel.setObjectName("endDateLabel")
        
        self.endDateEdit = QtWidgets.QDateEdit(GraphWindow)
        self.endDateEdit.setGeometry(QtCore.QRect(250, 50, 80, 22))
        self.endDateEdit.setAccelerated(True)
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDisplayFormat("dd.MM.yyyy")
        self.endDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.endDateEdit.setObjectName("endDateEdit")        
        self.endDateEdit.dateChanged.connect(self.updateGraph)
        
        # self.spO2CheckBox = QtWidgets.QCheckBox(GraphWindow)
        # self.spO2CheckBox.setGeometry(QtCore.QRect(610, 80, 91, 31))
        # self.spO2CheckBox.setObjectName("spO2CheckBox")
        # self.spO2CheckBox.setChecked(True)
        # self.spO2CheckBox.stateChanged.connect(self.spO2GraphDisplay)
        
        # self.hrCheckBox = QtWidgets.QCheckBox(GraphWindow)
        # self.hrCheckBox.setGeometry(QtCore.QRect(610, 110, 91, 31))
        # self.hrCheckBox.setObjectName("hrCheckBox")
        # self.hrCheckBox.setChecked(True)
        # self.hrCheckBox.stateChanged.connect(self.heartRateGraphDisplay)
        
        # self.temperatureChechBox = QtWidgets.QCheckBox(GraphWindow)
        # self.temperatureChechBox.setGeometry(QtCore.QRect(610, 140, 91, 31))
        # self.temperatureChechBox.setObjectName("temperatureChechBox")
        # self.temperatureChechBox.setChecked(True)
        # self.temperatureChechBox.stateChanged.connect(self.temperatureGraphDisplay)
        
        # self.bloodPressureCheckBox = QtWidgets.QCheckBox(GraphWindow)
        # self.bloodPressureCheckBox.setGeometry(QtCore.QRect(610, 170, 91, 31))
        # self.bloodPressureCheckBox.setChecked(True)
        # self.bloodPressureCheckBox.stateChanged.connect(self.bpGraphDisplay)    
        # self.bloodPressureCheckBox.setObjectName("bloodPressureCheckBox")
                

        
        self.horizontalLayoutWidget = QtWidgets.QWidget(GraphWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(37, 10, 681, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        
        self.nameEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.nameEdit.setMinimumSize(QtCore.QSize(120, 24))
        self.nameEdit.setMaximumSize(QtCore.QSize(120, 24))
        self.nameEdit.setObjectName("nameEdit")
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.nameEdit)
        
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        
        self.surnameEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.surnameEdit.setMinimumSize(QtCore.QSize(120, 24))
        self.surnameEdit.setMaximumSize(QtCore.QSize(120, 24))
        self.surnameEdit.setReadOnly(True)
        self.surnameEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.surnameEdit.setObjectName("surnameEdit")    
        
        self.horizontalLayout.addWidget(self.surnameEdit)
        
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        
        self.tcEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.tcEdit.setMinimumSize(QtCore.QSize(120, 24))
        self.tcEdit.setMaximumSize(QtCore.QSize(120, 24))
        self.tcEdit.setReadOnly(True)
        self.tcEdit.setObjectName("tcEdit")
        self.tcEdit.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.tcEdit)
        
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        
        self.ageEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.ageEdit.setMinimumSize(QtCore.QSize(120, 24))
        self.ageEdit.setMaximumSize(QtCore.QSize(120, 24))
        self.ageEdit.setReadOnly(True)
        self.ageEdit.setObjectName("ageEdit")
        #self.ageEdit.setAlignment(QtCore.Qt.AlignVCenter)
        # self.ageEdit.text.setAlignment(QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.ageEdit)

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "Graph Window"))
        # self.spO2CheckBox.setText(_translate("GraphWindow", "sp02"))
        # self.hrCheckBox.setText(_translate("GraphWindow", "Heart Rate"))
        # self.temperatureChechBox.setText(_translate("GraphWindow", "Temperature"))
        # self.bloodPressureCheckBox.setText(_translate("GraphWindow", "Blood Pressure"))

        self.startDateLabel.setText(_translate("GraphWindow", "Start Date:"))
        self.endDateLabel.setText(_translate("GraphWindow", "End Date:"))
        self.label_3.setText(_translate("GraphWindow", "Name:"))
        self.label_4.setText(_translate("GraphWindow", "Surname:"))
        self.label_5.setText(_translate("GraphWindow", "T.C. No:"))
        self.label_6.setText(_translate("GraphWindow", "Age:"))
        
    def updateGraph(self,date):
        print(date)
        self.endDateEdit.setMinimumDate(self.startDateEdit.date())
        self.startDateEdit.setMaximumDate(self.endDateEdit.date())
        self.endDateEdit.setMaximumDate(datetime.today())
        tc = self.tcEdit.toPlainText()
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
        else:
            self.printGraph(df)
        
        
    def updateInformation(self,tc):
        hr = HttpRequest()
        helper = Helper()
        
        df = hr.getEntriesByTc(tc)   
        self.printGraph(df)
        
        
    def printGraph(self,df):
        self.nameEdit.setPlainText(str(df.at[0,"NAME"]))
        self.surnameEdit.setPlainText(str(df.at[0,"SURNAME"]))
        self.tcEdit.setPlainText(str(df.at[0,"TC"]))
        self.ageEdit.setPlainText(str(df.at[0,"AGE"]))
        self.spO2 = np.array(df["SP02"])
        self.heartRate = np.array(df["HEARTRATE"])
        self.temperature = np.array(df[ "TEMPERATURE"])
        self.bloodPressure = [np.array(df["DIASTOLICBP"]),np.array(df["SYSTOLICBP"])]
        self.timeInterval = np.array(df["TIME"])

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
        
        
        self.plotWdgt.setBackground('k')
        self.legend = self.plotWdgt.addLegend(pen = 'k')
        self.legend.setBrush('w')
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
        self.plotWdgt.setYRange(-5, 180)
        self.plotWdgt.setXRange(0, 20, padding=0)
        self.plotWdgt.setYRange(0, 180, padding=0)
        self.scene = QGraphicsScene()
        # view->setSceneRect(0,0,view->frameSize().width(),view->frameSize().height());
        # self.scene.set
        # self.scene.setSceneRect(15,80,(770-15)/(450-15),(450-15)/(770-15))
        # 0, 0, self.painter.sceneRect().width() - self.view.frameWidth() * 2, 
        #     self.painter.sceneRect().height())
       # QtCore.QRect(15, 80, 770, 385))   
       # width+2*yourGraphicsView->frameWidth(), height+2*yourGraphicsView->frameWidth())
        self.scene.addWidget(self.plotWdgt)
        # self.scene.setF
        self.graphicsView.setScene(self.scene)
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
        
        
        
        
        
