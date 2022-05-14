# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:11:55 2022

@author: ASUS
"""

from datetime import datetime
from datetime import timedelta

class Helper(object):
    def getDate(self):
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        return current_date
    def getTime(self):
        now = datetime.now()
        current_time = now.strftime("%H.%M.%S")
        return current_time
    def getYesterday(self):
        yesterday = datetime.today() - timedelta(days=1)
        yesterday = yesterday.strftime("%Y-%m-%d")
        return yesterday