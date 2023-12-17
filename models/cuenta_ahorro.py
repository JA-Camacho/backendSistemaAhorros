from pydantic import BaseModel

class Cuenta_Ahorro(BaseModel):
    id_cuenta: int
    saldo: float
    id_usuario: int
