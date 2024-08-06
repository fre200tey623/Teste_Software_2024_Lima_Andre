from models import User
from settings import DATABASE

def create_user(name, age):
    user = User(name=name, age=age)
    DATABASE.append(user)
    return user

def get_user(name):
    for user in DATABASE:
        if user.name == name:
            return user
    return None
