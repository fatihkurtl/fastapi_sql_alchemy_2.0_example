from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import models, schemas
from utils import crud
from models.models import SessionLocal, engine

Session = SessionLocal()

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post('/admin/', response_model=schemas.Admin)
def create_new_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    db_user = crud.get_admin_by_email(db, email=admin.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_admin(db=db, admin=admin)