
from PyQt5 import QtWidgets,QtCore
import LoginManager
      
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("QtCurve")
    if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    window = LoginManager.LoginManager()
    window.show() 
    
    
    sys.exit(app.exec_())