
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base

class NewsPost(Base):
    __tablename__ = "news_posts"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    author = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)