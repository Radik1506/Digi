from dadesServer import *
from dataclasses import dataclass, asdict
from flask import jsonify

class UserDao:
    def getAllUsers(self):
        return [u.__dict__ for u in users]

    def getUserById(self, id):
        for u in users:
            if u.id == id:
                return u.__dict__
        return None

    def addUser(self, user):
        users.append(user)
        return user.__dict__
    
    def getUserByUsername(self, username):
        for user in users:
            if user.username == username or user.email == username:
                return user
        return None
    
    def login(self, username, password):
        for u in users:
            if u.username == username and u.password == password:
                return u
        return None
    
    def getUserByToken(self, token):
        for u in users:
            if hasattr(u, "token") and u.token == token:
                return u
        return None
    
class ChildDao:

    def getAllChildren(self):
        return [c.__dict__ for c in children]

    def getChildrenByUser(self, user_id):
        child_ids = [r["child_id"] for r in relation_user_child if r["user_id"] == user_id]
        return [c.__dict__ for c in children if c.id in child_ids]



class TapDao:

    def getTapsByChild(self, child_id):
        return [t.__dict__ for t in taps if t.child_id == child_id]



class StatusDao:

    def getAllStatus(self):
        return [s.__dict__ for s in statuses]



class RoleDao:

    def getAllRoles(self):
        return [r.__dict__ for r in roles]



class TreatmentDao:

    def getAllTreatments(self):
        return [t.__dict__ for t in treatments]