from sqlalchemy.orm import Session
from models import models, schemas

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext

def get_admin(db: Session, id: int):
    return db.query(models.Admin).filter(models.Admin.id == id).first()

def get_admin_by_email(db: Session, email: str):
    return db.query(models.Admin).filter(models.Admin.email == email).first()

def get_admin_by_password(db: Session, password: str):
    return db.query(models.Admin).filter(models.Admin.hashed_password == password).first()

def get_admin_by_token(db: Session, token: str):
    return db.query(models.Admin).filter(models.Admin.token == token).first()

def get_posts(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.Posts).offset(skip).limit(limit).all()

def get_snippets(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Snippets).offset(skip).limit(limit).all()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password): 
    return pwd_context.hash(password)

def create_admin(db: Session, admin: schemas.AdminCreate): 
    hashed_password = get_password_hash(admin.password) 
    db_admin = models.Admin(email=admin.email, hashed_password=hashed_password) 
    db.add(db_admin) 
    db.commit() 
    db.refresh(db_admin) 
    return db_admin


