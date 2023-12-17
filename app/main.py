"""
Integrantes:
José Camacho
Gilmar Campoverde
Josue Cueva
Santiago Miño
"""
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()

#classes
class Cliente(BaseModel):
    id_cliente: int
    nombre:str
    correo_electronico:str
    password:str

class Cuenta_Ahorro(BaseModel):
    id_cuenta: int
    saldo: float
    id_usuario: int

class Transaccion(BaseModel):
    id_transaccion:int
    id_cuenta:int
    tipo_transaccion:int
    monto:float
    fecha_transaccion: datetime  

fake_db = []

#controllers

#Routes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/clientes/")
async def create_cliente(cliente: Cliente):
    return {"mensaje": "Cliente creado exitosamente", "cliente": cliente}

@app.post("/cuentas/")
async def create_cuenta(cuenta: Cuenta_Ahorro):
    return {"mensaje": "Cuenta creada exitosamente", "cuenta": cuenta}

@app.post("/transacciones/")
async def create_transaccion(transaccion: Transaccion):
    return {"mensaje": "Transaccion exitosa", "transaccion": transaccion}




database.connect()

@app.on_event("startup")
async def startup_db_client():
    database.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    database.disconnect()