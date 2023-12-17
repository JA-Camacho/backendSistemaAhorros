# backendSistemaAhorros/main.py
from fastapi import FastAPI
from app import create_cliente, create_cuenta, create_transaccion

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/clientes/")
async def post_cliente(cliente: Cliente):
    return create_cliente(cliente)

@app.post("/cuentas/")
async def post_cuenta(cuenta: Cuenta_Ahorro):
    return create_cuenta(cuenta)

@app.post("/transacciones/")
async def post_transaccion(transaccion: Transaccion):
    return create_transaccion(transaccion)
