import requests

from User import User


class DaoUserClient:
    base_URL = "http://127.0.0.1:5000"
    token = ""

    def login(self, user):
        URL_peticio = self.base_URL + "/login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }
        response = requests.post(URL_peticio, json=params_POST)
        if response.status_code == 200:
            user_data_raw = response.json()
            if user_data_raw.get('coderesponse') == '1':
                user_raw = user_data_raw['data']
                user = User(
                    user_raw.get('id'),
                    user_raw.get('username'),
                    "",
                    user_raw.get('email'),
                    None,
                    user_raw.get('token')
                )
                self.token = user_raw.get('token', "")
                return user
        return None

    def loginToken(self, token):
        URL_peticio = self.base_URL + "/login"
        headers = {'Content-Type': 'application/json', 'api-token': token}
        response = requests.post(URL_peticio, headers=headers)
        if response.status_code == 200:
            user_data_raw = response.json()
            if user_data_raw.get('coderesponse') == '1':
                user_raw = user_data_raw['data']
                return User(
                    user_raw.get('id'),
                    user_raw.get('username'),
                    "",
                    user_raw.get('email'),
                    None,
                    user_raw.get('token')
                )
        return None

    def childToken(self, token):
        URL_peticio = self.base_URL + "/child"
        headers = {'Content-Type': 'application/json', 'api-token': token}
        response = requests.post(URL_peticio, headers=headers)
        if response.status_code == 200:
            user_data_raw = response.json()
            if user_data_raw.get('coderesponse') == '1':
                return user_data_raw.get('data')
        return None

    def taps(self, token, child_id):
        URL_peticio = self.base_URL + "/taps"
        headers = {'Content-Type': 'application/json', 'api-token': token}
        params_POST = {"child_id": int(child_id)}
        response = requests.post(URL_peticio, headers=headers, json=params_POST)
        try:
            return response.json()
        except ValueError:
            return {
                'coderesponse': '0',
                'msg': 'Invalid response from server',
                'data': None
            }
