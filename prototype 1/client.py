import requests

class User:
    def __init__ (self, username, nom, password, email, rol = "tutor"):
        self.username = username
        self.nom = nom
        self.password = password
        self.email = email
        self.rol = rol

    def __str__ (self):
        return self.nom
    
class daoUserClient:
    def getUserByUsername(self,username):
        response = requests.get("https://localhost:5000/user?username=" + username)
        if response.status_code == 200:
            user_data_raw = response.json()
            if 'msg' in user_data_raw.keys():
                return None
            else:
                user=User(user_data_raw['username'], user_data_raw['nom'], user_data_raw['password'], user_data_raw['email'], user_data_raw['rol'])
                return user
        return None
    
class ViewConsole:
    def getInputUsername():
        # TODO
        return None

    def showUserInfo(username):
        # to-do
        return None


daoUserClient = daoUserClient()

u = daoUserClient.getUserByUsername("rob")
print(u)

u = daoUserClient.getUserByUsername("Not exist")
print(u)