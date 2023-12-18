from models.cliente import Cliente
from sqlalchemy import text
from database.database import engine
from fastapi import HTTPException
import hashlib

def valor_md5(texto):
    md5 = hashlib.md5()
    md5.update(texto.encode('utf-8'))
    valor_md5 = md5.hexdigest()
    return valor_md5


def create_cliente(cliente: Cliente):
    with engine.connect() as connection:
        query = text("INSERT INTO clientes (id_cliente, nombre, correo_electronico, password) "
                     "VALUES (:id_cliente, :nombre, :correo_electronico, :password)")
        connection.execute(query, id_cliente=cliente.id_cliente, 
                           nombre=cliente.nombre, 
                           correo_electronico=cliente.correo_electronico, 
                           password=valor_md5(cliente.password))
    return {"mensaje": "Cliente creado exitosamente", "cliente": cliente}

def delete_cliente(cliente: Cliente):
    with engine.connect() as connection:
        query = text("DELETE FROM clientes WHERE id_cliente = :id_cliente")
        connection.execute(query, id_cliente=cliente.id_cliente)

def get_cliente(correo: str, contraseña: str):
    try:
        with engine.connect() as connection:
            query = text("SELECT id_cliente FROM clientes WHERE correo_electronico = :correo_electronico AND password = :contra_md5")
            result = connection.execute(query, correo_electronico=correo, contra_md5=valor_md5(contraseña)).fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Cliente no encontrado")

            cliente_id = result[0]
            return {"id_cliente": cliente_id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener cliente: {str(e)}")