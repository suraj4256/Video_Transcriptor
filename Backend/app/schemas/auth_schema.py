from pydantic import BaseModel, Field, EmailStr



class UserRegister(BaseModel):
    id: int = Field(default=None, description="The unique identifier of the user", example=1)
    username: str = Field(..., description="The username of the user", example="johndoe")
    name: str = Field(..., description="The name of the user", example="John Doe")
    email: EmailStr = Field(..., description="The email of the user")
    password: str = Field(..., min_length=8, description="The password of the user, must be at least 8 characters long", example="strongpassword123")

class UserLogin(BaseModel):
    email: str = Field(...,description="Signed up email_id of the user")
    password: str = Field(..., description="Password set by the user")

class LoginResponse(BaseModel):
    access_token : str
    token_type : str = "bearer"