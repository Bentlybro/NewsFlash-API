
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsPostBase(BaseModel):
    title: str
    content: str
    author: Optional[str] = None

class NewsPostCreate(NewsPostBase):
    pass

class NewsPost(NewsPostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True