from datetime import datetime, time, timedelta, date
from typing import List, Union
from uuid import UUID

from pydantic import BaseModel, Field, ValidationError, validator


class RequisicaoBase(BaseModel):
    DUV: int
    ETA: datetime
    mercadoria: str
    peso: int
    
    navio: Union[int, None]
    agencia: Union[int, None]
    amarrador: Union[int, None]
    rebocador: Union[int, None]
    pratico: Union[int, None]
    
    @validator('ETA')
    def datetime_format(cls, v):
        if type(v) != type(datetime.now()) :
            v = datetime.strptime(v, '%d/%m/%Y %H:%M:%S')
        return v
    
    class Config:
        orm_mode = True

class RequisicaoUpdate(RequisicaoBase):  
    pass

class PJ(BaseModel):
    cnpj: str
    nome: str
    perfil: str
    
    class Config:
        orm_mode = True
    
class Navio(BaseModel):
    imo: str = Field(default=None, title="1131428")
    nome: str = Field(default=None, title="Titanic", max_length=300)
    loa: float = Field(default=None, title="269")
    boca: float = Field(default=None, title="28.2")
    dwt: float = Field(default=None, title="Titanic")
    ab: float
    calado_entrada: float = Field(default=None, title="10.5")
    calado_saida: float
    calado_aereo: float
    pontal: float = Field(default=None, title="53.3")
    lanca: Union[float, None]
    ano_construcao: int  = Field(default=None, title="1909")
    ultimo_porto: str
    proximo_porto: str
   
    
    class Config:
        orm_mode = True
    
class Agencia(BaseModel):
    cnpj: str
    

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
        