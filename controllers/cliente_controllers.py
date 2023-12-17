from typing import List
from models import Cliente
from database import insert_cliente

def create_cliente(cliente: Cliente):
    return {"mensaje": "Cliente creado exitosamente", "cliente": cliente}


async def create_cliente(cliente: Cliente):
    await insert_cliente(cliente.nombre, cliente.correo_electronico, cliente.password)
    return {"mensaje": "Cliente creado exitosamente", "cliente": cliente.dict()}