from fastapi import FastAPI
from sqlalchemy import select

from config.db import conn
from models.user import users

app = FastAPI()

@app.get("/users")
async def get_user():
    stmt = select(users)
    result = conn.execute(stmt)

    for row in result:
        print(row)
    

