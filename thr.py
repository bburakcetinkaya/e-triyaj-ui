# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 03:11:48 2022

@author: ASUS
"""
import threading
stopFlag = threading.Event()
# from httpRequests import *
# from Helper import *
# from MainWindow import *
# from printTable import *


class UpdateTableThread(threading.Thread):
    def __init__(self,target,event):
        threading.Thread.__init__(self)
        self._target = target
        self._stopped = event

    def run(self):
        while not self._stopped.wait(5):
            self._target()
            
class UpdateTimeThread(threading.Thread):
    def __init__(self,target,event):
        threading.Thread.__init__(self)
        self._target = target
        self._stopped = event

    def run(self):
        while not self._stopped.wait(60):
            self._target()
    # def stop(self):
    #     self._stopped = event.set()
            
            # helper = Helper()
            # hr = HttpRequest()
            # data = hr.getEntriesByDateInterval(helper.getDate(),helper.getDate())
            # if data.empty:
            #     return
            # ui = Ui_MainWindow()
            # ui.updateTable(data)
            # hlpr = Helper()
            # hr = HttpRequest()
            # hr.getEntriesByDateInterval(hlpr.getDate(),hlpr.getDate())
            # call a function