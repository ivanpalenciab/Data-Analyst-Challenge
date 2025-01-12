from fastapi import File, APIRouter, UploadFile
import pandas as pd

from config.db import conn
from models.profile import profiles


profile = APIRouter()

@profile.post("/profile_migration/")
async def profile_migration(file:UploadFile = File(...)):
    """
    This endpoint receives a file that must be in CSV format to migrate profile table data to the database.
    For the process to be successful, the file must have the following columns:
    id (Integer), 
    user_id (Integer), 
    onboarding_goal (String), 
    created_at(Date),
    updated_at(Date)
    views(String).
    """
    if file.content_type not in ["text/csv"]:
        return {"error": "The file should be CSV."}
    try:
         data = pd.read_csv(file.file)
         for index, row in data.iterrows():
    # lets save in database
            query = profiles.insert().values(
                id=row["id"], 
                user_id=row["user_id"],
                onboarding_goal=row["onboarding_goal"],
                created_at=row["created_at"], 
                updated_at=row["updated_at"],
                views=row["views"])
            conn.execute(query)
            conn.commit()

         return "migration succeced"
    except Exception as e:
        return {"error": f"Error procesing the file: {str(e)}"}