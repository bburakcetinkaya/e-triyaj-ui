# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:45:19 2022

@author: piton
"""
from PyQt5 import QtWidgets,QtCore,QtGui
import threading


from GraphWindow import Ui_GraphWindow
import LoginManager
from ManualEntryManager import ManualEntryManager
from thr import UpdateThread

from Helper import Helper
from printTable import PrintTable
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt,QPoint
from httpRequests import HttpRequest

from datetime import datetime
import numpy as np
import pyqtgraph as pg
import pandas as pd

import time



class GraphManager(QtWidgets.QMainWindow,Ui_GraphWindow):
    def __init__(self,doctorID,tc,role="ROLE_ADMIN",thread=False,logOutVisible = False, parent=None):
        super().__init__(parent)
        
        self.setupUi(self)  
        # self.initData()
        self.__tc = tc
        self.__role = role
        self.__doctorID = doctorID
        self.__thread = thread
        self.dataHolderPatient = pd.DataFrame({})
        self.scene = QtWidgets.QGraphicsScene(self) 
        self.plotWdgt = pg.PlotWidget()
        self.setPensBrushes()
        self.initDates()
        self.initData()
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.logout_button.setVisible(logOutVisible)
        
        
        
        
        self.connectSignalsSlots()
    
    def closeEvent(self,event):
        self.stopUpdateThreadFlag.set()
        
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
        
    def setPensBrushes(self):
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
        
    def initData(self):
        if self.__thread:    
            self.stopUpdateThreadFlag = threading.Event()
            self.updateThread = UpdateThread(self.updateInformationByDate,self.stopUpdateThreadFlag,5)
            self.updateThread.start()
        self.updateInformation()
        self.updateInformationByDate() 
        
    def initDates(self):
        helper = Helper()
        self.startDateEdit.setDate(helper.getPreviousNthDay(10,asStr=False))
        self.endDateEdit.setDate(helper.getDate(asStr=False))
        self.endDateEdit.setMinimumDate(self.startDateEdit.date())
        self.startDateEdit.setMaximumDate(self.endDateEdit.date())
        self.endDateEdit.setMaximumDate(datetime.today())
        
    def connectSignalsSlots(self):
        self.manualEntryButton.clicked.connect(self.onManualEntry)
        self.startDateEdit.dateChanged.connect(lambda : {self.updateInformationByDate(),self.stopUpdateThreadFlag.set()})
        self.endDateEdit.dateChanged.connect(lambda : {self.updateInformationByDate(),self.stopUpdateThreadFlag.set()})
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

        if self.gender[0] == "MALE":
            self.ui.genderComboBox.setCurrentIndex(1)    
        if self.gender[0] == "FEMALE":        
            self.ui.genderComboBox.setCurrentIndex(2)
        self.ui.genderComboBox.setEnabled(False)
        self.ui.show()
        
    def printTable(self,data):
        data.pop("NAME")
        data.pop("TC")
        data.pop("SURNAME")
        data.pop("GENDER")
        data.pop("AGE")
        
        toPrint = PrintTable(data)
        self.tableView.setModel(toPrint)
        self.tableView.resizeColumnsToContents()
    
    def updateInformationByDate(self):
        print("Graph Window threading...")
        tc = self.tcEdit.text()
        startDate = self.startDateEdit.date().toString(QtCore.Qt.ISODate)
        endDate = self.endDateEdit.date().toString(QtCore.Qt.ISODate)
        hr = HttpRequest()
        print("role = ",self.__role)
        df = hr.getEntriesByDateIntervalAndTc(startDate,endDate,tc,self.__doctorID,self.__role)
        
        if df.empty :
            print("1")
        elif df.equals(self.dataHolderPatient):
            print("2")
        else:
            print("Data changed...")
            self.dataHolderPatient = pd.concat([df,self.dataHolderPatient]).drop_duplicates().reset_index(drop=True)
            print(self.dataHolderPatient)            
            self.gender = np.array(df["GENDER"])            
            self.printTable(df)
            self.printGraph(df)
        
    def updateInformation(self):
        hr = HttpRequest()        
        tc = self.__tc 
        df = hr.getEntriesByTc(tc,self.__doctorID,self.__role)  
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

    def printGraph(self,df): 
        df2 = df.copy()
        df2 = df2.loc[::-1].reset_index(drop=True).head()
        self.spO2 = np.array(df2["SP02"])
        self.heartRate = np.array(df2["HEARTRATE"])
        self.temperature = np.array(df2[ "TEMPERATURE"])
        self.bloodPressure = [np.array(df2["DIASTOLICBP"]),np.array(df2["SYSTOLICBP"])]
        self.plotWdgt.clear()
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
        # self.graphicsView.fitInView(self.scene.sceneRect,QtCore.Qt.KeepAspectRatio)
    def updateView(self):
       rect = self.scene.sceneRect()
       self.graphicsView.fitInView(rect, QtCore.Qt.IgnoreAspectRatio)

    def showEvent(self, event):
       # ensure that the update only happens when showing the window
       # programmatically, otherwise it also happen when unminimizing the
       # window or changing virtual desktop
       if not event.spontaneous():
           self.updateView()   
    def resizeEvent(self,event):
        # self.graphicsView.fitInView(0,0,self.scene.width(),self.scene.height())
        self.updateView()
        # QtWidgets.QMainWindow.resizeEvent(self, event)
        
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