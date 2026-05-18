from dataclasses import dataclass, asdict
from typing import Any

from flask import Flask, request, jsonify

from serverDAO import ChildDAO, UserDAO

@dataclass
class ApiResponse:
    msg: str
    coderesponse: str
    data: Any = None

userDao = UserDAO()
childDao = ChildDAO()
app = Flask(__name__)


def authenticate_token():
    token = request.headers.get("api-token")
    if not token:
        return None
    return userDao.getUserByToken(token)


@app.route('/login', methods=['POST'])
def login():
    token = request.headers.get("api-token")
    if token:
        user = userDao.getUserByToken(token)
    else:
        data = request.get_json(silent=True) or {}
        identifier = data.get('username')
        password = data.get('password')
        if not identifier or not password:
            response = ApiResponse("Invalid request", "0", None)
            return jsonify(asdict(response)), 400
        user = userDao.login(identifier, password)

    if user:
        response = ApiResponse("Authenticated", "1", user)
        return jsonify(asdict(response)), 200

    response = ApiResponse("Not authenticated", "0", None)
    return jsonify(asdict(response)), 401


@app.route('/child', methods=['POST'])
def child():
    user = authenticate_token()
    if not user:
        response = ApiResponse("Access not granted", "0", None)
        return jsonify(asdict(response)), 401

    childs = childDao.getChilds(user['id'])
    response = ApiResponse("GetChilds", "1", childs)
    return jsonify(asdict(response)), 200


@app.route('/taps', methods=['POST'])
def tap():
    user = authenticate_token()
    if not user:
        response = ApiResponse("Access not granted", "0", None)
        return jsonify(asdict(response)), 401

    data = request.get_json(silent=True) or {}
    child_id = data.get('child_id')
    if child_id is None:
        response = ApiResponse("Missing child_id", "0", None)
        return jsonify(asdict(response)), 400

    taps = childDao.getTapsByIds(user['id'], int(child_id))
    if not taps:
        response = ApiResponse("No taps found", "0", [])
        return jsonify(asdict(response)), 404

    response = ApiResponse("getTaps", "1", taps)
    return jsonify(asdict(response)), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
