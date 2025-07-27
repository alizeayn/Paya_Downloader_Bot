from sqlalchemy import Column, Integer, String
from data.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    language = Column(String, default="en")