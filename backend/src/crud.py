from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_navio(db: Session, imo: int):
    return db.query(models.Navio).filter(models.Navio.imo == imo).first()

def create_navio(db: Session, navio: schemas.Navio):
    db_navio = models.Navio(**navio.dict())
    db.add(db_navio)
    db.commit()
    db.refresh(db_navio)
    return db_navio

def create_requisicao(db: Session, requisicao: schemas.RequisicaoBase):
    db_requisicao = models.Requisicao(**requisicao.dict())
    db.add(db_requisicao)
    db.commit()
    db.refresh(db_requisicao)
    return db_requisicao


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
