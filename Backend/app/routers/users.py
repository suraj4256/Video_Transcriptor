from fastapi import Form, APIRouter
from services import auth_service
from schemas.auth_schema import LoginResponse

router = APIRouter(prefix='/auth', tags=["auth"], default_response_class=LoginResponse)

@router.post('/register', response_model=LoginResponse)
async def register(email: str = Form(...), password: str = Form(...)) -> dict:
    return await auth_service.register_user(email=email, password=password)




@router.post('/login', response_model=LoginResponse)
async def login(email: str = Form(...), password: str = Form(...)) -> dict:
    return await auth_service.login_user(email=email, password=password)