# -*- coding: utf-8 -*-
"""
Created on Mon May 30 03:38:48 2022

@author: piton
"""
from PyQt5 import QtWidgets,QtCore
from ManualEntryWindow import Ui_manualEntryWindow
from httpRequests import HttpRequest

class ManualEntryManager(QtWidgets.QMainWindow,Ui_manualEntryWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
    def connectSignalsSlots(self):
        self.manualEntryEnterButton.clicked.connect(self.onEnterClicked)
        self.manualEntryDiscardButton.clicked.connect(self.onDiscardClicked)
        self.exitButton.clicked.connect(lambda: {self.close()})
            
    def onEnterClicked(self):
        
        name = self.nameEdit.text()
        surname = self.surnameEdit.text()
        age = self.ageEdit.text()
        genderIndex = self.genderComboBox.currentIndex()
        # 0 DEĞERİ DEĞİŞTİRİLECEK
        if genderIndex == 0:
            gender = "MALE"
        if genderIndex == 1:
            gender = "MALE"
        if genderIndex == 2:
            gender = "FEMALE"
       
        tc = self.tcEdit.text()
        sp02 = self.spO2Edit.text()
        heartRate = self.heartRateEdit.text()
        temperature = self.temperatureEdit.text()
        systolicBP = self.systolicBpEdit.text()
        diastolicBp = self.diastolicBpEdit.text()
        
        hr = HttpRequest()
        hr.postEntry(name,surname,age,gender,tc,sp02,heartRate,
                            temperature,systolicBP,diastolicBp)
        
        
        self.close()

    def onDiscardClicked(self):
        self.nameEdit.clear()
        self.surnameEdit.clear()
        self.ageEdit.clear()
        self.genderComboBox.setCurrentIndex(0)
        self.tcEdit.clear()
        self.heartRateEdit.clear()
        self.spO2Edit.clear()
        self.temperatureEdit.clear()
        self.systolicBpEdit.clear()
        self.diastolicBpEdit.clear()