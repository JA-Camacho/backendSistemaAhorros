from models import Transaccion
from sqlalchemy import text
from fastapi import HTTPException
from database.database import engine

def create_transaccion(transaccion: Transaccion):
    try:
        with engine.connect() as connection:
            query = text("INSERT INTO transacciones (id_cuenta, tipo_transaccion, monto, fecha_transaccion) "
                         "VALUES (:id_cuenta, :tipo_transaccion, :monto, :fecha_transaccion)")
            connection.execute(query, id_cuenta=transaccion.id_cuenta,
                               tipo_transaccion=transaccion.tipo_transaccion,
                               monto=transaccion.monto,
                               fecha_transaccion=transaccion.fecha_transaccion)

            return {"mensaje": "Transacción exitosa", "transaccion": transaccion.dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear transacción: {str(e)}")

def get_transacciones(id_cuenta: int):
    try:
        with engine.connect() as connection:
            query = text("SELECT tipo_transaccion, monto FROM transacciones WHERE id_cuenta = :id_cuenta")
            result = connection.execute(query, id_cuenta=id_cuenta).fetchall()

            transacciones_data = [{"tipo_transaccion": row[0], "monto": row[1]} for row in result]
            return transacciones_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener transacciones de la cuenta: {str(e)}")