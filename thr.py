# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 03:11:48 2022

@author: ASUS
"""
import threading


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
