from flask import Flask, request, jsonify
from serverDAO import *
import uuid
from dataclasses import dataclass, asdict

app = Flask(__name__)

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

userDAO = UserDAO()
childDAO = ChildDAO()

@app.route('/login', methods=['POST'])
def login():
    token = request.headers.get("api-token")
    user = None
    if (token):
        user = userDAO.getUserByToken(token)
    else:
        data = request.get_json()
        identifier = data.get('username')
        password = data.get('password')
        user = userDAO.login(identifier, password)

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

@app.route('/child', methods=['POST'])
def child():
    token = request.headers.get("api-token")
    user = None
    if(token):
        user=userDAO.getUserByToken(token)
    if not user:
        response = ApiResponse(
            msg="Access not granted",
            coderesponse="0",
            data=""
        )
        return jsonify(asdict(response)),400

    data = request.get_json()
    childs = childDAO.getChildren(user['id'])
    response = ApiResponse(
        msg="Get Children",
        coderesponse="1",
        data=user
    )

    return jsonify(asdict(response)), 200

if __name__ == '__main__':
    app.run(debug=True)