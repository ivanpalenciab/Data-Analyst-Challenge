from fastapi import FastAPI

from routes.profile import profile
from routes.user import user
from routes.challenge import challenge

app = FastAPI()

app.include_router(user)
app.include_router(profile)
app.include_router(challenge)