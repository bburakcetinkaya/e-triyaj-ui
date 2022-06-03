# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:11:55 2022

@author: ASUS
"""

from datetime import datetime
from datetime import timedelta

class Helper(object):
    def getDate(self,asStr = True):
        date = datetime.now()
        if asStr:
            current_date_str = date.strftime("%Y-%m-%d")
            return current_date_str
        else:
            return date.date()
            print(date)
    def getTime(self,asStr = True):
        time = datetime.now()
        if asStr:
            current_time_str = time.strftime("%H.%M.%S")
            return current_time_str
        else:
            return time.time()
    def getPreviousNthDay(self,n,asStr = True):
        previous = datetime.today() - timedelta(days=n)
        if asStr:
            previous_str = previous.strftime("%Y-%m-%d")
            return previous_str
        else:
            return previous.date()
            print(previous.date())
        