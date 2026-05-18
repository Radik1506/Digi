from DAOUserClient import DaoUserClient
from User import User


class ViewConsole:
    def __init__(self):
        self.daoClient = DaoUserClient()
        self.token = ""

    def viewShowMenu(self):
        print("1: Login")
        print("2: Login Token")
        print("3: Child")
        print("4: Taps")
        print("5: Quit")

        while True:
            option = input("Enter Option: ")
            if not option.isdigit():
                print("error, enter a number")
                continue

            optionInt = int(option)
            if 1 <= optionInt <= 5:
                return optionInt

            print("Error: Introdueix una opció correcta")

    def viewGeneral(self):
        while True:
            option = self.viewShowMenu()
            if option == 1:
                self.viewLogin()
            elif option == 2:
                self.viewLoginToken(self.token)
            elif option == 3:
                self.viewChilds(self.token)
            elif option == 4:
                childId = input("Enter Child Id: ")
                self.viewTaps(self.token, childId)
            elif option == 5:
                print("Adeu, Gràcies per utilitzar l'aplicació")
                break
            else:
                print("Error")

    def viewChilds(self, token):
        print("View Childs")
        resposta_child = self.daoClient.childToken(token)
        if resposta_child:
            print(resposta_child)
        else:
            print("No child data available")

    def viewLoginToken(self, token):
        print("View LOGIN TOKEN")
        resposta_user = self.daoClient.loginToken(token)
        if resposta_user:
            self.viewUser(resposta_user)
            self.token = resposta_user.token
        else:
            self.viewUserNotAuthenticated()

    def viewLogin(self):
        print("View LOGIN")
        print("Introdueix el Username o email i el password")
        username = input("Username o email: ")
        passwd = input("Password: ")
        user = User(None, username, passwd, None, None, None)
        resposta_user = self.daoClient.login(user)
        if resposta_user:
            self.viewUser(resposta_user)
            self.token = resposta_user.token
        else:
            self.viewUserNotAuthenticated()

    def viewUser(self, user):
        print("View User Authenticated")
        print(user)

    def viewUserNotAuthenticated(self):
        print("View User")
        print("User NOT Authenticated")

    def viewTaps(self, token, child_id):
        if not child_id.isdigit():
            print("Child Id must be a number")
            return
        print(self.daoClient.taps(token, child_id))


if __name__ == '__main__':
    viewConsole = ViewConsole()
    viewConsole.viewGeneral()
