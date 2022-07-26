from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello Santos!!!"}

@app.get("/requisicao", response_model=List[schemas.RequisicaoBase])
def read_reqs(db: Session = Depends(get_db)):
    reqs = crud.get_reqs(db)
    return reqs

@app.get("/requisicao/{duv}", response_model=schemas.RequisicaoBase)
def read_reqs(duv: int, db: Session = Depends(get_db)):
    req = crud.get_req_by_duv(db, duv)
    return req

@app.get("/navios", response_model=List[schemas.Navio])
def read_navios(db: Session = Depends(get_db)):
    navios = crud.get_navios(db)
    return navios

@app.get("/navios/{imo}", response_model=schemas.Navio)
def read_navios(imo: str, db: Session = Depends(get_db)):
    navio = crud.get_navio_by_imo(db, imo)
    return navio

@app.post("/requisicao",  response_model=schemas.Navio)
async def requisicao(requisicao: schemas.RequisicaoBase, navio: schemas.Navio, db: Session = Depends(get_db)):
    db_navio = crud.get_navio(db, imo=navio.imo)
    print(db_navio)
    if db_navio is None:
        db_navio = crud.create_navio(db=db, navio=navio)
    requisicao.navio = db_navio.imo
    requisicao = crud.create_requisicao(db=db, requisicao=requisicao)
    return requisicao


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_fdocs_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

