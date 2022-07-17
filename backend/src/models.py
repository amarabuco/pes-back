from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, BigInteger, DateTime
from sqlalchemy.orm import relationship

from database import Base

CNPJ = "pj.cnpj"

class PJ(Base):
    __tablename__ = "pj"
        
    cnpj = Column(String, primary_key=True, index=True)
    nome = Column(String)
    perfil = Column(String)

class Requisicao(Base):
    __tablename__ = "requisicao"
    
    DUV = Column(BigInteger,  primary_key=True, index=True)
    ETA = Column(DateTime)
    mercadoria = Column(String)
    peso = Column(Integer)    
    agencia = Column(Integer, ForeignKey(CNPJ))
    amarrador = Column(Integer, ForeignKey(CNPJ))
    rebocador = Column(Integer, ForeignKey(CNPJ))
    pratico = Column(Integer, ForeignKey(CNPJ))
    navio = Column(Integer, ForeignKey("navio.imo"))

class Navio(Base):
    __tablename__ = "navio"
    
    imo = Column(String, primary_key=True, index=True)
    nome = Column(String)
    loa = Column(Float)
    boca = Column(Float)
    dwt = Column(Float)
    ab = Column(Float)
    calado_entrada = Column(Float)
    calado_saida = Column(Float)
    calado_aereo = Column(Float)
    pontal = Column(Integer)
    lanca = Column(Integer)
    ano_construcao = Column(Integer)
    ultimo_porto = Column(String)
    proximo_porto = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    
    
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")