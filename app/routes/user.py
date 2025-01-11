from fastapi import File, APIRouter, UploadFile
import pandas as pd
from sqlalchemy import select

from models.user import users
from config.db import conn

user = APIRouter()

@user.get("/users/")
def get_user():
    try:
        stmt = select(users)
        result = conn.execute(stmt)

        users_list = []
        for row in result:
            user ={
                "id":row.id,#
                "name":row.name,
                "identification_number":row.identification_number,
                "slug":row.slug,
                "video":row.video,
                "email":row.email,
                "created_at":row.created_at,
                "updated_at":row.updated_at
            }
            users_list.append(user)
        
        return users_list

    except Exception as e:
        return {"error": f"Error geting data: {str(e)}"}
    
@user.post("/users_migration/")
async def user_migration(file:UploadFile = File(...)):
    if file.content_type not in ["text/csv"]:
        return {"error": "The file should be CSV."}
    try:
         data = pd.read_csv(file.file)
         for index, row in data.iterrows():
    # lets save in database
            query = users.insert().values(
                id=row["id"], 
                name=row["name"],
                identification_number=row["identification_number"],
                slug=row["slug"], 
                video=row["video"],
                email=row["email"],
                created_at=row["created_at"], 
                updated_at=row["updated_at"])
            conn.execute(query)
            conn.commit()

         return "migration succeced"
    except Exception as e:
        return {"error": f"Error procesing the file: {str(e)}"}