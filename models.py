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
#1.1
class Message:
    def __init__(self, from_id, to_id, text):
        self._id = -1
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self._creation_date = None
#2.1
    @property
    def id(self):
        return self._id
#2.2
    @property
    def creation_date(self):
        return self._creation_date
#3.1
    @staticmethod
    def load_all_messages(cursor, user_id = None):
        if user_id:
            sql = "SELECT id, from_id, to_id, text, creation_date FROM messages WHERE to_id =%s"
            cursor.execute(sql, (user_id,))
        else:
            sql = "SELECT id, from_id, to_id, text, creation_date FROM messages"
            cursor.execute(sql)
        messages = []
        for row in cursor.fetchall():
            id_, from_id, to_id, text, creation_date = row
            loaded_message = Message(from_id, to_id, text)
            loaded_message._id = id_
            loaded_message._creation_date = creation_date
            messages.append(loaded_message)
        return messages
#4.1
    @staticmethod
    def save_to_db(self, cursor):
        if self._id == -1:
            sql = "INSERT INTO messages (from_id, to_id, text) VALUES (%s, %s, %s) RETURNING id, creation_date"
            values = (self.from_id, self.to_id, self.text)
            cursor.execute(sql, values)
            self._id, self._creation_date = cursor.fetchone()
            return True
#4.2
        else:
            sql = "UPDATE messages SET from_id = %s, to_id = %s, text = %s WHERE id = %s"
            values = (self.from_id, self.to_id, self.text, self._id)
            cursor.execute(sql, values)
            return True



