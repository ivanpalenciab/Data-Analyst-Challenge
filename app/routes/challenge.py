from fastapi import File, APIRouter, UploadFile
import pandas as pd
from sqlalchemy import select

from models.challenge import challenges
from config.db import conn

challenge = APIRouter()

@challenge.post("/challenge_migration/")
async def challenge_migration(file:UploadFile = File(...)):
    """
    This endpoint receives a file that must be in CSV format to migrate challenge table data to the database.
    For the process to be successful, the file must have the following columns:
    id (Integer), 
    name(String),  
    description(String), 
    status(String), 
    opencall_objective(String), 
    created_at(Date) 
    """
    if file.content_type not in ["text/csv"]:
        return {"error": "The file should be CSV."}
    try:
         data = pd.read_csv(file.file)
         for index, row in data.iterrows():
    # lets save in database
            query = challenges.insert().values(
                id=row["id"], 
                name=row["name"],
                description=row["description"],
                status=row["status"],
                opencall_objective=row["opencall_objective"],
                created_at=row["created_at"])
            conn.execute(query)
            conn.commit()

         return "migration succeced"
    except Exception as e:
        return {"error": f"Error procesing the file: {str(e)}"}