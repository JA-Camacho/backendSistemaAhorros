from models.cuenta_ahorro import Cuenta_Ahorro
from sqlalchemy import text
from database.database import engine

def create_cuenta(cuenta: Cuenta_Ahorro):
    with engine.connect() as connection:
        query = text("INSERT INTO cuentas_ahorro (id_cuenta, id_usuario, saldo) VALUES (:id_cuenta, :id_usuario, :saldo)")
        connection.execute(query, id_cuenta=cuenta.id_cuenta, id_usuario=cuenta.id_usuario, saldo=cuenta.saldo)
    return {"mensaje": "Cuenta creada exitosamente", "cuenta": cuenta}

def delete_cuenta(cuenta: Cuenta_Ahorro):
    with engine.connect() as connection:
        query = text("DELETE FROM cuentas_ahorro WHERE id_cuenta = :id_cuenta")
        connection.execute(query, id_cuenta=cuenta.id_cuenta)