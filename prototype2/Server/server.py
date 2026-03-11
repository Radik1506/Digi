from flask import Flask, request, jsonify
from dadesServer import *
from DAOServer import *
import uuid

app = Flask(__name__)

user_dao = UserDao()
child_dao = ChildDao()
tap_dao = TapDao()
status_dao = StatusDao()
role_dao = RoleDao()
treatment_dao = TreatmentDao()

@app.route('/login', methods=['POST'])
def login():

    token_header = request.headers.get("Authorization")

    if token_header:
        user = user_dao.getUserByToken(token_header)

        if user:
            return jsonify({
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "email": user.email,
                "token": user.token,
                "idrole": user.idrole,
                "msg": "Usuari Ok",
                "coderesponse": "1"
            }), 200

        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400


    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    user = user_dao.login(username, password)

    if user:
        user.token = str(uuid.uuid4())

        return jsonify({
            "id": user.id,
            "username": user.username,
            "password": user.password,
            "email": user.email,
            "token": user.token,
            "idrole": user.idrole,
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200

    return jsonify({
        "coderesponse": "0",
        "msg": "No validat"
    }), 400


@app.route('/child', methods=['POST'])
def get_child():
    data = request.get_json()
    iduser = data.get("iduser")

    if not iduser:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    childs = child_dao.getChildrenByUser(iduser)

    return jsonify({
        "msg": str(len(childs)),
        "coderesponse": "1",
        "children": childs
    }), 200

if __name__ == '__main__':
    app.run(debug=True)