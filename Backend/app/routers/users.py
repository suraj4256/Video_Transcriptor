from fastapi import Form, APIRouter
from services import auth_service
from schemas.auth_schema import LoginResponse, UserLogin, UserRegister

router = APIRouter(prefix='/auth', tags=["auth"])

@router.post('/register')
async def register(name:str = Form(...), email: str = Form(...), password: str = Form(...), age: int|None = Form()) -> dict:
    user_data = UserRegister(name = name, email=email, password=password, age=age)
    return await auth_service.register_user(name=user_data.name,email=user_data.email, password=user_data.password, age=user_data.age)


@router.post('/login', response_model=LoginResponse)
async def login(email: str = Form(...), password: str = Form(...)) -> dict:
    user_data = UserLogin(email=email, password=password)
    return await auth_service.login_user(email=user_data.email, password=user_data.password)