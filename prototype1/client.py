import requests

from prototype1.server import ViewConsole

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
        @staticmethod
        def getInputUsername():
            username = input("Introduce nombre de usuario: ")
            user = dao.getUserByUsername(username)
            return user

    def showUserInfo(username):
        # to-do
        if user is None:
            print("User not found")
        else:
            print("User Found")
            print(f"Username: {user.username}")
            print(f"Name: {user.name}")
            print(f"Email: {user.email}")
            print(f"Role: {user.rol}")

if __name__ == "__main__":
    dao = daoUserClient
    user = ViewConsole.getInputUsername()
    ViewConsole.showUserInfo(user)