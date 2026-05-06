import requests
from User import *
from flask import jsonify

class DaoUserClient:
    base_URL = "http://127.0.0.1:5000"
    token=""

    def login(self, user):
        # Validació paràmetres 
        # TO-DO
        # Petició HTTP al Webservice /login
        URL_peticio= self.base_URL + "/login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }
        response = requests.post(URL_peticio, json=params_POST)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response=user_data_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                user_raw=user_data_raw['data']
                user=User(user_raw['id'], user_raw['username']
                          , "" ,user_raw['email']
                          , "", user_raw['token'])
                self.token=user_raw['token']
                return user
            else: 
                return None
        else:
            return None
    
    def loginToken(self, token):
        URL_peticio= self.base_URL + "/login"
        print(token)
        headers = {'Content-Type': 'application/json', 'api-token': token}
        response = requests.post(URL_peticio,headers=headers) 
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response=user_data_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                user_raw=user_data_raw['data']
                user=User(user_raw['id'], user_raw['username']
                          , "" ,user_raw['email']
                          , "", user_raw['token'])
                return user  
        else:
            return None

    def childToken(self, token):
        URL_peticio= self.base_URL + "/child"
        #print(token)
        headers = {'Content-Type': 'application/json', 'api-token': token}
        response = requests.post(URL_peticio,headers=headers) 
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response=user_data_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                user_raw=user_data_raw['data']
                print("type user_raw child/: ", type(user_raw))
                return user_raw
        else:
            return None
        
    def taps(self, user_id, child_id, token):
        URL_peticio= self.base_URL + "/taps"
        #print(token)
        headers = {'Content-Type': 'application/json', 'api-token': token}
        params_POST = {
            "user_id": int(user_id),
            "child_id": int(child_id)
        }
        response = requests.post(URL_peticio,headers=headers, json=params_POST) 
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            data = response.json()
            return data