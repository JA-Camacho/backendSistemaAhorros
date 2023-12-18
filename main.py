from fastapi import FastAPI
from views.cliente_views import router as cliente_router
from database.database import engine

app = FastAPI()

def open_database_connection_pools():
    engine.connect()

def close_database_connection_pools():
    engine.disconnect()

app.add_event_handler("startup", open_database_connection_pools)
app.add_event_handler("shutdown", close_database_connection_pools)
app.include_router(cliente_router)

@app.get("/")
def read_root():
    return {"Hello":"World"}
