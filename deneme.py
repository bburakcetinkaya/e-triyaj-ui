
from PyQt5 import QtCore, QtGui, QtWidgets
from thr import *
from MainWindow import *


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.updateTable()
    thread = UpdateTableThread(ui.updateTable,stopFlag)
    thread.start()
    MainWindow.show()      
    app.aboutToQuit.connect(stopFlag.set)
    
    
    sys.exit(app.exec_())  
        
        
        
if __name__ == "__main__":
    main()