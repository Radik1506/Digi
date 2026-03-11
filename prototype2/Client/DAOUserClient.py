import requests
from client import *
from flask import jsonify
from User import *



class DaoUserClient:
    base_url = "http://localhost:5000"

    def login (self, user):
        url_petition = self.base_url + "/login"
        params_post = {
            "username": user.username,
            "password": user.password
        }
        response = requests.post(url_petition, json=params_post)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response = user_data_raw['coderesponse']
            if code_response == '0':
                return None
            else:
                user = User(user_data_raw['id'], user_data_raw['username'], "", user_data_raw['email'], user_data_raw['idrole'], user_data_raw['token'])
                return user
        else:
            return None

'''daoClient=DaoUserClient()
user=User("", "mare", "12345", "", "", "")
resposta=daoClient.login(user)
print(resposta)'''