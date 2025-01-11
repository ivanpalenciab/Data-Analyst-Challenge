from datetime import date

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id:Optional[int]
    user_id: int
    onboarding_goal: str
    created_at: date
    updated_at: date
    views:int