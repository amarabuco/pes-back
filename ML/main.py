from typing import List
from fastapi import FastAPI, HTTPException


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello ML!!!"}

@app.get("/fila")
def get_fila(berco: str):
    return berco