# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraphWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.resize(700, 700)
        GraphWindow.setStyleSheet("#GraphWindow\n"
"{\n"
"background-image: url(logo/background.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120);\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(GraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
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
        self.surnameEdit = QtWidgets.QLineEdit(self.centralwidget)
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
        self.tcEdit = QtWidgets.QLineEdit(self.centralwidget)
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
        self.ageEdit = QtWidgets.QLineEdit(self.centralwidget)
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
        self.genderDisplay = QtWidgets.QPushButton(self.centralwidget)
        self.genderDisplay.setStyleSheet("#genderDisplay\n"
"{\n"
"    background-color:  rgb(255,255,255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 120);\n"
"    font: bold 14px;\n"
"    color: black;\n"
"    padding: 6px;\n"
"}")
        self.genderDisplay.setText("")        
        self.genderDisplay.setObjectName("genderDisplay")
        self.horizontalLayout.addWidget(self.genderDisplay)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setStyleSheet("#logout_button\n"
"{\n"
"    background-color:  rgb(255,255,255,100);\n"
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
        self.logout_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("logo/log-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_button.setIcon(icon1)
        self.logout_button.setObjectName("logout_button")
        self.horizontalLayout.addWidget(self.logout_button)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setStyleSheet("#exitButton\n"
"{\n"
"    background-color:  rgb(255,255,255,100);\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("logo/power-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exitButton.setIcon(icon2)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startDateEdit = QtWidgets.QDateEdit(self.centralwidget)
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
"    image: url(logo/down_arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}")
        self.startDateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.startDateEdit.setAccelerated(True)
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setObjectName("startDateEdit")
        self.horizontalLayout_2.addWidget(self.startDateEdit)
        self.endDateEdit = QtWidgets.QDateEdit(self.centralwidget)
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
"    image: url(logo/down_arrow.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}")
        self.endDateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.endDateEdit.setAccelerated(True)
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setObjectName("endDateEdit")
        self.horizontalLayout_2.addWidget(self.endDateEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
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
        self.horizontalLayout_2.addWidget(self.manualEntryButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"\n"
"  border-color: rgb(0, 0, 120);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"  top:-4px; \n"
"bottom:-4px;\n"
"  background-color:  rgb(255,255,255);\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  background-color:  rgb(255,255,255,50);\n"
"  border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"  border-color: rgb(0, 0, 120);\n"
"  margin-bottom: -3px; \n"
"    margin-top: 2px;\n"
"  padding: 6px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background-color:  rgb(50,50,250,50);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    margin-bottom: -3px; \n"
"    font-size:15\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
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
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.graphicsView.setRenderHints(QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
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
        self.tableView.setStyleSheet("QScrollBar::vertical {           \n"
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
"QScrollBar::horizontal {           \n"
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
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.gridLayout_4.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tableTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        GraphWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GraphWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "E-Triyaj Personal"))
        self.nameEdit.setToolTip(_translate("GraphWindow", "Name"))
        self.surnameEdit.setToolTip(_translate("GraphWindow", "Surname"))
        self.tcEdit.setToolTip(_translate("GraphWindow", "TC"))
        self.ageEdit.setToolTip(_translate("GraphWindow", "Age"))
        self.logout_button.setToolTip(_translate("GraphWindow", "Log Out"))
        self.exitButton.setToolTip(_translate("GraphWindow", "Exit"))
        self.startDateEdit.setToolTip(_translate("GraphWindow", "Start Date"))
        self.startDateEdit.setDisplayFormat(_translate("GraphWindow", "dd/MM/yyyy"))
        self.endDateEdit.setToolTip(_translate("GraphWindow", "End Date"))
        self.endDateEdit.setDisplayFormat(_translate("GraphWindow", "d/M/yyyy"))
        self.manualEntryButton.setText(_translate("GraphWindow", "Manual Entry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphTab), _translate("GraphWindow", "Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tableTab), _translate("GraphWindow", "Table"))
