# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManualEntryWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from httpRequests import *
# from thr import *
import time

class Ui_manualEntryWindow(object):
    def setupUi(self, manualEntryWindow):
        manualEntryWindow.setObjectName("manualEntryWindow")
        manualEntryWindow.resize(454, 468)
        manualEntryWindow.setMinimumSize(QtCore.QSize(454, 468))
        manualEntryWindow.setMaximumSize(QtCore.QSize(454, 468))
        self.frame = QtWidgets.QFrame(manualEntryWindow)
        self.frame.setGeometry(QtCore.QRect(10, 10, 431, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 381, 20))
        self.label_11.setObjectName("label_11")
        self.manualEntryEnterButton = QtWidgets.QPushButton(self.frame)
        self.manualEntryEnterButton.setGeometry(QtCore.QRect(300, 417, 75, 23))
        self.manualEntryEnterButton.setObjectName("manualEntryEnterButton")
        self.manualEntryEnterButton.clicked.connect(self.onEnterClicked)
        self.manualEntryDiscardButton = QtWidgets.QPushButton(self.frame)
        self.manualEntryDiscardButton.setGeometry(QtCore.QRect(210, 417, 75, 23))
        self.manualEntryDiscardButton.setObjectName("manualEntryDiscardButton")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 40, 361, 370))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(-1, 4, -1, -1)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
        self.manualEntryVLayout = QtWidgets.QVBoxLayout()
        self.manualEntryVLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.manualEntryVLayout.setContentsMargins(-1, 4, -1, -1)
        self.manualEntryVLayout.setSpacing(7)
        self.manualEntryVLayout.setObjectName("manualEntryVLayout")
        self.nameEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.nameEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.nameEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.nameEdit.setObjectName("nameEdit")
        self.nameEdit.setTabChangesFocus(True)        
        self.manualEntryVLayout.addWidget(self.nameEdit)
        
        self.surnameEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.surnameEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.surnameEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.surnameEdit.setObjectName("surnameEdit")
        self.surnameEdit.setTabChangesFocus(True)
        self.manualEntryVLayout.addWidget(self.surnameEdit)
        
        self.tcEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.tcEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.tcEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.tcEdit.setObjectName("tcEdit") 
        self.tcEdit.setTabChangesFocus(True)
        self.manualEntryVLayout.addWidget(self.tcEdit)
        
        self.ageEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.ageEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.ageEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.ageEdit.setObjectName("ageEdit")
        self.ageEdit.setTabChangesFocus(True)
        self.manualEntryVLayout.addWidget(self.ageEdit)
        
        self.genderComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.genderComboBox.setMinimumSize(QtCore.QSize(200, 30))
        self.genderComboBox.setMaximumSize(QtCore.QSize(200, 30))
        self.genderComboBox.setEditable(False)
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.manualEntryVLayout.addWidget(self.genderComboBox)
        
        self.spO2Edit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.spO2Edit.setMinimumSize(QtCore.QSize(200, 30))
        self.spO2Edit.setMaximumSize(QtCore.QSize(200, 30))
        self.spO2Edit.setObjectName("spO2Edit")
        self.spO2Edit.setTabChangesFocus(True)
        self.manualEntryVLayout.addWidget(self.spO2Edit)
        
        self.heartRateEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.heartRateEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.heartRateEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.heartRateEdit.setObjectName("heartRateEdit")
        self.heartRateEdit.setTabChangesFocus(True)
        self.manualEntryVLayout.addWidget(self.heartRateEdit)
        
        self.temperatureEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.temperatureEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.temperatureEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.temperatureEdit.setObjectName("temperatureEdit")
        self.temperatureEdit.setTabChangesFocus(True)
        self.manualEntryVLayout.addWidget(self.temperatureEdit)
        
        self.systolicBpEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.systolicBpEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.systolicBpEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.systolicBpEdit.setObjectName("systolicBpEdit")
        self.systolicBpEdit.setTabChangesFocus(True)
        self.manualEntryVLayout.addWidget(self.systolicBpEdit)
        
        self.diastolicBpEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.diastolicBpEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.diastolicBpEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.diastolicBpEdit.setObjectName("diastolicBpEdit")
        self.diastolicBpEdit.setTabChangesFocus(True)
        self.manualEntryVLayout.addWidget(self.diastolicBpEdit)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.manualEntryVLayout)

        self.retranslateUi(manualEntryWindow)
        QtCore.QMetaObject.connectSlotsByName(manualEntryWindow)

    def retranslateUi(self, manualEntryWindow):
        _translate = QtCore.QCoreApplication.translate
        manualEntryWindow.setWindowTitle(_translate("manualEntryWindow", "Manual Entry"))
        self.label_11.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Manual Entry Form</span></p></body></html>"))
        self.manualEntryEnterButton.setText(_translate("manualEntryWindow", "Enter"))
        self.manualEntryDiscardButton.setText(_translate("manualEntryWindow", "Discard"))
        self.label.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Name:</span></p></body></html>"))
        self.label_2.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Surname:</span></p></body></html>"))
        self.label_3.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">T.C. No:</span></p></body></html>"))
        self.label_4.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Age:</span></p></body></html>"))
        self.label_5.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Gender:</span></p></body></html>"))
        self.label_6.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">sp0</span><span style=\" font-size:10pt; vertical-align:sub;\">2</span><span style=\" font-size:10pt;\">:</span></p></body></html>"))
        self.label_7.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Heart Rate:</span></p></body></html>"))
        self.label_10.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Temperature:</span></p></body></html>"))
        self.label_9.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Diastolic Blood Pressure:</span></p></body></html>"))
        self.label_8.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Systolic Blood Pressure:</span></p></body></html>"))
        self.nameEdit.setHtml(_translate("manualEntryWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.surnameEdit.setHtml(_translate("manualEntryWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.genderComboBox.setItemText(0, _translate("manualEntryWindow", "Select"))
        self.genderComboBox.setItemText(1, _translate("manualEntryWindow", "Male"))
        self.genderComboBox.setItemText(2, _translate("manualEntryWindow", "Female"))
        
    def onEnterClicked(self):
        
        # stopFlag.set()
        # UpdateTableThread.join()
        # thread = UpdateTableThread(ui.updateTable,stopFlag = True)
        # print("manual start ",stopFlag)
        name = self.nameEdit.toPlainText()
        surname = self.surnameEdit.toPlainText()
        age = self.ageEdit.toPlainText()
        genderIndex = self.genderComboBox.currentIndex()
        # 0 DEĞERİ DEĞİŞTİRİLECEK
        if genderIndex == 0:
            gender = "MALE"
        if genderIndex == 1:
            gender = "MALE"
        if genderIndex == 2:
            gender = "FEMALE"
            
       
        tc = self.tcEdit.toPlainText()
        sp02 = self.spO2Edit.toPlainText()
        heartRate = self.heartRateEdit.toPlainText()
        temperature = self.temperatureEdit.toPlainText()
        systolicBP = self.systolicBpEdit.toPlainText()
        diastolicBp = self.diastolicBpEdit.toPlainText()
        
        
        hr = HttpRequest()
        hr.postEntry(name,surname,age,gender,tc,sp02,heartRate,
                            temperature,systolicBP,diastolicBp)
        
        
        # stopFlag.clear()
        # UpdateTableThread.join()
        # thread._stopped = true
        # print("manual end",stopFlag)
        self.close()
        
        
        # QtCore.QCoreApplication.instance().quit()

        
        
        
        
        
        
        
        
        
        
        
        
        
