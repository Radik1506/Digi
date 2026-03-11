from DAOUserClient import *
from User import *

class ViewConsole:

    daoClient = DaoUserClient()

    def viewShowMenu(self):
        print("1. Login")
        print("2: Quit")
        while(True):
            option=input("Enter Option: ")
            if (option.isdigit()):
                optionInt=int(option)
                if (optionInt < 3 and optionInt > 0):
                    return optionInt
                else:
                    print("Error, Input a correct option")
    
    def viewGeneral(self):
        option=-1
        while (option != 2):
            option=self.viewShowMenu()
            match option:
                case 1:
                    self.viewLogin()
                case 2:
                    print("Bye")

    def viewLogin(self):
        print("View Login")
        print("Input name or email and password")
        username = input("Username or email: ")
        password = input("Password: ")
        user = User("",username,password,"","","")
        resposta_user = self.daoClient.login(user)

        if resposta_user:
            self.viewUser(resposta_user)
        else:
            self.viewUserNA()
    
    def viewUser(self,user):
        print("User Authenticated")
        print(user)

    def viewUserNA(self):
        print("User not Authenticated")

viewConsole = ViewConsole()
viewConsole.viewGeneral()