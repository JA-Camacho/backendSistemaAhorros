from fastapi import APIRouter, Depends, HTTPException
from controllers import create_cliente
from models.cliente import Cliente

router = APIRouter()

@router.post("/clientes/", response_model=dict)
async def create_client_route(cliente: Cliente):
    return await create_cliente(cliente)

