from dataclasses import dataclass, asdict
import mysql.connector
import hashlib
from time import time
import random

class UserDAO:
    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="TapatApp"
        )
        return connection

    def login(self, identifier, password):

        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = """
        SELECT * FROM User
        WHERE (username = %s OR email = %s) AND password = %s
        """

        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        token= None
        if user:
            token = self.setTokenUser(user['username'])
            user['token'] = token
        cursor.close()
        con.close() 
        return user

    def setTokenUser(self, username):
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        token = self.getHash()
        print(type(token))
        query = "UPDATE User SET token = '" + token + "' WHERE username = '" + username +"'"
        print(query)
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
        return token

    def getHash(self):
        milliseconds = str(time() * random.randrange(1000))
        data = milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""

