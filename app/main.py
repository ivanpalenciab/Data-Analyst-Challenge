from fastapi import FastAPI
from sqlalchemy import select

from routes.profile import profile
from routes.user import user

app = FastAPI()

app.include_router(user)
app.include_router(profile)