# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setWindowModality(QtCore.Qt.NonModal)
        LoginWindow.resize(822, 637)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        LoginWindow.setFont(font)
        LoginWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setAutoFillBackground(False)
        LoginWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-image: url(logo/login_background.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.loginPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.loginPage)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo/loginLogo_2.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.logo = QtWidgets.QLabel(self.loginPage)
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo/loginLogo.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.loginPage)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
"color: \"green\";\n"
"    font: 8pt \"8514oem\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.id_lineEdit = QtWidgets.QLineEdit(self.loginPage)
        self.id_lineEdit.setStyleSheet("QLineEdit {\n"
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
        self.id_lineEdit.setText("")
        self.id_lineEdit.setObjectName("id_lineEdit")
        self.verticalLayout_2.addWidget(self.id_lineEdit)
        self.password_lineEdit = QtWidgets.QLineEdit(self.loginPage)
        self.password_lineEdit.setStyleSheet("QLineEdit {\n"
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
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.verticalLayout_2.addWidget(self.password_lineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.signUp_Button = QtWidgets.QPushButton(self.loginPage)
        self.signUp_Button.setStyleSheet("QPushButton {\n"
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
        self.signUp_Button.setObjectName("signUp_Button")
        self.horizontalLayout_2.addWidget(self.signUp_Button)
        self.pushButton = QtWidgets.QPushButton(self.loginPage)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.exitButton = QtWidgets.QPushButton(self.loginPage)
        self.exitButton.setStyleSheet("#exitButton\n"
"{\n"
"    background-color:  rgb(255,255,255,50);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120,50);\n"
"    min-width: 1em;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"QPushButton:pressed\n"
" {\n"
"    background-color: rgb(0, 0, 150);\n"
"    border-style: inset;\n"
"}")
        self.exitButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("logo/power-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon1)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_4.addWidget(self.exitButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.loginPage)
        self.newUserPage = QtWidgets.QWidget()
        self.newUserPage.setObjectName("newUserPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.newUserPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.status_label = QtWidgets.QLabel(self.newUserPage)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("#status_label\n"
"{\n"
"    color: \"green\";\n"
"    font: 8pt \"8514oem\";\n"
"}")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.verticalLayout_4.addWidget(self.status_label)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.signUp_Name = QtWidgets.QLineEdit(self.newUserPage)
        self.signUp_Name.setStyleSheet("QLineEdit {\n"
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
        self.signUp_Name.setText("")
        self.signUp_Name.setObjectName("signUp_Name")
        self.horizontalLayout_7.addWidget(self.signUp_Name)
        self.signUp_Surname = QtWidgets.QLineEdit(self.newUserPage)
        self.signUp_Surname.setStyleSheet("QLineEdit {\n"
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
        self.signUp_Surname.setText("")
        self.signUp_Surname.setObjectName("signUp_Surname")
        self.horizontalLayout_7.addWidget(self.signUp_Surname)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.signUp_TC = QtWidgets.QLineEdit(self.newUserPage)
        self.signUp_TC.setStyleSheet("QLineEdit {\n"
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
        self.signUp_TC.setText("")
        self.signUp_TC.setObjectName("signUp_TC")
        self.verticalLayout_4.addWidget(self.signUp_TC)
        self.signUp_password1 = QtWidgets.QLineEdit(self.newUserPage)
        self.signUp_password1.setStyleSheet("QLineEdit {\n"
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
        self.signUp_password1.setObjectName("signUp_password1")
        self.verticalLayout_4.addWidget(self.signUp_password1)
        self.signUp_password2 = QtWidgets.QLineEdit(self.newUserPage)
        self.signUp_password2.setStyleSheet("QLineEdit {\n"
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
        self.signUp_password2.setObjectName("signUp_password2")
        self.verticalLayout_4.addWidget(self.signUp_password2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.signUp_signupButton = QtWidgets.QPushButton(self.newUserPage)
        self.signUp_signupButton.setStyleSheet("QPushButton {\n"
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
        self.signUp_signupButton.setObjectName("signUp_signupButton")
        self.horizontalLayout_5.addWidget(self.signUp_signupButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.exitButton_newUser = QtWidgets.QPushButton(self.newUserPage)
        self.exitButton_newUser.setStyleSheet("#exitButton_newUser\n"
"{\n"
"    background-color:  rgb(0,0,255,10);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120,50);\n"
"    min-width: 1em;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"QPushButton:pressed\n"
" {\n"
"    background-color: rgb(0, 0, 150);\n"
"    border-style: inset;\n"
"}")
        self.exitButton_newUser.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("logo/left_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton_newUser.setIcon(icon2)
        self.exitButton_newUser.setObjectName("exitButton_newUser")
        self.horizontalLayout_6.addWidget(self.exitButton_newUser)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 4)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.newUserPage)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login Window"))
        self.label.setText(_translate("LoginWindow", "Welcome to E-Triage"))
        self.id_lineEdit.setPlaceholderText(_translate("LoginWindow", "User ID"))
        self.password_lineEdit.setPlaceholderText(_translate("LoginWindow", "Password"))
        self.signUp_Button.setText(_translate("LoginWindow", "Sign up"))
        self.pushButton.setText(_translate("LoginWindow", "Login"))
        self.status_label.setText(_translate("LoginWindow", "Welcome to E-Triage"))
        self.signUp_Name.setPlaceholderText(_translate("LoginWindow", "Name:"))
        self.signUp_Surname.setPlaceholderText(_translate("LoginWindow", "Surname"))
        self.signUp_TC.setPlaceholderText(_translate("LoginWindow", "TC number:"))
        self.signUp_password1.setPlaceholderText(_translate("LoginWindow", "Password"))
        self.signUp_password2.setPlaceholderText(_translate("LoginWindow", "Password again"))
        self.signUp_signupButton.setText(_translate("LoginWindow", "Sign up"))
