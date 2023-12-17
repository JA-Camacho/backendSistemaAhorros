from fastapi import APIRouter, Depends, HTTPException
from controllers import create_cliente
from models.transaccion import Transaccion

router = APIRouter()

@router.post("/transacciones/")
async def create_transaccion(transaccion: Transaccion):
    return {"mensaje": "Transaccion exitosa", "transaccion": transaccion}
