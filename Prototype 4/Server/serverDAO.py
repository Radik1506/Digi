import hashlib
import random
from time import time

import mysql.connector


class ChildDAO:
    def connectBBDD(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="TapatApp"
        )

    def getChilds(self, id_user):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = (
            "SELECT DISTINCT Child.* "
            "FROM RelationUserChild "
            "JOIN Child ON RelationUserChild.child_id = Child.id "
            "WHERE RelationUserChild.user_id = %s"
        )
        cursor.execute(query, (id_user,))
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return results

    def getTapsByIds(self, id_user, id_child):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM Tap WHERE child_id = %s AND user_id = %s"
        cursor.execute(query, (id_child, id_user))
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return results


class UserDAO:
    def connectBBDD(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="TapatApp"
        )

    def getUserByToken(self, token):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE token = %s"
        cursor.execute(query, (token,))
        user = cursor.fetchone()
        cursor.close()
        con.close()
        return user

    def login(self, identifier, password):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = (
            "SELECT * FROM User "
            "WHERE (username = %s OR email = %s) AND password = %s"
        )
        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        if user:
            token = self.setTokenUser(user['username'])
            user['token'] = token
        cursor.close()
        con.close()
        return user

    def setTokenUser(self, username):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        token = self.getHash()
        query = "UPDATE User SET token = %s WHERE username = %s"
        cursor.execute(query, (token, username))
        con.commit()
        cursor.close()
        con.close()
        return token

    def getHash(self):
        milliseconds = str(time() * random.randrange(1000))
        hash_object = hashlib.sha256(milliseconds.encode('utf-8'))
        return hash_object.hexdigest()
