from datetime import datetime
from pydantic import BaseModel

class Transaccion(BaseModel):
    id_transaccion: int
    id_cuenta: int
    tipo_transaccion: int
    monto: float
    fecha_transaccion: datetime