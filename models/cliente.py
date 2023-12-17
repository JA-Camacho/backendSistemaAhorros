from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    correo_electronico: str
    password: str
