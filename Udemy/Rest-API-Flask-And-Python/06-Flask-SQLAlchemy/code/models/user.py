import sqlite3

class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod #use the current class instead of hardcoding the classname
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,)) # passing in username to the query, comma defines a tuple
        row = result.fetchone()

        if row:
            user = cls(*row) #id, username, password, could also pass row[0], row[1], row[2]
        else:
            user = None

        connection.close()
        return user

    @classmethod #use the current class instead of hardcoding the classname
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,)) # passing in username to the query, comma defines a tuple
        row = result.fetchone()

        if row:
            user = cls(*row) #id, username, password, could also pass row[0], row[1], row[2]
        else:
            user = None

        connection.close()
        return user