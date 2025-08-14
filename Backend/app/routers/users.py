from fastapi import Form, APIRouter
from services import auth_service
router = APIRouter(prefix='/auth', tags=["auth"])

@router.post('/register')
async def register(data:Form):
 return await auth_service.register_user(data)




@router.post('/login')
async def login():
 return {"Login":"Actually happened"}