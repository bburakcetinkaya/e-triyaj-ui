
from PyQt5 import QtWidgets
import threading
from MainManager import MainManager
      
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    stopFlag = threading.Event()
    window = MainManager(stopFlag)
    window.show()      
    app.aboutToQuit.connect(stopFlag.set)
    
    
    sys.exit(app.exec_())