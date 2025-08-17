from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from routers.users import router as users_router
from typing import Annotated
from database import db


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def readroot():
    collections = db.list_collection_names()
    return {"message": "Welcome to the Video Streaming API", "collections": collections}



app.include_router(users_router, prefix='/api')
