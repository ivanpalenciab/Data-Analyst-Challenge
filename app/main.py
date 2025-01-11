from fastapi import FastAPI
from sqlalchemy import select

from routes.user import user

app = FastAPI()

app.include_router(user)