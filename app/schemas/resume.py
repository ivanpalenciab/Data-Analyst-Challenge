from datetime import date

from pydantic import BaseModel
from typing import Optional

class Resume(BaseModel):
    id:Optional[int]
    user_id: int
    name: str
    type:str
    video: str
    views:int
    created_at: date