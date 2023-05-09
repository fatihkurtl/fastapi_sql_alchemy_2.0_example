from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from datetime import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.sql import func

engine = create_engine("sqlite:///./my-site.db")
Base = declarative_base()

class Admin(Base):
    __tablename__ = "admin"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    token = Column(String, nullable=True, index=True, unique=True)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=True)
    
class Posts(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True, unique=True)
    hashtags = Column(String, nullable=False, index=True)
    reading_time = Column(String, nullable=False, index=True)
    category = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False, index=True)
    note = Column(String, nullable=True, index=True)
    code_space = Column(String, nullable=True, index=True)
    second_code_space = Column(String, nullable=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
class Snippets(Base):
    __tablename__ = "snippets"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True, unique=True)
    image = Column(String, nullable=False, index=True)
    hashtags = Column(String, nullable=False, index=True)
    reading_time = Column(String, nullable=False, index=True)
    category = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False, index=True)
    note = Column(String, nullable=True, index=True)
    code_space = Column(String, nullable=True, index=True)
    second_code_space = Column(String, nullable=True, index=True)
    is_active = Column(Boolean, default=True)
    reated_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()