from fastapi import APIRouter, Depends, HTTPException
from models.cuenta_ahorro import Cuenta_Ahorro
from controllers.cuenta_controllers import create_cuenta, delete_cuenta

router = APIRouter()

@router.post("/cuentas/")
async def create_cuenta_endpoint(cuenta: Cuenta_Ahorro):
    result = create_cuenta(cuenta)
    return {"mensaje": "Cuenta creada exitosamente", "cuenta": result["cuenta"]}


@router.delete("/cuentas/")
async def delete_cuenta_endpoint(cuenta: Cuenta_Ahorro):
    result = delete_cuenta(cuenta)
    return {"mensaje": "Cliente eliminado correctamente"}