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
url = "http://localhost:8000"

class HttpRequest(object):
    def __init__(self):

        print()
    def postNewUser(self,tc,name,surname,password,role):
        postData = {
                          "id": 0,
                          "tc": 0,
                          "name": "string",
                          "surname": "string",
                          "role": "ROLE_PATIENT",
                          "password": "string"
                   }
        postData["name"] = str(name)
        postData["surname"] = str(surname)
        postData["tc"] = int(tc)
        postData["password"] = str(password)
        postData["role"] = str(role)
        print(postData)
        jsonPostData = json.dumps(postData)
        status = 0
        try:
            x = rq.post(url + '/users/newUser', data = jsonPostData)
        except:
            status = -1
        else: 
            status = x.status_code
        finally:
            print(status)
            return status
    def requestLogin(self,name,password):
        status = 0
        try:
            x = rq.get(url + '/users/requestLogin/tc/'+str(name)+'/password/'+str(password))
        except: 
            status = -1
        else:
            status = x.status_code
        finally:
            print(status,x)
            return status,x

    def getEntriesByTc(self,tc,doctorID,role):
        print(tc)
        try:            
            entries = rq.get(url + '/users/getUserRecordsByTc/'+str(tc)).json()   
            items = pd.DataFrame(entries['items'])
        except:
           print("could not send request")
           emptyDict = {}
           items = pd.DataFrame(emptyDict)
           
        else:            
           print("OK")
           if role == "ROLE_DOCTOR":
                items = self.controlDataForDoctorOnly(items,doctorID)   
           items.pop('id')
           items.pop('doctorID')
           items.pop('onlyMyDoctor')
           items.sort_values(by=['date','time'], ascending=[False,False],inplace=True)
           items.reset_index(drop=True, inplace=True)            
           items.columns = map(str.upper, items.columns)  
        finally:
           return items
        # finally:
            
        
    def getEntriesByDateInterval(self,startDate,endDate,doctorID,role):

        try:
            entries = rq.get(url +'/users/startDate/' + startDate +'/endDate/' +endDate).json()
            items = pd.DataFrame(entries['items'])
        except:
            emptyDict = {}
            print("could not send request")
            items = pd.DataFrame(emptyDict)
            
        else:            
            print("OK")
            if role == "ROLE_DOCTOR":
                items = self.controlDataForDoctorOnly(items,doctorID)   
            items.pop('id')
            items.pop('doctorID')
            items.pop('onlyMyDoctor')
            items.sort_values(by=['date','time'], ascending=[False,False],inplace=True)
            items.reset_index(drop=True, inplace=True)            
            items.columns = map(str.upper, items.columns)  
        finally:
            return items
            
    def getEntriesByDateIntervalAndTc(self,startDate,endDate,tc,doctorID,role):
        

        try:         
            entries = rq.get(url +'/users/tc/'+ tc+'/startDate/' + startDate +'/endDate/' + endDate).json()
            items = pd.DataFrame(entries['items'])
            
        except:
            emptyDict = {}
            print("could not send request")
            items = pd.DataFrame(emptyDict)
            
        else:
            print("OK")
            if role == "ROLE_DOCTOR":
                items = self.controlDataForDoctorOnly(items,doctorID)  
            items.pop('id')
            items.pop('doctorID')
            items.pop('onlyMyDoctor')
            items.sort_values(by=['date','time'], ascending=[False,False],inplace=True)
            items.reset_index(drop=True, inplace=True)            
            items.columns = map(str.upper, items.columns)   
        finally:
            return items
        
    # def getAllEntries(self):
    #         emptyDict = {}
    #     try:    
            
    #         entries = rq.get(url +'/users/getAll').json()
    #         items = pd.DataFrame(entries['items'])
    #         items.pop('id')
    #         items.sort_values(by=['time'], ascending=False,inplace=True)
    #         items.reset_index(drop=True, inplace=True)
    #         items.columns = map(str.upper, items.columns)  
    #     except:
    #         # error_ui = Ui_ErrorWindow()
    #         # error_ui.setErrorMessage('Could not update table')
    #         # error_ui.setupUi()
    #         print("could not send request")
    #         return pd.DataFrame(emptyDict)
    #     else:
    #         print("errordu")
    #         return items  
        
    def postEntry(self,name,surname,age,gender,tc,sp02,heartRate,
                        temperature,systolicBP,diastolicBP,doctorID,onlyMyDoctor):
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
                          "doctorID": 0,
                          "onlyMyDoctor": "TRUE",
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
        self.postData["doctorID"] = int(doctorID)
        self.postData["onlyMyDoctor"] = str(onlyMyDoctor)
        self.postData["date"] = now.strftime("%Y-%m-%d")
        self.postData["time"] = now.strftime("%H.%M.%S")
        self.jsonPostData = json.dumps(self.postData)

        try:
            x = rq.post(url + '/users/createUser', data = self.jsonPostData)
            
            # time.sleep(3)      

        except: 
           print(00)
        else:
           print(0)
        # finally:
            # stopFlag.clear()

        
    def controlDataForDoctorOnly(self,data,doctorID):
        for i in range(0,len(data)-1):            
            controldata = data.loc[i]
            if (controldata["onlyMyDoctor"] == "TRUE") and (controldata["doctorID"] != doctorID):
                    data.drop([i],axis=0,inplace=True)     
        data.reset_index(drop=True, inplace=True)
        return data
            
        
  