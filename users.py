import argparse

from psycopg2 import connect, OperationalError
from psycopg2.errorcodes import UNIQUE_VIOLATION

from models import User

from clcrypto import check_password


parser = argparse.ArgumentParser()

parser.add_argument("-u", "--username", help="Username")
parser.add_argument("-p", "--password", help="Password, (min 8 characters)")
parser.add_argument("-n", "--new_password", help="New Password, (min 8 characters)")
parser.add_argument("-l", "--list", help="List", action="store_true")
parser.add_argument("-d", "--delete", help="Delete", action="store_true")
parser.add_argument("-e", "--edit", help="Edit", action="store_true")
args = parser.parse_args()


def list_users(cursor):
    users = User.load_all_users(cursor)
    for user in users:
        print(user.username)

def create_user(cursor, username, password):

    if len(password) < 8:
        print("Password must be at least 8 characters")
    else:
        try:
            user = User(username=username, password=password)
            user.save_to_db()
            print("User created successfully")
        except UNIQUE_VIOLATION as e:
            print("User is already created.",e)

def delete_user(cursor, username, password):
    user = User.load_user_by_username(cursor, username)
    if not user:
        print("User not found")
    elif check_password(password, user.hashed_password):
        user.delete(cursor)
        print("User deleted successfully")
    else:
        print("Password does not match")

def edit_user(cursor, username, password, new_password):
    user = User.load_user_by_username(cursor, username)
    if not user:
        print("User not found")
    elif check_password(password, user.hashed_password):
        if len(new_password) < 8:
            print("Password must be at least 8 characters")
        else:
            user.hashed_password = new_password
            user.save_to_db(cursor)
            print("User edited successfully")
    else:
        print("Password does not match")

if __name__ == "__main__":
    try:
        cnx = connect(database="workshop", user="postgres", password="postgres", host="coderslab", port=5432)
        cnx.autocommit = True
        cursor = cnx.cursor()
        if args.username and args.password and args.edit and args.new_pass:
            edit_user(cursor, args.username, args.password, args.new_pass)
        elif args.username and args.password and args.delete:
            delete_user(cursor, args.username, args.password)
        elif args.username and args.password:
            create_user(cursor, args.username, args.password)
        elif args.list:
            list_users(cursor)
        else:
            parser.print_help()
        cnx.close()
    except OperationalError as err:

        print("Connection Error: ", err)


