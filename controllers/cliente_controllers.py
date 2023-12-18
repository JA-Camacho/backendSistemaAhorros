from models.cliente import Cliente
from sqlalchemy import text
from database.database import engine

def create_cliente(cliente: Cliente):
    with engine.connect() as connection:
        query = text("INSERT INTO clientes (id_cliente, nombre, correo_electronico, password) "
                     "VALUES (:id_cliente, :nombre, :correo_electronico, :password)")
        connection.execute(query, id_cliente=cliente.id_cliente, 
                           nombre=cliente.nombre, 
                           correo_electronico=cliente.correo_electronico, 
                           password=cliente.password)
    return {"mensaje": "Cliente creado exitosamente", "cliente": cliente}

def delete_cliente(cliente: Cliente):
    with engine.connect() as connection:
        query = text("DELETE FROM clientes WHERE id_cliente = :id_cliente")
        connection.execute(query, id_cliente=cliente.id_cliente)