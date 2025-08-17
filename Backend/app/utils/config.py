from models.user_model import User

def create_user(name,email,password,age=None):
    newuser = User()
    newuser.name = name
    if age is not None:
        newuser.age = age
    newuser.email = email
    newuser.password = password

    return dict(newuser)