from datetime import date

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id:Optional[int]
    name: str
    identification_number: int
    slug:str
    video: str
    email:str
    created_at: date
    updated_at: Optional[date]