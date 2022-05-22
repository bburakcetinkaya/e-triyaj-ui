# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManualEntryWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# from httpRequests import *
import time


class Ui_manualEntryWindow(object):
    def setupUi(self, manualEntryWindow):
        manualEntryWindow.setObjectName("manualEntryWindow")
        manualEntryWindow.resize(1500, 1000)
        manualEntryWindow.setMinimumSize(QtCore.QSize(0, 0))
        manualEntryWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        manualEntryWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_3 = QtWidgets.QGridLayout(manualEntryWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.manualEntryDiscardButton = QtWidgets.QPushButton(manualEntryWindow)
        self.manualEntryDiscardButton.setStyleSheet("QPushButton {\n"
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
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 150);\n"
"    border-style: inset;\n"
"}")
        self.manualEntryDiscardButton.setObjectName("manualEntryDiscardButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.manualEntryDiscardButton)
        self.manualEntryEnterButton = QtWidgets.QPushButton(manualEntryWindow)
        self.manualEntryEnterButton.clicked.connect(self.onEnterClicked)
        self.manualEntryEnterButton.setStyleSheet("QPushButton {\n"
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
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 150);\n"
"    border-style: inset;\n"
"}")
        self.manualEntryEnterButton.setObjectName("manualEntryEnterButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.manualEntryEnterButton)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)
        # spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        # spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.gridLayout.addItem(spacerItem2, 7, 1, 1, 1)
        # spacerItem3 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.surnameLabel = QtWidgets.QLabel(manualEntryWindow)
        self.surnameLabel.setObjectName("surnameLabel")
        self.gridLayout_2.addWidget(self.surnameLabel, 1, 0, 1, 1)
        self.nameLabel = QtWidgets.QLabel(manualEntryWindow)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout_2.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.temperatureLabel = QtWidgets.QLabel(manualEntryWindow)
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.gridLayout_2.addWidget(self.temperatureLabel, 7, 0, 1, 1)
        self.heartRateLabel = QtWidgets.QLabel(manualEntryWindow)
        self.heartRateLabel.setObjectName("heartRateLabel")
        self.gridLayout_2.addWidget(self.heartRateLabel, 5, 0, 1, 1)
        self.diastBPLabel = QtWidgets.QLabel(manualEntryWindow)
        self.diastBPLabel.setObjectName("diastBPLabel")
        self.gridLayout_2.addWidget(self.diastBPLabel, 8, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(manualEntryWindow)
        self.nameEdit.setStyleSheet("QLineEdit {\n"
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
        self.nameEdit.setObjectName("nameEdit")
        # self.nameEdit.setTabChangesFocus(True)
        self.gridLayout_2.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.genderLabel = QtWidgets.QLabel(manualEntryWindow)
        self.genderLabel.setObjectName("genderLabel")
        self.gridLayout_2.addWidget(self.genderLabel, 4, 0, 1, 1)
        self.spo2Label = QtWidgets.QLabel(manualEntryWindow)
        self.spo2Label.setObjectName("spo2Label")
        self.gridLayout_2.addWidget(self.spo2Label, 6, 0, 1, 1)
        self.ageLabel = QtWidgets.QLabel(manualEntryWindow)
        self.ageLabel.setObjectName("ageLabel")
        self.gridLayout_2.addWidget(self.ageLabel, 3, 0, 1, 1)
        self.tcLabel = QtWidgets.QLabel(manualEntryWindow)
        self.tcLabel.setObjectName("tcLabel")
        self.gridLayout_2.addWidget(self.tcLabel, 2, 0, 1, 1)
        self.sysBPLabel = QtWidgets.QLabel(manualEntryWindow)
        self.sysBPLabel.setObjectName("sysBPLabel")
        self.gridLayout_2.addWidget(self.sysBPLabel, 9, 0, 1, 1)
        self.surnameEdit = QtWidgets.QLineEdit(manualEntryWindow)
        self.surnameEdit.setStyleSheet("QLineEdit {\n"
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
        self.surnameEdit.setObjectName("surnameEdit")
        # self.surnameEdit.setTabChangesFocus(True)
        self.gridLayout_2.addWidget(self.surnameEdit, 1, 1, 1, 1)
        self.tcEdit = QtWidgets.QLineEdit(manualEntryWindow)
        self.tcEdit.setStyleSheet("QLineEdit {\n"
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
        self.tcEdit.setObjectName("tcEdit")
        # self.tcEdit.setTabChangesFocus(True)
        
        self.gridLayout_2.addWidget(self.tcEdit, 2, 1, 1, 1)
        self.ageEdit = QtWidgets.QLineEdit(manualEntryWindow)
        self.ageEdit.setStyleSheet("QLineEdit {\n"
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
        self.ageEdit.setObjectName("ageEdit")
        # self.ageEdit.setTabChangesFocus(True)
        
        self.gridLayout_2.addWidget(self.ageEdit, 3, 1, 1, 1)
        self.genderComboBox = QtWidgets.QComboBox(manualEntryWindow)
        self.genderComboBox.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.genderComboBox.setStyleSheet("QComboBox{\n"
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
"QComboBox::drop-down \n"
"{\n"
"    border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(../logo/down_arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}")
        self.genderComboBox.setIconSize(QtCore.QSize(16, 16))
        self.genderComboBox.setFrame(False)
        self.genderComboBox.setEditable(False)
        self.genderComboBox.setObjectName("genderComboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../logo/male_gender.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genderComboBox.addItem(icon, "")
        self.genderComboBox.addItem("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../logo/female_gender.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genderComboBox.addItem(icon1, "")
        self.gridLayout_2.addWidget(self.genderComboBox, 4, 1, 1, 1)
        
        # self.genderComboBox.setTabChangesFocus(True)
        
        self.heartRateEdit = QtWidgets.QLineEdit(manualEntryWindow)
        self.heartRateEdit.setStyleSheet("QLineEdit {\n"
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
        self.heartRateEdit.setObjectName("heartRateEdit")
        # self.heartRateEdit.setTabChangesFocus(True)
        self.gridLayout_2.addWidget(self.heartRateEdit, 5, 1, 1, 1)
        self.systolicBpEdit = QtWidgets.QLineEdit(manualEntryWindow)
        self.systolicBpEdit.setStyleSheet("QLineEdit {\n"
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
        self.systolicBpEdit.setObjectName("systolicBpEdit")
        # self.systolicBpEdit.setTabChangesFocus(True)
        self.gridLayout_2.addWidget(self.systolicBpEdit, 9, 1, 1, 1)
        self.diastolicBpEdit = QtWidgets.QLineEdit(manualEntryWindow)
        self.diastolicBpEdit.setStyleSheet("QLineEdit {\n"
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
        self.diastolicBpEdit.setObjectName("diastolicBpEdit")
        # self.diastolicBpEdit.setTabChangesFocus(True)
        self.gridLayout_2.addWidget(self.diastolicBpEdit, 8, 1, 1, 1)
        self.temperatureEdit = QtWidgets.QLineEdit(manualEntryWindow)
        # self.temperatureEdit.setTabChangesFocus(True)
        self.temperatureEdit.setStyleSheet("QLineEdit {\n"
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
        self.temperatureEdit.setObjectName("temperatureEdit")
        self.gridLayout_2.addWidget(self.temperatureEdit, 7, 1, 1, 1)
        self.spO2Edit = QtWidgets.QLineEdit(manualEntryWindow)
        # self.spO2Edit.setTabChangesFocus(True)
        self.spO2Edit.setStyleSheet("QLineEdit {\n"
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
        self.spO2Edit.setObjectName("spO2Edit")
        self.gridLayout_2.addWidget(self.spO2Edit, 6, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(manualEntryWindow)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../logo/e-triage_manual_entry_form.png"))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        # spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(manualEntryWindow)
        QtCore.QMetaObject.connectSlotsByName(manualEntryWindow)

    def retranslateUi(self, manualEntryWindow):
        _translate = QtCore.QCoreApplication.translate
        manualEntryWindow.setWindowTitle(_translate("manualEntryWindow", "Manual Entry"))
        self.manualEntryDiscardButton.setText(_translate("manualEntryWindow", "Discard"))
        self.manualEntryEnterButton.setText(_translate("manualEntryWindow", "Enter"))
        self.surnameLabel.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Surname:</span></p></body></html>"))
        self.nameLabel.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Name:</span></p></body></html>"))
        self.temperatureLabel.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Temperature:</span></p></body></html>"))
        self.heartRateLabel.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Heart Rate:</span></p></body></html>"))
        self.diastBPLabel.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Diastolic Blood Pressure:</span></p></body></html>"))
        self.genderLabel.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Gender:</span></p></body></html>"))
        self.spo2Label.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">sp0</span><span style=\" font-size:10pt; vertical-align:sub;\">2</span><span style=\" font-size:10pt;\">:</span></p></body></html>"))
        self.ageLabel.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Age:</span></p></body></html>"))
        self.tcLabel.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">T.C. No:</span></p></body></html>"))
        self.sysBPLabel.setText(_translate("manualEntryWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Systolic Blood Pressure:</span></p></body></html>"))
        self.genderComboBox.setItemText(0, _translate("manualEntryWindow", "MALE"))
        self.genderComboBox.setItemText(1, _translate("manualEntryWindow", "Select"))
        self.genderComboBox.setItemText(2, _translate("manualEntryWindow", "FEMALE"))
    
    def onEnterClicked(self):
        
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
        
        
        # hr = HttpRequest()
        # hr.postEntry(name,surname,age,gender,tc,sp02,heartRate,
        #                     temperature,systolicBP,diastolicBp)
        
        self.close()

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_manualEntryWindow()
ui.setupUi(MainWindow)
# ui.updateTable()
# thread = UpdateTableThread(ui.updateTable,stopFlag)
# thread.start()  
MainWindow.show()      
# app.aboutToQuit.connect(stopFlag.set)


sys.exit(app.exec_())  
