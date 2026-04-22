import mysql.connector

class ChildDAO:

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
        SELECT * FROM Child
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