import argparse
from models import User
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


