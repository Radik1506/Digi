from User import *
from DAOUserClient import *

class ViewConsole:

    daoClient=DaoUserClient()
    token=""
   
    def viewShowMenu(self):
        print("1: Login")
        print("2: Login Token")
        print("3: Child")
        print("4. Taps")
        print("5: Quit")
        while(True):
            option=input("Enter Option: ")
            if not option.isdigit:
                print("error, enter a number")
            if option.isdigit:
                optionInt=int(option)
                if(optionInt >0 and optionInt <6):
                    return optionInt
            
            print("Error: Introdueix una opció correcta")

        
    def viewGeneral(self):
        option=-1
        while(True):
            option=self.viewShowMenu()
            match option:
                case 1:
                    #login
                    self.viewLogin()
                case 2:
                    #login Token
                    self.viewLoginToken(self.token)
                case 3:
                    #Childs
                    print("View Childs")
                    self.viewChilds(self.token)
                    #self.viewLogin()
                case 4:
                    #Childs
                    print("View taps")
                    userId = input("Enter User Id: ")
                    childId = input("Enter Child Id: ")
                    self.viewTaps(self.token, childId)
                    #self.viewLogin()
                case 5:
                    # Quit
                    exit()
                    print("Adeu, Gràcies per utilitzar l'aplicació")
                case _:
                    print("Error")


    def viewChilds(self, token):
        print("View Childs")
        resposta_child=self.daoClient.childToken(token)
        if(resposta_child):
            print(resposta_child)              
        

    def viewLoginToken(self, token):
        print("View LOGIN TOKEN")
        resposta_user=self.daoClient.loginToken(token)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()

    def viewLogin(self):
        print("View LOGIN")
        print("Introdueix el Username o email i el password")
        username=input("Username o email: ")
        passwd=input("Password: ")
        user=User("", username, passwd, "", "", "")
        resposta_user=self.daoClient.login(user)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()
    
    def viewUser(self,user):
        print("View User Authenticated")
        print(user)
    
    def viewUserNotAutenticated(self):
        print("View User")
        print("User NOT Authenticated")

    def viewTaps(self, token, child_id):
        print(self.daoClient.taps(token, child_id))


viewConsole=ViewConsole()

viewConsole.viewGeneral()