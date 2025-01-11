from fastapi import FastAPI

from routes.challenge import challenge
from routes.profile import profile
from routes.resume import resume
from routes.user import user



app = FastAPI()

app.include_router(user)
app.include_router(profile)
app.include_router(challenge)
app.include_router(resume)