from datetime import date

from pydantic import BaseModel
from typing import Optional

class Challenge(BaseModel):
    id:Optional[int]
    name: str
    descripion: str
    status:str
    opencall_objective: str
    created_at: date