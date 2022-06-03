# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 03:11:48 2022

@author: ASUS
"""
import threading


class UpdateThread(threading.Thread):
    def __init__(self,target,event,secs):
        threading.Thread.__init__(self)
        self.__secs = secs
        self.__target = target
        self.__stopped = event
        # self.run()

    def run(self):
        while not self.__stopped.wait(self.__secs):
            self.__target()
            
# class UpdateThread1Sc(threading.Thread):
#     def __init__(self,target,event):
#         threading.Thread.__init__(self)
#         self._target = target
#         self._stopped = event
#         # self.run()

#     def run(self):
#         while not self._stopped.wait(1):
#             self._target()
