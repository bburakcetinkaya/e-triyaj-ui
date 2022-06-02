
from PyQt5 import QtWidgets,QtCore
import threading
# from MainManager import MainManager
from LoginManager import LoginManager
      
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("QtCurve")
    if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    stopFlag = threading.Event()
    window = LoginManager()
    window.show()      
    app.aboutToQuit.connect(stopFlag.set)
    
    
    sys.exit(app.exec_())