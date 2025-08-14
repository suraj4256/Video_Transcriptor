from fastapi import FastAPI
from routers.users import router as users_router
app = FastAPI()

@app.get('/')
def readroot():
    return {"Hello":"World"}


app.include_router(users_router, prefix='/api')
