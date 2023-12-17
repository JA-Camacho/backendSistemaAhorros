# backendSistemaAhorros/models.py
from pydantic import BaseModel
from datetime import datetime

class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    correo_electronico: str
    password: str

class Cuenta_Ahorro(BaseModel):
    id_cuenta: int
    saldo: float
    id_usuario: int

class Transaccion(BaseModel):
    id_transaccion: int
    id_cuenta: int
    tipo_transaccion: int
    monto: float
    fecha_transaccion: datetime
