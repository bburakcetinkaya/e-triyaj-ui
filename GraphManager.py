# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:45:19 2022

@author: piton
"""
from PyQt5 import QtWidgets,QtCore,QtGui

from GraphWindow import Ui_GraphWindow
import LoginManager
from ManualEntryManager import ManualEntryManager

from Helper import Helper
from printTable import PrintTable
from PyQt5.QtWidgets import QMessageBox

from httpRequests import HttpRequest

from datetime import datetime
import numpy as np
import pyqtgraph as pg
import pandas as pd
import time

dataHolderPatient = pd.DataFrame({})

class GraphManager(QtWidgets.QMainWindow,Ui_GraphWindow):
    def __init__(self,doctorID,tc,role="ROLE_ADMIN",parent=None):
        super().__init__(parent)
        
        self.setupUi(self)
        self.connectSignalsSlots()
        self.scene = QtWidgets.QGraphicsScene(self) 
        self.__tc = tc
        self.__role = role
        self.__doctorID = doctorID
        self.updateInformation()
        
        
        
    def connectSignalsSlots(self):
        self.manualEntryButton.clicked.connect(self.onManualEntry)
        self.startDateEdit.dateChanged.connect(self.updateInformationByDate)
        self.endDateEdit.dateChanged.connect(self.updateInformationByDate)
        self.exitButton.clicked.connect(lambda: self.close())
        self.logout_button.clicked.connect(self.logout)
    def logout(self):
        
        self.window = LoginManager.LoginManager()
        self.window.show()
        self.close()
    def setTc(self,tc):
        self.__tc = tc
    def getTc(self):
        return self.__tc
    def onManualEntry(self):
        
        
        self.ui = ManualEntryManager()
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

        self.ui.show()
        # if self.ui.closing():
        # self.manualEntryWindow.close()
        # self.manualEntryWindow.closeEvent(self.updateInformation(self.tcEdit.text()))
        
    def printTable(self,data):
        data.pop("NAME")
        data.pop("TC")
        data.pop("SURNAME")
        data.pop("GENDER")
        data.pop("AGE")
        
        toPrint = PrintTable(data)
        self.tableView.setModel(toPrint)
        
    
    def updateInformationByDate(self):
        global dataHolderPatient
        self.endDateEdit.setMinimumDate(self.startDateEdit.date())
        self.startDateEdit.setMaximumDate(self.endDateEdit.date())
        self.endDateEdit.setMaximumDate(datetime.today())
        tc = self.tcEdit.text()
        startDate = self.startDateEdit.date().toString(QtCore.Qt.ISODate)
        endDate = self.endDateEdit.date().toString(QtCore.Qt.ISODate)
        hr = HttpRequest()
        df = hr.getEntriesByDateIntervalAndTc(startDate,endDate,tc,self.__doctorID,self.__role)
        
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
            # a = QtGui.QResizeEvent(QtGui.QResizeEvent.size(),QtGui.QResizeEvent.oldSize())
            # self.resizeEvent(a)
            
        
    def updateInformation(self):
        hr = HttpRequest()        
        tc = self.__tc    
        print("update info tc :" ,tc)
        df = hr.getEntriesByTc(tc,self.__doctorID,self.__role)   
        self.printGraph(df)
        self.printTable(df)
        # a = QtGui.QResizeEvent(QtGui.QResizeEvent.size(),QtGui.QResizeEvent.oldSize())
        # self.resizeEvent(a)
    def resizeEvent(self,event):

        self.graphicsView.fitInView(0,0,self.scene.width(),self.scene.height())
        QtWidgets.QMainWindow.resizeEvent(self, event)
        
    def resizeEvent2(self):
        self.graphicsView.fitInView(0,0,self.scene.width(),self.scene.height())
        
    def printGraph(self,df):
        
        print(df)
        self.nameEdit.setText(str(df.at[0,"NAME"]))
        self.surnameEdit.setText(str(df.at[0,"SURNAME"]))
        self.tcEdit.setText(str(df.at[0,"TC"]))
        self.ageEdit.setText(str(df.at[0,"AGE"]))
        if str(df.at[0,"GENDER"]) == "MALE":            
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("logo/male_gender.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.genderDisplay.setIcon(icon)
        if str(df.at[0,"GENDER"]) == "FEMALE":
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("logo/female_gender.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.genderDisplay.setIcon(icon)
        self.spO2 = np.array(df["SP02"])
        self.heartRate = np.array(df["HEARTRATE"])
        self.temperature = np.array(df[ "TEMPERATURE"])
        self.bloodPressure = [np.array(df["DIASTOLICBP"]),np.array(df["SYSTOLICBP"])]
        self.timeInterval = np.array(df["TIME"])
        self.gender = np.array(df["GENDER"])
        

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
        
        self.plotWdgt = pg.PlotWidget()
        self.plotWdgt.setBackground('w')
        self.legend = self.plotWdgt.addLegend(pen = 'k')
        self.legend.setBrush('white')
        # self.legend.pen()
        self.plotWdgt.showGrid(x=True, y=True)
        self.plotWdgt.setXRange(40,4)
        
        self.plotWdgt.enableAutoRange(axis='x')
        self.plotWdgt.enableAutoRange(axis='y')
        self.plotWdgt.setAutoVisible(x=True,y=True)
        
        self.spo2_graph = self.plotWdgt.plot(self.spO2,pen=self.red,symbol='o', symbolBrush=self.redMarker ,name="spO2")      
        self.heartRate_graph = self.plotWdgt.plot(self.heartRate,pen=self.green,symbol='o', symbolBrush=self.greenMarker,name="heartRate")
        self.temperature_graph = self.plotWdgt.plot(self.temperature,pen=self.purple,symbol='o', symbolBrush=self.purpleMarker,name="temperature")
        self.diastolic_graph = self.plotWdgt.plot(self.bloodPressure[0],pen=self.lightBlue,symbol='o', symbolBrush=self.lightBlueMarker,name="diastolicBP")
        self.systolic_graph = self.plotWdgt.plot(self.bloodPressure[1],pen=self.blue,symbol='o', symbolBrush=self.blueMarker,name="systolicBP")
   
        
        

        self.scene.addWidget(self.plotWdgt)

        self.graphicsView.setScene(self.scene)  
  
        # time.sleep(0.1)
        # self.graphicsView.fitInView(0,0,self.scene.width(),self.scene.height())
        
        # self.initialSolution_figure = plt.figure()
        # self.initialSolution_canvas = FigureCanvas(self.initialSolution_figure)
                
        # # self.initialSolution_figure.clear()
        # ploting = self.initialSolution_figure.add_subplot(111)
        # if len(self.__data):
        #     ploting.scatter(self.__data[:,0], self.__data[:,1],color="k",s=50) 
        #     # print("data")

        # if len(self.__labels):
        #     ploting.scatter(self.__data[:,0], self.__data[:,1],c = self.__labels,s = 50,cmap = 'rainbow')
        #     # print("lbl")
        # if len(self.__centers):
        #     ploting.scatter(self.__centers[:, 0],self.__centers[:, 1],c = "red",s = 100, marker="x",alpha = 1,linewidth=1)
        #     # print("center")
        # self.initialSolution_scene.addWidget(self.initialSolution_canvas)
        # self.initialSolution_graphicsView.setScene(self.initialSolution_scene)   
        # self.initialSolution_graphicsView.fitInView(self.initialSolution_scene.sceneRect())
    
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