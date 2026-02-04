# Dades d'exemple amb List 
# Clase User 
class User:
    def __init__(self, id, username, password, email, idrole):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email

# Clase Child
class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

# Clase Tap
class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end

# Clase Status
class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Clase Role
class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

# Clase Treatment
class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name


users = [
    User(id=1, username="mare", password="12345", email="prova@gmail.com", idrole=1),
    User(id=2, username="pare", password="123", email="prova2@gmail.com", idrole=1)
]

# Crear les classes Child, Tap, Role, Status i Treatment

children = [
    Child(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6)
]

taps = [
    Tap(id=1, child_id=1, status_id=1, user_id=1, init="2024-12-18T19:42:43", end="2024-12-18T20:42:43"),
    Tap(id=2, child_id=2, status_id=2, user_id=2, init="2024-12-18T21:42:43", end="2024-12-18T22:42:43")
]

relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 1},
    {"user_id": 1, "child_id": 2, "rol_id": 1},
    {"user_id": 1, "child_id": 1, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 1},
    {"user_id": 2, "child_id": 2, "rol_id": 2}
]

roles = [
    Role(id=1, type_rol='Admin'),
    Role(id=2, type_rol='Tutor Mare Pare'),
    Role(id=3, type_rol='Cuidador'),
    Role(id=4, type_rol='Seguiment')
]

statuses = [
    Status(id=1, name="sleep"),
    Status(id=2, name="awake yes_eyepatch"),
    Status(id=3, name="awake no_eyepatch")
]

treatments = [
    Treatment(id=1, name='Hour'),
    Treatment(id=2, name='percentage')
]
class DAOUser:
    def __init__(self, users_list):
        self.users = users_list

    def listAllUsers(self):
        return self.users

    def addUser(self, user_obj):
        self.users.append(user_obj)

    def searchByEmail(self, email):
        for u in self.users:
            if u.email == email:
                return u
        return None

    def updateUser(self, user_id, new_data):
        user = self.getUserById(user_id)
        if user:
            user.username = new_data.get('username', user.username)
            user.email = new_data.get('email', user.email)
            return True
        return False

    def deleteUser(self, user_id):
        user = self.getUserById(user_id)
        if user:
            self.users.remove(user)
            return True
        return False

    def getUserById(self, user_id):
        for u in self.users:
            if u.id == user_id:
                return u
        return None
    
    def searchByUsernameOrEmail(self, identifier):
        for u in self.users:
            if u.username == identifier or u.email == identifier:
                return u
        return None

class DAOChild:
    def __init__(self, children_list, relation_list):
        self.children = children_list
        self.relations = relation_list

    def listAllChildren(self):
        return self.children

    def getChildrenByUser(self, user_id):
        # Finds IDs of children linked to this user
        child_ids = [r['child_id'] for r in self.relations if r['user_id'] == user_id]
        # Returns the actual child objects
        return [c for c in self.children if c.id in child_ids]

    def addChild(self, child_obj):
        self.children.append(child_obj)

class DAOTap:
    def __init__(self, taps_list):
        self.taps = taps_list

    def listAllTaps(self):
        return self.taps

    def addTap(self, tap_obj):
        self.taps.append(tap_obj)

    def getTapsByChild(self, child_id):
        return [t for t in self.taps if t.child_id == child_id]

from flask import Flask, request, jsonify

app = Flask(__name__)

# Create the DAOs (The Librarians)
dao_user = DAOUser(users)
dao_child = DAOChild(children, relation_user_child)
dao_tap = DAOTap(taps)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Change searchByEmail to this:
    user = dao_user.searchByUsernameOrEmail(data.get('username')) 
    
    if user and user.password == data.get('password'):
        return jsonify({"msg": "Usuari Ok", "coderesponse": "1", "id": user.id, "token": "token12345"}), 200
    return jsonify({"msg": "No validat", "coderesponse": "0"}), 400

@app.route('/child', methods=['POST'])
def get_children_route():
    data = request.get_json()
    # Use the DAO to get the list
    user_kids = dao_child.getChildrenByUser(data.get('iduser'))
    
    # Convert objects to dictionaries so Flask can send them
    return jsonify([k.__dict__ for k in user_kids]), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)