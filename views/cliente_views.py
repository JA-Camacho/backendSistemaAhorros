from fastapi import APIRouter, Depends, HTTPException
from models.cliente import Cliente
from controllers.cliente_controllers import create_cliente, delete_cliente

router = APIRouter()

@router.post("/clientes/")
async def create_cliente_endpoint(cliente: Cliente):
    result = create_cliente(cliente)
    return {"mensaje": "Cliente creado exitosamente", "cliente": result["cliente"]}


@router.delete("/clientes/")
async def delete_cliente_endpoint(cliente: Cliente):
    result = delete_cliente(cliente)
    return {"mensaje": "Cliente eliminado correctamente"}
