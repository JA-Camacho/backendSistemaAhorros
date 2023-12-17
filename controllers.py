# backendSistemaAhorros/controllers.py
from typing import List
from datetime import datetime
from app.models import Cliente, Cuenta_Ahorro, Transaccion

fake_db = []

def create_cliente(cliente: Cliente):
    # Lógica para crear un cliente
    return {"mensaje": "Cliente creado exitosamente", "cliente": cliente}

def create_cuenta(cuenta: Cuenta_Ahorro):
    # Lógica para crear una cuenta de ahorro
    return {"mensaje": "Cuenta creada exitosamente", "cuenta": cuenta}

def create_transaccion(transaccion: Transaccion):
    # Lógica para crear una transacción
    return {"mensaje": "Transaccion exitosa", "transaccion": transaccion}
