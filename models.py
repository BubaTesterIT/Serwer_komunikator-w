from models import User
from clcrypto import hash_password
#1
class User:
    def __init__(self, username="", password="", salt=""):
        self._id = -1,
        self.username = username,
        self._hashed_password = hash_password(password, salt),
#2
    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password
#3
    def new_password(self, password, salt=""):
        self._hashed_password = hash_password(password, salt)

    @hashed_password.setter
    def hashed_password(self, password):
        self.new_password(password)
#4
    def save_to_db(self, cursor):
        if self._id == -1:
            sql = "INSERT INTO users (username, hashed_password) VALUES (%s, %s)RETURNING id"
            values = (self.username, self._hashed_password)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]
            return True
#5
        else:
            sql = "UPDATE users SET username= %s, hashed_password = %s WHERE id = %s"
            values = (self.username, self._hashed_password, self._id)
            cursor.execute(sql, values)
            return True
#4.1
    @staticmethod
    def load_user_by_id(id_, cursor):
        sql = "SELECT id, username, hashed_password FROM users WHERE cursor.execute(sql,( id))"
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = loaded_user.id
            loaded_user.hashed_password = hashed_password
            return loaded_user
        else:
            return None
#4.2
    @staticmethod
    def load_all_users(username, cursor):
        sql = "SELECT id, username, hashed_password FROM users WHERE Users"
        users = []
        for row in cursor.fetchall():
            id_, username, hashed_password = row
            loaded_user = User()
            loaded_user._id = loaded_user.id
            loaded_user.username = username
            loaded_user.hashed_password = hashed_password
            users.append(loaded_user)
        return users
#6
    def delete_from_db(self, cursor):
        sql = "DELETE FROM users WHERE id = %s"
        values = (self._id,)
        cursor.execute(sql, values)
        self._id = -1
        return True



