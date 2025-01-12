from fastapi import File, APIRouter, UploadFile
import pandas as pd

from config.db import conn
from models.resume import resumes


resume = APIRouter()

@resume.post("/resume_migration/")
async def resume_migration(file:UploadFile = File(...)):
    """
    This endpoint receives a file that must be in CSV format to migrate resume table data to the database.
    For the process to be successful, the file must have the following columns:
    id (Integer), 
    user_id (Integer), 
    name(String), 
    type(String), 
    video(String), 
    views(String), 
    created_at(Date).
    """
    if file.content_type not in ["text/csv"]:
        return {"error": "The file should be CSV."}
    try:
         data = pd.read_csv(file.file)
         for index, row in data.iterrows():
    # lets save in database
            query = resumes.insert().values(
                id=row["id"], 
                user_id=row["user_id"],
                name=row["name"],
                type=row["type"],
                video=row["video"],
                views=row["views"],
                created_at=row["created_at"])
            conn.execute(query)
            conn.commit()

         return "migration succeced"
    except Exception as e:
        return {"error": f"Error procesing the file: {str(e)}"}