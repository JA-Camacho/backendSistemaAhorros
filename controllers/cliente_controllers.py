from models.cliente import Cliente
from database.database import engine

def create_cliente(cliente: Cliente):
    with engine.connect() as connection:
        connection.execute('insert into clientes values ({0},\'{1}\',\'{2}\',\'{3}\')'.
                           format(cliente.id_cliente,cliente.nombre,cliente.correo_electronico,cliente.password,cliente))
    return {"mensaje": "Cliente creado exitosamente", "cliente": cliente}

def delete_cliente(cliente: Cliente):
    with engine.connect() as connection:
        connection.execute('delete from clientes where id_cliente = {0}'.
                           format(cliente.id_cliente))
