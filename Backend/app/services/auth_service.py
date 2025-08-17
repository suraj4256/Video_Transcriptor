from fastapi import Form, HTTPException
from models.user_model import User
from database import db
from utils.config import create_user
from utils.security import get_password_hash


async def register_user(name:str, email: str, password: str, age:int) -> dict :
    # Check if the user already exists
    email = email.strip().lower()
    existing_user = db.users.find_one({"email": email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    data = create_user(name, email, password)
    data = dict(data)
    hashed_password = get_password_hash(data['password'])
    data['password'] = hashed_password
    # Insert the user into the database
    result = db.users.insert_one(data)
    print(result)

    # Check if the insertion was successful
    if not result.acknowledged:
        raise HTTPException(status_code=500, detail="User registration failed")
    
    # Return a success message or the created user data
    return {"message": "User registered successfully","success":True}


async def login_user(email: str, password: str) -> dict:
    # Here you would typically handle the login logic,
    # such as checking the credentials, generating a token, etc.
    return ({"Hello":"World"})