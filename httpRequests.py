# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 02:48:00 2022

@author: ASUS
"""

import requests as rq
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
from datetime import datetime
import json
import time

url = "http://192.168.35.90"

class HttpRequest:

    def getEntriesByTc(self,tc):
        try:            
            entries = rq.get(url + '/users/getUserRecordsByTc/'+str(tc)).json()
            # print(entries.url)
            items = pd.DataFrame(entries['items'])
            items.pop('id')
            items.sort_values(by=['time'], ascending=False,inplace=True)
            items.reset_index(drop=True, inplace=True)
            items.columns = map(str.upper, items.columns)             
        except:
            # error_ui = Ui_ErrorWindow()
            # error_ui.setErrorMessage('Could not find')
            # error_ui.setupUi()
            print("could not send request")
            return "error"
        else:
            # print("errordu")
            return items
        
    def getEntriesByDateInterval(self,startDate,endDate):
        try:#http://192.168.1.103/users/startDate/2022-04-30/endDate/2022-04-30
            emptyDict = {}
            entries = rq.get(url +'/users/startDate/' + startDate +'/endDate/' +endDate).json()
            # print(entries.status_code)
            items = pd.DataFrame(entries['items'])
            items.pop('id')
            items.sort_values(by=['time','date'], ascending=[False,False],inplace=True)
            items.reset_index(drop=True, inplace=True)
            items.columns = map(str.upper, items.columns)  
        except:
            # error_ui = Ui_ErrorWindow()
            # error_ui.setErrorMessage('Could not update table')
            # error_ui.setupUi()
            # print(entries)
            print("could not send request")
            return pd.DataFrame(emptyDict)
        else:
            # print(entries)
            print("OK")
            return items  
            
    def getEntriesByDateIntervalAndTc(self,startDate,endDate,tc):
        try:#/users/tc/{tc}/startDate/{startDate}/endDate/{endDate}
            emptyDict = {}
            entries = rq.get(url +'/users/tc/'+ tc+'/startDate/' + startDate +'/endDate/' + endDate).json()
            items = pd.DataFrame(entries['items'])
            items.pop('id')
            items.sort_values(by=['time','date'], ascending=[False,False],inplace=True)
            items.reset_index(drop=True, inplace=True)
            items.columns = map(str.upper, items.columns)  
        except:
            # error_ui = Ui_ErrorWindow()
            # error_ui.setErrorMessage('Could not update table')
            # error_ui.setupUi()
            print("could not send request")
            return pd.DataFrame(emptyDict)
        else:
            print("errordu")
            return items  
        
    def getAllEntries(self):
        try:         
            emptyDict = {}
            entries = rq.get(url +'/users/getAll').json()
            items = pd.DataFrame(entries['items'])
            items.pop('id')
            items.sort_values(by=['time'], ascending=False,inplace=True)
            items.reset_index(drop=True, inplace=True)
            items.columns = map(str.upper, items.columns)  
        except:
            # error_ui = Ui_ErrorWindow()
            # error_ui.setErrorMessage('Could not update table')
            # error_ui.setupUi()
            print("could not send request")
            return pd.DataFrame(emptyDict)
        else:
            print("errordu")
            return items  
        
    def postEntry(self,name,surname,age,gender,tc,sp02,heartRate,
                        temperature,systolicBP,diastolicBP):
        self.postData = {
                          "id": 0,
                          "name": "string",
                          "surname": "string",
                          "age": 0,
                          "gender": "MALE",
                          "tc": 0,
                          "sp02": 0,
                          "heartRate": 0,
                          "temperature": 0,
                          "systolicBP": 0,
                          "diastolicBP": 0,
                          "role": "ROLE_PATIENT",
                          "date": "string",
                          "time": "string"
                        }
        # self.postData["id"] = id
        now = datetime.now()
        self.postData["name"] = name
        self.postData["surname"] = surname
        self.postData["age"] = int(age)
        self.postData["gender"] = gender
        self.postData["tc"] = int(tc)
        self.postData["sp02"] = int(sp02)
        self.postData["heartRate"] = int(heartRate)
        self.postData["temperature"] = float(temperature)
        self.postData["systolicBP"] = int(systolicBP)
        self.postData["diastolicBP"] = int(diastolicBP)
        self.postData["date"] = now.strftime("%Y-%m-%d")
        self.postData["time"] = now.strftime("%H.%M.%S")
        self.jsonPostData = json.dumps(self.postData)

        try:
            x = rq.post(url + '/users/createUser', data = self.jsonPostData) 
            time.sleep(3)      

        except: 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Failed')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Success")
            msg.setInformativeText('Patient record entered successfully.')
            msg.setWindowTitle("Success")
            msg.exec_()
            
        
  