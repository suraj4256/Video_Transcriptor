from fastapi import Form

async def register_user(email: str, password: str) -> dict :
    # Here you would typically handle the registration logic,

    
    # such as validating the data, saving the user to the database, etc.
    
    return {"message": "User registered successfully"}


async def login_user(email: str, password: str) -> dict:
    # Here you would typically handle the login logic,
    # such as checking the credentials, generating a token, etc.
    return ({"Hello":"World"})