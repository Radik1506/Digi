from flask import Flask, jsonify, request

app = Flask(__name__)

class User:
    def __init__(self,username, nom, password, email, rol):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol
us1=User(username="aa", nom = "Test Test", password = "1234", email = "wqd@gm@com", rol = "Role")
print(us1.rol)


@app.route('/user/', methods=['GET'])
def user():
    resposta = ""
    print("AAAAAAAAAAA")
    username = request.args.get("Username",default="")
    if username != "":
        resposta = "username=", username
    else:
        resposta = "No username format"
    return "test"

if __name__ == '__main__':
    app.run(debug=True)