from flask import Flask, request, jsonify
from userDAO import *
import uuid
from dataclasses import dataclass, asdict

app = Flask(__name__)

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

userDAO = UserDAO()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    identifier = data.get('username')
    password = data.get('password')
    user = userDAO.login(identifier, password)
    response = ApiResponse(
        msg="login",
        coderesponse="-1",
        data=user
    )
    if user:
        response = ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=user
        )
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=""
        )
    return jsonify(asdict(response)),200

@app.route('/getchild', methods=['POST'])
def getChild():
    data = request.get_json()
    identifier = data.get('username')
    password = data.get('password')
    user = userDAO.login(identifier, password)
    response = ApiResponse(
        msg="login",
        coderesponse="-1",
        data=user
    )
    if user:
        response = ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=user
        )
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=""
        )
    return jsonify(asdict(response)),200

if __name__ == '__main__':
    app.run(debug=True)