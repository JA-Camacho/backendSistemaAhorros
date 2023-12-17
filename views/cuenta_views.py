from fastapi import APIRouter, Depends, HTTPException
from controllers import create_cliente
from models.cuenta_ahorro import Cuenta_Ahorro

router = APIRouter()

@router.post("/cuentas/")
async def create_cuenta(cuenta: Cuenta_Ahorro):
    return {"mensaje": "Cuenta creada exitosamente", "cuenta": cuenta}
